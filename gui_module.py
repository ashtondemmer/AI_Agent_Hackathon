import customtkinter as ctk
import ai_module
    

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
        self.user_input_frame = ctk.CTkFrame(self.root, fg_color=colors["darkGray"])
        self.user_input_frame.grid(row=0, column=1, sticky='nsew')
        self.user_input_frame.grid_rowconfigure(1, weight=1)
        self.header = ctk.CTkLabel(self.user_input_frame, text="API Search Tool - Powered by AI", font=('Open Sans', 26))
        self.header.grid(row=0, columnspan=2, column=0, pady=10)
        self.body_frame = ctk.CTkFrame(self.user_input_frame, fg_color=colors["darkGray"])
        self.body_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.user_input_frame.grid_columnconfigure(0, weight=1)
        self.pad_frame = ctk.CTkFrame(self.user_input_frame, bg_color=colors["darkGray"], fg_color=colors['darkGray'])
        self.pad_frame.grid_columnconfigure(0, weight=1)
        self.pad_frame.grid(row=2, column=0, sticky='ew', pady=15, padx=15)
        self.entry = ctk.CTkEntry(self.pad_frame, placeholder_text="Tell us what API you're looking for...", height=50)
        self.entry.grid(row=2, column=0, sticky='ew')
        self.entry.bind("<Return>", self.input_to_output)
        self.ask_button = ctk.CTkButton(self.pad_frame, command=self.input_to_output, text=">", width=60, height=50, fg_color=colors["lightPurple"], font=('Open Sans', 18))
        self.ask_button.grid(row=2, column=1, sticky='ew')


        #Suggestions Frame
        suggestionTexts = [
            "Show me all the APIs that are related to animal images.",
            "Return a list of weather APIs that I can use in my new project.",
            "Recommend some APIs for language translation.",
            "Can you suggest some APIs for data visualization?"
        ]
        self.suggestion_frame = ctk.CTkFrame(self.body_frame)
        self.suggestion_frame.pack(side="bottom", pady=25)
        self.suggestion_header = ctk.CTkLabel(self.suggestion_frame, text="Try some of these messages:")
        self.suggestion_header.grid(row=0, column=0, columnspan=2)
        for index, text in enumerate(suggestionTexts):
            row = (index // 2) +1
            column = index % 2
            sub_frame = ctk.CTkFrame(self.suggestion_frame)
            sub_frame.grid(row=row, column=column, padx=5, pady=5)
            label = ctk.CTkLabel(sub_frame, text=text, font=("Arial", 14), height=50, width=20, wraplength=250)
            label.pack(padx=5, pady=5)

    def input_to_output(self, event=None):
        input = self.entry.get()
        self.entry.delete(0, ctk.END)
        output = ai_module.run_ai(input)