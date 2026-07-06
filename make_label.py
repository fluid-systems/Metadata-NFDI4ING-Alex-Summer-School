from labelmaker.maker import generate_files


def main():
    # This script will create directories for each device defined in the list below containing:
    # - device.json: Metadata template with device information
    # - label.pdf: Printable QR code label
    # - qr.svg: QR code in SVG format

    # Documentation for the generate_files function:

    # Generate device metadata templates and QR code labels.
    # This function processes a list of device information dictionaries and generates
    # the corresponding files for each device, including JSON metadata files and
    # QR code labels. Each device gets its own directory named after its UUID.

    # Args:
    #     devices_information (list[dict]): List of dictionaries containing device information.
    #         Each dictionary should contain:
    #             - device_type (str): Type of sensor/device (required). Must be one of
    #               the supported types: temperature, acceleration, raspberrypi, kettle.
    #             - uuid (str, optional): Unique identifier for the device. If not provided,
    #               a new UUID will be generated.
    #             - message (str, optional): Custom message to include in the label.
    #               Defaults to empty string.
    #     generate_path (str or Path, optional): Directory path where device folders
    #         will be created. Defaults to the root directory of this repository.

    # Raises:
    #     ValueError: If device_type is missing or not supported.
    #     TypeError: If generate_path is not a string or Path object.


    devices_information = [
        {
            # Raspberry Pi device with a specific UUID
            "device_type": "raspberrypi",
            # Pre-defined UUID
            #"uuid": "1f051e50-70f8-686a-aa62-bc0e1b38e956",
            # Custom message for the label, please think of meaningful message.
            "message": "Located at Table 1 - Sharifi,Gast - 2026-07-06",
        },
        {
            "device_type": "temperature",
        },
        {
            "device_type": "temperature",
        },
        {
            "device_type": "acceleration",
        },
        {
            "device_type": "kettle",
            "message": "Located at Table 1 - Sharifi,Gast - 2026-07-06",
        }
    ]

    generate_files(devices_information)


if __name__ == "__main__":
    main()
