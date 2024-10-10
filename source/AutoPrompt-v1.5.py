import os
import random
from PyQt6 import QtWidgets, QtCore, QtGui
import sys

# Change to the script directory
script_directory = os.path.dirname(__file__)
os.chdir(script_directory)
folder_path = os.path.join(script_directory, "parts")

# Function to get filenames
def get_filename():
    name = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            name.append(filename[3:-4])
    return name

# Function to select a random line from the collection file
def select_random_line_from_collection():
    file_path = os.path.join(folder_path, "collection.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        readline = random.choice(lines).strip()
        return readline

# Function to select a random line from a specific CSV file
def select_random_line_from_csv_file(file):
    chosen_lines = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv") and filename[3:-4] == file:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file_content:
                lines = file_content.readlines()
                if lines:
                    chosen_lines.append(random.choice(lines).strip())
    return "".join(chosen_lines)

# Main Application Class
class AutoPromptApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("AutoPrompt v1.5")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(34, 34, 34, 0.9);
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #333333;
                color: white;
                padding: 5px;
            }
            QPushButton {
                background-color: #555555;
                border: 1px solid #444444;
                padding: 8px;
                color: white;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QLabel {
                font-size: 16px;
            }
            QCheckBox {
                color: cyan;
            }
        """)

        self.init_ui()

    def init_ui(self):
        # Layouts
        layout = QtWidgets.QVBoxLayout()
        
        # Prompt input box
        self.prompt_input = QtWidgets.QLineEdit(self)
        self.prompt_input.setPlaceholderText("Generated prompt will appear here")
        layout.addWidget(self.prompt_input)

        # Checkbox area for CSV files
        self.checkbox_layout = QtWidgets.QGridLayout()
        layout.addLayout(self.checkbox_layout)

        # Add checkboxes for each CSV file
        self.check_vars = {}
        self.add_checkboxes()

        # Generate Prompt button
        self.generate_button = QtWidgets.QPushButton("Generate Prompt", self)
        self.generate_button.clicked.connect(self.generate_prompt)
        layout.addWidget(self.generate_button)

        # Copy to Clipboard button
        self.copy_button = QtWidgets.QPushButton("Copy to Clipboard", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)

        # About button
        self.about_button = QtWidgets.QPushButton("About", self)
        self.about_button.clicked.connect(self.show_about)
        layout.addWidget(self.about_button)

        self.setLayout(layout)

    def add_checkboxes(self):
        name_of_files = get_filename()
        row_count = 0
        col_count = 0

        for idx, name in enumerate(name_of_files):
            checkbox = QtWidgets.QCheckBox(name)
            self.checkbox_layout.addWidget(checkbox, row_count, col_count)
            self.check_vars[name] = checkbox

            row_count += 1
            if row_count >= 15:
                row_count = 0
                col_count += 1

    def generate_prompt(self):
        selected_parts = [name for name, checkbox in self.check_vars.items() if checkbox.isChecked()]
        if selected_parts:
            prompt = ", ".join(select_random_line_from_csv_file(part) for part in selected_parts)
        else:
            prompt = select_random_line_from_collection()
        self.prompt_input.setText(prompt.strip())

    def copy_to_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.prompt_input.text())

    def show_about(self):
        QtWidgets.QMessageBox.information(self, "About", 
            "Autoprompt generates random prompts for AI image generation platforms.\n"
            "The purpose is to help users expand their prompting for better generation results.\n"
            "Select CSV files, generate a prompt, and paste it into your favorite platform.\n\n"
            "Version 1.5\nBuild Date: July 10 2024\n\nVisit GitHub for more information and updates:\nhttps://github.com/noarche/AutoPrompt")


# Run the Application
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AutoPromptApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

