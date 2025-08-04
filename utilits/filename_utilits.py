
symbols = [
    '/',
    '>',
    '<',
    ':',
    '\\',
    '|',
    '?',
    '*'
]
names = [
    "CON",
    "PRN",
    "AUX",
    "NUL",
    "COM1",
    "COM2",
    "COM3",
    "COM4",
    "COM5",
    "COM6",
    "COM7",
    "COM8",
    "COM9",
    "LPT1",
    "LPT2",
    "LPT3",
    "LPT4",
    "LPT5",
    "LPT6",
    "LPT7",
    "LPT8",
    "LPT9"
]

def check_filename(filename: str):
    for symbol in symbols:
        if symbol in filename:
            return False
    for name in names:
        if filename.lower() == name.lower():
            return False

    return True