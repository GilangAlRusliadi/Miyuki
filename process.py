import os
import uuid
import json
import time
import subprocess

static_dir = os.path.join(os.getcwd(), "static")
queue_file = os.path.join(os.getcwd(), "download_queue.json")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

def load_queue():
    if os.path.exists(queue_file):
        with open(queue_file, "r") as f:
            return json.load(f)
    return {}

def save_queue(queue):
    with open(queue_file, "w") as f:
        json.dump(queue, f)

def download_file(video_url_input, quality):
    movie_id = video_url_input.split("/")[-1]
    log_id = uuid.uuid4()
    log_file_path = os.path.join(static_dir, f"{log_id}.log")
    command = f"miyuki -ffmpeg -auto {video_url_input} -quality {quality} -cover"
    
    with open(log_file_path, "w") as log_file:
        subprocess.Popen(
            command, stdout=log_file, stderr=log_file, text=True, shell=True
        )
    
    log_link = f"./static/{log_id}.log"
    return "Downloading", log_link

def check_task_status(url, log_link):
    if not log_link:
        return "Not Started", ""
    
    log_file = log_link.split("/static/")[-1]
    log_path = os.path.join(static_dir, log_file)
    
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            content = f.read()
            movie_id = url.split("/")[-1]
            
            if f"File integrity for {movie_id}: 100.00%" in content:
                return "Success", log_link
            elif "Failed to fetch HTML for" in content:
                return "Failed", log_link
    
    return "Downloading", log_link

def clean_log_files():
    queue = load_queue()
    urls_to_remove = []
    
    for url, task in queue.items():
        if task["Status"] in ["Success", "Failed"]:
            if task["Log"]:
                log_file = task["Log"].split("/static/")[-1]
                log_path = os.path.join(static_dir, log_file)
                if os.path.exists(log_path):
                    os.remove(log_path)
            urls_to_remove.append(url)
    
    for url in urls_to_remove:
        del queue[url]
    
    save_queue(queue)
    
    for filename in ["downloaded_urls_miyuki.txt", "ffmpeg_input_miyuki.txt", "tmp_movie_miyuki.html", "miyuki.log"]:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
