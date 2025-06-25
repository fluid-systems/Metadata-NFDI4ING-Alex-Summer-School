from labelmaker.maker import generate_files


def main():
    """Main function to generate labels and metadata for sample devices."""
    # Generate files for a list of predefined devices
    # This will create directories for each device containing:
    # - device.json: Metadata template with device information
    # - label.pdf: Printable QR code label
    # - qr.svg: QR code in SVG format
    generate_files(
        devices_infomation=[
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


if __name__ == "__main__":
    main()
