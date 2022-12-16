from pathlib import Path

FLOAT_REGEX = r"^\d*[.,]?\d*$"
PHONE_NUMBER_REGEX = r"^([0-9\(\)\/\+ \-]*)$"
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

DATA_DIR = Path(__file__).parent.parent / "data"
IMAGES_DIR = DATA_DIR / "images"
