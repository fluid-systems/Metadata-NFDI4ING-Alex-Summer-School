import json
from pathlib import Path

from uuid6 import uuid6

from labelmaker import utilities

SUPPORTED_DEVICES_TYPES = [
    "temperature",
    "acceleration",
    "raspberrypi",
    "kettle",
]


def generate_files(
    devices_information: list[dict],
    generate_path: [str, Path] = Path(__file__).parent.parent,
):
    """Generate device metadata templates and QR code labels.

    This function processes a list of device information dictionaries and generates
    the corresponding files for each device, including JSON metadata files and
    QR code labels. Each device gets its own directory named after its UUID.

    Args:
        devices_information (list[dict]): List of dictionaries containing device information.
            Each dictionary should contain:
                - device_type (str): Type of sensor/device (required). Must be one of
                  the supported types: temperature, acceleration, raspberrypi, kettle.
                - uuid (str, optional): Unique identifier for the device. If not provided,
                  a new UUID will be generated.
                - message (str, optional): Custom message to include in the label.
                  Defaults to empty string.
        generate_path (str or Path, optional): Directory path where device folders
            will be created. Defaults to the root directory of this repository.

    Raises:
        ValueError: If device_type is missing or not supported.
        TypeError: If generate_path is not a string or Path object.

    """
    _generate_dir(generate_path)

    for device in devices_information:
        device_type: str = device.get("device_type", None)
        if device_type is None:
            raise ValueError("Sensor type is required in device information.")

        device_type = device_type.strip().lower()
        if device_type not in SUPPORTED_DEVICES_TYPES:
            raise ValueError(
                f"Unsupported sensor type: {device_type}. Supported types are: {SUPPORTED_DEVICES_TYPES}"
            )

        uuid = device.get("uuid", _generate_uuid())
        http_link = device.get("link", None)
        _generate_dir(generate_path / uuid)

        message = device.get("message", "")
        path_for_generated_files = generate_path / uuid

        data_dict = {
            "internal_id": uuid,
            "product_name": device_type,
            "message": message,
            "link": http_link,
            "p_id": device.get("p_id", ""),
        }

        _generate_json_file(device_type, uuid, path_for_generated_files)

        _generate_label(data_dict, path_for_generated_files)


def _generate_label(
    data_dict: dict,
    path_for_generated_files: [str, Path],
):
    if isinstance(path_for_generated_files, str):
        path_for_generated_files = Path(path_for_generated_files)
    path_for_generated_files.mkdir(parents=True, exist_ok=True)

    assert "internal_id" in data_dict
    assert "product_name" in data_dict
    assert "message" in data_dict

    # Name the file after the uuid.
    label_file_path: Path = Path(path_for_generated_files / "label.pdf")
    qr_code_file_path: Path = Path(path_for_generated_files / "qr.svg")

    # Generate the QR code and the QR code label.
    if "link" in data_dict:
        qr_content = data_dict["link"]
    else:
        qr_content = data_dict["internal_id"]
    utilities.generate_QR_code(qr_content, qr_code_file_path)
    print("[INFO] QR code generated at: {}".format(qr_code_file_path))
    utilities.generate_pID_QR_code_label(label_file_path, qr_code_file_path, data_dict)
    print("[INFO] Label generated at: {}".format(label_file_path))


def _generate_json_file(
    device_type: str, uuid: str, path_for_generated_files: [str, Path]
):
    # check if file exists
    if isinstance(path_for_generated_files, str):
        path_for_generated_files = Path(path_for_generated_files)
    if (path_for_generated_files / "device.json").exists():
        print(
            "[INFO] device.json file already exists: {}, nothing to do.".format(
                path_for_generated_files
            )
        )
        return

    with open(
        Path(__file__).parent / "json-templates" / "{}.json".format(device_type), "r"
    ) as template_file:
        json_dict = json.load(template_file)
    json_dict["JSON"]["ID"] = uuid
    with open(Path(path_for_generated_files / "device.json"), "w") as json_file:
        json.dump(json_dict, json_file, indent=4)
        print(
            "[INFO] Metadata for {} generated at: {}".format(
                device_type, path_for_generated_files / "device.json"
            )
        )


def _generate_uuid():
    return str(uuid6())


def _generate_dir(dir: [str, Path]) -> Path:
    if isinstance(dir, str):
        path = Path(dir)
        path.mkdir(parents=True, exist_ok=True)
    elif isinstance(dir, Path):
        dir.mkdir(parents=True, exist_ok=True)
        return dir
    else:
        raise TypeError("generate_path must be a string or a Path object.")
