import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class FileDialogExample(QMainWindow):
   def __init__(self):
      super().__init__()

      self.initUI()

   def initUI(self):
      self.setWindowTitle("QFileDialog Example")
      self.setGeometry(100, 100, 400, 300)

      self.button = QPushButton("Open File", self)
      self.button.clicked.connect(self.openFileDialog)
      self.button.setGeometry(150, 150, 100, 30)

   def openFileDialog(self):
      file_dialog = QFileDialog(self)
      file_dialog.setWindowTitle("Open File")
      file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
      file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

      if file_dialog.exec():
         selected_files = file_dialog.selectedFiles()
         print("Selected File:", selected_files[0])

def main():
   app = QApplication(sys.argv)
   window = FileDialogExample()
   window.show()
   sys.exit(app.exec())

if __name__ == "__main__":
   main()