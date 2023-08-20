import customtkinter as ctk
from customtkinter import filedialog
import ai_module
    

class GUI:
    def __init__(self, root):
        self.colors = {"black":"#000000",
                  "darkGray":"#141414",
                  "lightGray":"#282828",
                  "darkPurple":"#230046",
                  "lightPurple":"#320064"}
        self.root = root
        self.root.title("QuickRead")
        self.root.geometry("1100x650")
        self.root._set_appearance_mode("Dark")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        #Left Side
        self.left_frame = ctk.CTkFrame(self.root, fg_color=self.colors["darkGray"])
        self.left_frame.grid(row=0, column=0, sticky='nsew')
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.header = ctk.CTkLabel(self.left_frame, text="QuickRead", font=('Open Sans', 26))
        self.header.grid(row=0, columnspan=2, column=0, pady=10)
        self.summarized_text = ctk.CTkLabel(self.left_frame, text="Your summarized text will appear here.", font=('Open Sans', 14), wraplength=450, justify='left')
        self.summarized_text.grid(row=1, columnspan=2, column=0)
        # self.body_frame = ctk.CTkFrame(self.left_frame, fg_color=self.colors["darkGray"])
        # self.body_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.left_frame.grid_columnconfigure(0, weight=1)

            #Old txt input and submit button
        # self.pad_frame = ctk.CTkFrame(self.left_frame, bg_color=self.colors["darkGray"], fg_color=self.colors['darkGray'])
        # self.pad_frame.grid_columnconfigure(0, weight=1)
        # self.pad_frame.grid(row=3, column=0, sticky='ew', pady=15, padx=15)
        # self.entry = ctk.CTkEntry(self.pad_frame, placeholder_text="Tell us what API you're looking for...", height=50)
        # self.entry.grid(row=2, column=0, sticky='ew')
        # self.entry.bind("<Return>", self.input_to_output)
        # self.ask_button = ctk.CTkButton(self.pad_frame, command=self.input_to_output, text=">", width=60, height=50, fg_color=self.colors["lightPurple"], font=('Open Sans', 18))
        # self.ask_button.grid(row=2, column=1, sticky='ew')

        self.suggestionTexts = [
            "Paste long emails that take too much time to read.",
            "Copy over articles from the news that you never have enough time to read.",
            "Review topics from your school textbook before your next exam.",
            "Open files from your computer within QuickRead for easy summarization!"
        ]
        self.suggestion_frame = ctk.CTkFrame(self.left_frame)
        self.suggestion_frame.grid(row=2, column=0, pady=25)
        self.suggestion_header = ctk.CTkLabel(self.suggestion_frame, text="Some uses for QuickRead:")
        self.suggestion_header.grid(row=0, column=0, columnspan=2)
        for index, text in enumerate(self.suggestionTexts):
            row = (index // 2) +1
            column = index % 2
            sub_frame = ctk.CTkFrame(self.suggestion_frame)
            sub_frame.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
            label = ctk.CTkLabel(sub_frame, text=text, font=("Arial", 14), height=50, width=20, wraplength=250)
            label.pack(padx=5, pady=5)

        #Right Side
        self.left_frame.grid(row=0, column=0)
        self.right_frame = ctk.CTkFrame(self.root, fg_color=self.colors['lightGray'])
        self.right_frame.grid(row=0, column=1, sticky='nsew')

        #Suggestions Frame
        self.template_options = [
            "History of Rome",
            "The moon landing",
            "The invention of Programming"
        ]
        self.template_frame = ctk.CTkFrame(self.right_frame)
        self.template_frame.pack(side="top", pady=25)
        self.template_header = ctk.CTkLabel(self.template_frame, text="Try summarizing some of these articals:")
        self.template_header.grid(row=0, column=0, columnspan=3)
        for index, text in enumerate(self.template_options):
            column = index
            sub_frame = ctk.CTkFrame(self.template_frame)
            sub_frame.grid(row=1, column=column, padx=5, pady=5, sticky='nsew')
            label = ctk.CTkLabel(sub_frame, text=text, font=("Arial", 14), height=50, width=20, wraplength=175)
            label.pack(padx=5, pady=5)
            sub_frame.bind("<Button-1>", lambda event, idx=index+1: self.add_article(idx))
            label.bind("<Button-1>", lambda event, idx=index+1: self.add_article(idx))

        self.input_field = ctk.CTkTextbox(self.right_frame)
        self.input_field.insert("1.0", "Paste what you want to be summarized here...")
        self.input_field.pack(fill="both", expand=True, padx=15)
        
        self.btn_frame = ctk.CTkFrame(self.right_frame)
        self.btn_frame.pack(side='bottom', pady=15)
        self.summarize_btn = ctk.CTkButton(self.btn_frame, text="Summarize", command=self.summarize)
        self.summarize_btn.grid(row=0, column=0, padx=15)
        self.upload_file_button = ctk.CTkButton(self.btn_frame, text="Upload File", command=self.upload_file)
        self.upload_file_button.grid(row=0, column=1, padx=15)

    def add_article(self, file_number):
        print(file_number)
        with open(f"example_text/example{file_number}.txt", "r", encoding="utf-8") as file:
            content = file.read()
            self.input_field.delete("1.0", "end")
            self.input_field.insert("1.0", content)
    # def example_1(self):
    #     self.add_article(1)
    # def example_2(self):
    #     self.add_article(2)
    # def example_3(self):
    #     self.add_article(3)

    def summarize(self, event=None):
        input = self.input_field.get("1.0", "end-1c")
        self.response = ai_module.run_ai(input)
        self.summarized_text.configure(text=self.response)

    def upload_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.configure(text=f"Selected File: {file_path}")
    




