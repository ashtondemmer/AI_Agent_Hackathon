import PyPDF2

def convert_to_text(input_path):
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