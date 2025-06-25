# Metadata Repository

This repository is used during the summer school for storing and managing device metadata. Use the `make_label.py` script to generate all necessary files including QR code labels and JSON metadata for your devices. After generating your files, please commit and push them to the repository.

## Label Maker Usage

Follow these steps to set up the environment and generate device labels:

```bash
# Clone the repository
git clone https://git.rwth-aachen.de/fst-tuda/public/lehre/metadata-alex-summer-school.git

# Set up Python environment
cd metadata-alex-summer-school
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Generate device files (labels and metadata)
python make_label.py
```

## What Gets Generated

When you run the script, it creates:
- **Device directories**: Named after each device's UUID
- **QR code labels** (`label.pdf`): Printable labels with QR codes and device information
- **QR code SVG files** (`qr.svg`): Vector format QR codes
- **Metadata files** (`device.json`): JSON files containing device specifications
