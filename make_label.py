from labelmaker.maker import generate_files


def main():
    """Main function to generate labels and metadata for sample devices."""
    # Generate files for a list of predefined devices
    # This will create directories for each device containing:
    # - device.json: Metadata template with device information
    # - label.pdf: Printable QR code label
    # - qr.svg: QR code in SVG format

    devices_infomation = (
        [
            {
                # Raspberry Pi device with a specific UUID
                "device_type": "raspberrypi",
                "uuid": "1f051e50-70f8-686a-aa62-bc0e1b38e956",  # Pre-defined UUID
                "message": "Raspberry Pi as example",  # Custom message for the label
            },
            {
                # Kettle device - UUID will be auto-generated
                "device_type": "kettle",
                # Note: No UUID specified, so a new one will be generated automatically
            },
        ],
    )

    # Documentation of generate_files funktion:

    # Generate devices metadata template and QR code labels.
    # This function processes a list of device information dictionaries and generates
    # the corresponding files for each device, including JSON metadata files and
    # QR code labels. Each device gets its own directory named after its UUID.

    # Args:
    #     devices_infomation (list[dict]): List of dictionaries containing device information.
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

    generate_files(devices_infomation)


if __name__ == "__main__":
    main()
