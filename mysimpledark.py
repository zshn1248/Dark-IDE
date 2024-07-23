import customtkinter
from tkinter import filedialog, messagebox
            
customtkinter.set_appearance_mode("dark")
import customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1) # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.textbox = customtkinter.CTkTextbox(master=self, width=1280, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.btn = customtkinter.CTkButton(self, text= "Save", command= self.saveFile)
        self.btn.grid(row = 1, column = 0, sticky = "ns")
    def saveFile(self):
        filepath = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension= "*.py", filetypes = [("Python File", "*.py"), ("C++ File", "*.cpp"), ("Java File", "*.java"), ("txt File", "*.txt")])
        with open(filepath, "w") as file:
            file.write(self.textbox.get(1.0, customtkinter.END))
        messagebox.showinfo("Saved!", "File Saved successfully")
      
# class myFunctions(customtkinter.CTk()):
#     def __init__(self):
#         super.__init__()
#         self.btn = customtkinter.CTkButton(self,command= App.saveFile(self))
#         self.btn.grid(row = 10, column = 1, sticky = "nsew")
app = App()
app.mainloop()



# class myApp(customtkinter.CTk()):
#     def __init__(self):
#         super.__init__()
#         self.grid_rowconfigure(0, weight = 1)
#         self.grid_columnconfigure(0, weight = 1)
#         self.title("Dark")
#         self.minsize(1280,840)
        # self.headerf = customtkinter.CTkFrame(master=self, width=1280, height=40, bg_color="black")
        # self.headerf.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "nsew")
        # self.filesop = customtkinter.CTkOptionMenu(master= self.headerf)
        # self.filesop.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "ew")
        # self.appbtn = customtkinter.CTkButton(master = self, text="Save", command= self.saveFile())
        # self.appbtn.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "ew")
        # self.textf = customtkinter.CTkFrame(master = self, width= 800, height = 401, bg_color="#000712")
        # self.textf.grid(row = 1, column = 0, padx = 1, pady = 1)
        # self.txtbox = customtkinter.CTkTextbox(self, width=1280, height=840)
        # self.txtbox.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "nsew")
        # txtbox.insert("0.0", file)
        # appoptions = customtkinter.CTkOptionMenu( appframe, appbtn)
#     def saveFile(self):
#         self.txtbox = customtkinter.CTkTextbox(self, width=1280, height=840)
#         self.txtbox.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = "nsew")
#         filetypes = (
#         ("Python File", "*.py"),
#         ("C++ File", "*.cpp"),
#         ("Java File", "*.java"),
#         ("Plaintext File", "*.txt")
#         )
    
#         files = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension= "*.py", filetypes=filetypes)
#         with open(files, "w") as file:
#             text = self.txtbox.read()
#             file.write(text)

# app = myApp()
# app.mainloop()


