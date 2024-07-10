import tkinter as tk
from tkinter import messagebox, ttk
import random
import os

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

# Class for the main application
class AutoPromptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoPrompt v1.4")

        self.prompt_text = tk.StringVar()

        self.textbox = tk.Entry(root, textvariable=self.prompt_text, width=80)
        self.textbox.pack(pady=10)

        self.check_vars = {}
        self.checkbuttons = []

        self.name_of_files = get_filename()
        self.create_checkboxes()

        self.generate_button = ttk.Button(root, text="Generate Prompt", command=self.generate_prompt)
        self.generate_button.pack(pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)
        
        # Add About button
        self.about_button = ttk.Button(root, text="About", command=self.show_about)
        self.about_button.pack(pady=10)

    def create_checkboxes(self):
        frame = ttk.Frame(self.root)
        frame.pack()

        col_count = 0
        row_count = 0

        for idx, name in enumerate(self.name_of_files):
            var = tk.BooleanVar()
            checkbutton = ttk.Checkbutton(frame, text=name, variable=var)
            checkbutton.grid(row=row_count, column=col_count, sticky='w')
            self.check_vars[name] = var
            self.checkbuttons.append(checkbutton)

            row_count += 1
            if row_count >= 15:
                row_count = 0
                col_count += 1

    def generate_prompt(self):
        selected_parts = [name for name, var in self.check_vars.items() if var.get()]
        if selected_parts:
            prompt = ", ".join(select_random_line_from_csv_file(part) for part in selected_parts)
        else:
            prompt = select_random_line_from_collection()
        self.prompt_text.set(prompt.strip())

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.prompt_text.get())

    def show_about(self):
        messagebox.showinfo("About", "Autoprompt generates random prompts to be used for AI Image generation using any platform. The purpose is to help users of all experience lvls expand their prompting for better generation results.\nIt is a good idea to make a note of the prompts you like to circle back to and curate your own arsenal of prompts.\n\nVersion 1.4\nBuild Date:\nJuly 10 2024\n\nHelp:\n\nTo Generate a prompt place a check in the boxes. Think of these boxes as containers with a bunch of random prompts. The final prompt will be combined with a comma inbetween the random strings pulled from the boxes.\nYou do not need to change check boxes to get a new random prompt.\nPaste the prompt into your favorite AI-image gen. platform.\n\nEnjoy.\n\nVisit GitHub for more information and updates.\nhttps://github.com/noarche/AutoPrompt")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoPromptApp(root)
    root.mainloop()
