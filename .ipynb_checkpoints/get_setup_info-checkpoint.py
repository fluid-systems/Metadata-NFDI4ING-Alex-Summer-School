import json
from typing import Any, Dict

from functions.m_json import get_json_entry, get_json_file_from_gitlab


def main():
    print("[INFO] Getting setup information...")
    print()

    parse_setup_file("datasheets/setup_template.json", debug=False)

    print("[INFO] Finished getting setup information.")


def parse_setup_file(file_path: str, debug: bool = False):
    """Parse a setup JSON file and retrieve device information from GitLab.

    Args:
        file_path (str): Path to the JSON setup file to parse
        debug (bool, optional): If True, prints the complete JSON data from GitLab.
            Defaults to False.

    """
    # read setup file
    with open(file_path, "r") as file:
        try:
            print("[INFO] Parsing JSON file <{}>...".format(file_path))
            json_data = json.load(file)
            print("[INFO] {}".format(json_data.get("comment", "")))
        except json.JSONDecodeError:
            print("[ERROR] JSON file <{}> is not valid.".format(file_path))
            return

    print("[INFO] Found {} devices in setup.".format(len(json_data["setup"])))
    # print information about each device
    for device in json_data["setup"]:
        print("[INFO] Device {} found".format(device))
        # print information in setup file if available
        metainfo = json_data["setup"][device]
        if metainfo:
            for key, item in metainfo.items():
                print("\t{}: {}".format(key, item))

        # get JSON data of device from GitLab
        device_json_data = get_json_file_from_gitlab(device)
        # print basic information about device
        get_info_in_data_sheet(device_json_data)

        # print the hole JSON file on Gitlab if debug is True
        if debug and device_json_data:
            print("[DEBUG] {}".format(device_json_data))
        print()


def get_info_in_data_sheet(json_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract and display information from device JSON data.

    Args:
        json_data (Dict[str, Any]): JSON data containing device information with keys
            like 'sensor', 'probe', or 'instrument'

    Returns: Dict[str, Any]: Dictionary containing extracted device information
            (uuid, name, type, serial if applicable)

    """
    if "device" in json_data:
        info = {
            "uuid": get_json_entry(json_data, ["JSON", "ID"]),
            "name": get_json_entry(json_data, ["device", "name"]),
            "type": get_json_entry(json_data, ["device", "type"]),
        }
        if "serial" in json_data["device"]:
            info["serial"] = get_json_entry(json_data, ["device", "serial"])
        print("Got {} with the following information:".format(info["name"]))
    else:
        print("[ERROR] Unknown JSON data structure.")
        return {}

    for key, value in info.items():
        print("\t{}: {}".format(key, value))
    return info


if __name__ == "__main__":
    main()
