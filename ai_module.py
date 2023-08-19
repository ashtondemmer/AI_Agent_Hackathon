import cohere

def run_ai(input, length='medium'):
    api_key = "DWj2W2Xrp138tVMderoQAiVBxV3ZywVMj2XXgUh1"
    co = cohere.Client(api_key)
    
    response = co.summarize(
        text=input,
        model='command',
        length=length,
        extractiveness='medium'
    )
    output = response.summary
    return output