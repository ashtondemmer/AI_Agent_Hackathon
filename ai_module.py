import cohere
import PyPDF2

def run_ai(input_path, length='medium'):
    api_key = "DWj2W2Xrp138tVMderoQAiVBxV3ZywVMj2XXgUh1"
    co = cohere.Client(api_key)

    file_contents = ''
    try:
        # refactor into a different function:
        with open(input_path, 'rb') as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file) 
            for page_number, page in enumerate(pdf.pages):
                page = pdf.pages[page_number]
                file_contents += page.extract_text()

        response = co.summarize(
            text=file_contents,
            model='command',
            length=length,
            extractiveness='medium'
        )
        return response.summary 
    except FileNotFoundError:
        return "File not found!"            
