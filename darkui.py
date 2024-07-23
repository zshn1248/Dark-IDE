import customtkinter as ctk
from tkinter import filedialog, messagebox

# Initialize the customtkinter library
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DarkCodeEditor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dark - Code Editor")
        self.geometry("800x600")

        # Configure grid layout (1 row, 1 column)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a CTkTextbox widget
        self.textbox = ctk.CTkTextbox(self, wrap='none')
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # Create a CTkFrame for buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, sticky="nsew")
        
        # Create 

        # Open and Save buttons
        self.open_button = ctk.CTkButton(self.button_frame, text="Open", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.button_frame, text="Save", command=self.save_file)
        self.save_button.grid(row=0, column=1, padx=5, pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox.delete(1.0, ctk.END)
                self.textbox.insert(ctk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.textbox.get(1.0, ctk.END)
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")

if __name__ == "__main__":
    app = DarkCodeEditor()
    app.mainloop()
