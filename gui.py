import customtkinter as ctk

class GUI:
    def __init__(self, root):
        colors = {"black":"#000000",
                  "darkGray":"#141414",
                  "lightGray":"#282828",
                  "darkPurple":"#230046",
                  "lightPurple":"#320064"}
        self.root = root
        self.root.title("API Finder")
        self.root.geometry("800x550")
        self.root._set_appearance_mode("Dark")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        #User Input Frame init
        self.userInputFrame = ctk.CTkFrame(self.root, fg_color=colors["darkGray"])
        self.userInputFrame.grid(row=0, column=1, sticky='nsew')
        self.userInputFrame.grid_rowconfigure(1, weight=1)
        self.header = ctk.CTkLabel(self.userInputFrame, text="API Search Tool - Powered by AI", font=('Open Sans', 26))
        self.header.grid(row=0, columnspan=2, column=0)
        self.bodyFrame = ctk.CTkFrame(self.userInputFrame, fg_color=colors["darkGray"])
        self.bodyFrame.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.userInputFrame.grid_columnconfigure(0, weight=9)
        self.userInputFrame.grid_columnconfigure(1, weight=1)
        self.input = ctk.CTkEntry(self.userInputFrame, placeholder_text="Tell us what API you're looking for...", height=50)
        self.input.grid(row=2, column=0, sticky='ew')
        self.askBtn = ctk.CTkButton(self.userInputFrame, text=">", width=5, height=50, fg_color=colors["lightPurple"], font=('Open Sans', 18))
        self.askBtn.grid(row=2, column=1, sticky='ew')

        #Suggestions Frame
        suggestionTexts = [
            "Show me all the APIs that are related to animal images.",
            "Return a list of weather APIs that I can use in my new project.",
            "Recommend some APIs for language translation.",
            "Can you suggest some APIs for data visualization?"
        ]
        self.suggestionFrame = ctk.CTkFrame(self.bodyFrame)
        self.suggestionFrame.pack(side="bottom", pady=25)
        self.suggestionHeader = ctk.CTkLabel(self.suggestionFrame, text="Try some of these messages:")
        self.suggestionHeader.grid(row=0, column=0, columnspan=2)
        for index, text in enumerate(suggestionTexts):
            row = (index // 2) +1
            column = index % 2
            subFrame = ctk.CTkFrame(self.suggestionFrame)
            subFrame.grid(row=row, column=column, padx=5, pady=5)
            label = ctk.CTkLabel(subFrame, text=text, font=("Arial", 14), height=50, width=20, wraplength=250)
            label.pack(padx=5, pady=5)

