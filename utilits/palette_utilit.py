from PyQt6.QtGui import QPalette, QColor


def get_palette(r,g,b):
    palette = QPalette()
    palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, QColor(r,g,b)) # TODO: choose color role later
    return palette