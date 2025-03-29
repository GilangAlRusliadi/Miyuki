import subprocess
import gradio as gr
from process import *
from extra import *

try:
    import miyuki
    print("Miyuki is already installed.")
except ImportError:
    subprocess(f"pip install miyuki-0.7.7.tar.gz", shell=True)

# Load existing queue
download_queue = load_queue()

def add_to_queue(video_url, quality):
    if not video_url.startswith("http"):
        return "Error: Please enter a valid URL."
    
    if video_url in download_queue:
        return "Warning: This URL is already in the queue."
    
    download_queue[video_url] = {
        "URL": video_url,
        "Status": "Not Started",
        "Log": ""
    }
    save_queue(download_queue)
    return f"Added {video_url} to the queue."

def start_download():
    for url, task in download_queue.items():
        if task["Status"] == "Not Started":
            status, log = download_file(url, "720")
            download_queue[url]["Status"] = status
            download_queue[url]["Log"] = log
            save_queue(download_queue)
    return "Downloads started."

def view_queue():
    return [(url, data["Status"]) for url, data in download_queue.items()]

def check_status():
    for url, task in download_queue.items():
        if task["Status"] in ["Downloading", "Not Started"]:
            status, log = check_task_status(url, task["Log"])
            download_queue[url]["Status"] = status
            download_queue[url]["Log"] = log
            save_queue(download_queue)
    return "Queue status updated."

with gr.Blocks() as app:
    gr.Markdown("# Miyuki GUI Downloader")
    
    with gr.Row():
        video_url = gr.Textbox(label="Video URL")
        quality = gr.Dropdown(["360", "480", "720"], label="Quality", value="360")
        add_button = gr.Button("Add to Queue")
    
    add_button.click(add_to_queue, inputs=[video_url, quality], outputs=None)
    
    start_button = gr.Button("Start Download")
    start_button.click(start_download, outputs=None)
    
    check_button = gr.Button("Check Status")
    check_button.click(check_status, outputs=None)
    
    queue_list = gr.Dataframe(headers=["URL", "Status"], datatype=["str", "str"], label="Download Queue")
    view_button = gr.Button("View Queue")
    view_button.click(view_queue, outputs=queue_list)

app.launch()
