import PyPDF2

def convert_to_text(input_path):
    split_path = [character for character in input_path]
    if ((split_path[len(split_path) - 3] + split_path[len(split_path) - 2] + split_path[len(split_path) - 1]).upper() == 'PDF'):
        file_contents = ''
        try:
            # refactor into a different function:
            with open(input_path, 'rb') as pdf_file:
                pdf = PyPDF2.PdfReader(pdf_file) 
                for page_number, page in enumerate(pdf.pages):
                    page = pdf.pages[page_number]
                    file_contents += page.extract_text()
            return file_contents
        except FileNotFoundError:
            return "ENOENT"
    else:
        with open(input_path, 'r') as txt_file:
            return txt_file.read()