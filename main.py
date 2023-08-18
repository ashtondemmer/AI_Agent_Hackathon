import customtkinter as ctk
from gui_module import GUI


def main():
    root = ctk.CTk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()