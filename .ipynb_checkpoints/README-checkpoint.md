# Metadata Repository

This repository is used during the summer school for storing and managing device metadata. Use the `make_label.py` script to generate all necessary files including QR code labels and JSON metadata for your devices. After generating your files, please commit and push them to the repository.

Make sure you have permission to push to this repository. If you are not sure, please ask the organizer. Please follow these steps to generate an access token: 

1. Log in at [RWTH-Aachen GitLab instance](https://git.rwth-aachen.de/users/sign_in) with `DFN-AAI` or `GitHub account`.
2. Click your avatar on the top left of the webpage after logging in and select `Preferences`. The text after @ is your username.
3. Then go to `Access tokens` on the left side and select `Add new token` on the right side of the page.
4. Give it a name like `summer school 2025`, activate `write_repository` and `read_repository`, then hit `create token`.
5. Copy the token somewhere safe, you can only see it once. However, you can always delete old tokens and generate new ones.
6. If git asks for your username and password, you should use the access token as the password.

## Label Maker Usage

Follow these steps to set up the environment and generate device labels:

```bash
# Clone the repository
git clone https://git.rwth-aachen.de/fst-tuda/public/lehre/metadata-alex-summer-school.git

# Set up Python environment if not already done
cd metadata-alex-summer-school
python -m venv venv
source venv/bin/activate
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
