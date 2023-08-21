import cohere
import PyPDF2

def run_ai(input, length):
    length = length.split()[0].lower()
    
    api_key = "DWj2W2Xrp138tVMderoQAiVBxV3ZywVMj2XXgUh1"
    co = cohere.Client(api_key)

    try:
        response = co.summarize(
            text=input,
            model='command',
            length=length,
            extractiveness='medium'
        )
        return response.summary 
    except FileNotFoundError:
        return "There was an error..."