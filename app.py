"""
Gradio App
David Peng
20230621
"""
import base64
import gradio as gr
from download_pdf import download

examples = [
    "https://indianculture.gov.in/reports-proceedings/report-village-and-cottage-industries-national-committee-development-backward"
]

def try_download(url):
    try:
        pdf = download(url)
        return pdf
    except Exception as e:
        raise gr.Error(str(e))

with gr.Blocks() as app:
    gr.Markdown("# <p align='center'>Extract PDF from indianculture[dot]gov[dot]in</p>")
    # with gr.Row():
    #     with gr.Column():
    #         landing_page_url = gr.Textbox(label="Landing Page URL")
    #         landing_page_url_btrn = gr.Button(value="Extract PDF")
    #     with gr.Column():
    #         pdf_file = gr.File(label="PDF")
    landing_page_url = gr.Textbox(label="Landing Page URL")
    landing_page_url_btrn = gr.Button(value="Extract PDF")
    pdf_file = gr.File(label="PDF")
    gr.Examples(examples=examples,inputs=landing_page_url,outputs=pdf_file)

    landing_page_url_btrn.click(
        try_download,
        inputs=landing_page_url,
        outputs=pdf_file
    )
app.launch()
