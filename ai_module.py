import cohere
import PyPDF2
from CTkMessagebox import CTkMessagebox


def run_ai(input, length, root):
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
    except:
        CTkMessagebox(master=root, title="Error", message="You must submit at least 250 characters and can only make 5 summaries/min. ", icon="cancel", width=400, height=50, button_width=180, button_height=100, topmost=False)
