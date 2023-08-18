import customtkinter as ctk

class GUI:
    def __init__(self, root):
        colors = {"veryDark":"#0D0630",
                  "dark":"#18314F",
                  "middle":"#384E77",
                  "light":"#38AECC",
                  "veryLight":"#5ADBFF"}
        self.root = root
        self.root.title("API Finder")
        self.root.geometry("800x550")
        # self.root._set_appearance_mode("Dark")
        self.root.configure(bg="blue")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        #User Input Frame init
        self.userInputFrame = ctk.CTkFrame(self.root, fg_color=colors["dark"])
        self.userInputFrame.grid(row=0, column=1, sticky='nsew')
        self.userInputFrame.grid_columnconfigure(0, weight=1)
        self.input = ctk.CTkEntry(self.userInputFrame, placeholder_text="Tell us what API you're looking for...")
        self.input.grid(row=2, column=0, sticky='ew')
