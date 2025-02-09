# 1) Import Required Libraries 

import requests
import gradio as gr

# Deepseek only uses abstract summarization
# This tool use DeepSeek API Endpoint

# 2) Define the DeepSeek API Endpoint

OLLAMA_URL = "http://localhost:11434/api/generate"

# 3) Define the Summarization Function which can retrieve Information

def summarize_text(text):
    payload = {
        "model": "deepseek-r1", #Here you can load whatever the model you have in your ollama(ex:deepseek-r1:1.5b,7b,8b,14b) I used 7b model here 
        "prompt": f"Summarize the following text in **5 bullet points**:\n\n{text}", #The prompt is here for tell commands for the llm to act 
        "stream": False  # Ensures the response is returned as a whole, not streamed
    }

    response = requests.post(OLLAMA_URL, json=payload) #Send Requests to deepseekAPI

    if response.status_code == 200: #if server run correctly it return the result or it will give error
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"

# 4) Create Gradio interface to design 
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(label="Summarized Text"),
    #theme='NoCrypt/miku', #Theme for the Interface I used Hatsune Miku from HF 
    title="AI-Powered Text Summarizer",
    description="Enter a long text and DeepSeek AI will generate a concise summary."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()

 