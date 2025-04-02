import os
import re
import subprocess

def apostrof(text):
    # Pola untuk mencari apostrof apapun diikuti dengan huruf kapital (baik 'S, ’S, atau ‘S)
    text = re.sub(r"([’‘'\"])S", r"\1s", text)
    text = re.sub(r"([’‘'\"])T", r"\1t", text)
    return text

def rename_miyuki(folder_path = "./movies_folder_miyuki", dest_folder = "./Download MissAV"):
    if not os.path.exists(folder_path):
        return
    
    dest_video = os.path.join(dest_folder, "Video")
    dest_cover = os.path.join(dest_folder, "Cover")
    if not os.path.exists(dest_video):
        os.makedirs(dest_video)
    if not os.path.exists(dest_cover):
        os.makedirs(dest_cover)

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            file_path = os.path.join(folder_path, filename)

            # Pisahkan kode dan shortname
            name, ext = os.path.splitext(filename)
            kode = name.split(" ")[0]
            shortname = " ".join(name.split(" ")[1:]).rsplit(".", 1)[0]

            # Buat nama baru
            new_name = f"{kode.upper().replace('_1080P','').replace('_720P','').replace('_480P','').replace('_360P','')} {apostrof(shortname.replace('&quot;', '').title())}"
            new_name = new_name.strip() + ".mp4"
            new_path = os.path.join(dest_video, new_name.replace("..", ".").replace(" .MP4 .mp4", ".mp4"))

            # Rename file
            os.rename(file_path, new_path)
            print(f"Renamed '{filename}' to '{new_name}'")

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            file_path = os.path.join(folder_path, filename)
            if os.path.splitext(os.path.basename(new_path))[0] in filename.upper():

                # Buat nama baru
                new_name = new_name.replace(".mp4", " Cover.jpg")
                new_path = os.path.join(dest_cover, new_name)

                # Rename file
                os.rename(file_path, new_path)
                print(f"Renamed '{filename}' to '{new_name}'")

def search(string, path="."):
    hasil = []
    output = ""
    
    for root, dirs, files in os.walk(path):
        # Cek folder yang mengandung string
        for dir_name in dirs:
            if string.lower() in dir_name.lower():
                hasil.append(os.path.join(root, dir_name))
        
        # Cek file yang mengandung string
        for file_name in files:
            if string.lower() in file_name.lower():
                hasil.append(os.path.join(root, file_name))
    
    # Menampilkan hasil pencarian
    if hasil:
        output += "\nHasil Pencarian:"
        for i, item in enumerate(hasil, 1):
            output += f"\n{i}. {item}"
    else:
        output += "Tidak ada hasil ditemukan."

    return output

def search_jav(path="."):
    video_files = []
    image_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".mp4"):
                video_files.append(os.path.join(root, file))  # Simpan path lengkap
            elif file.lower().endswith(".jpg"):
                image_files.append(os.path.join(root, file))

    return video_files, image_files

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            return result.stdout  # Kembalikan output jika ada
        # Jika output kosong, lempar error
        raise RuntimeError("Perintah tidak menghasilkan output!")
    except Exception as e:
        return search(command)
    
def install_miyuki():
    try:
        import miyuki
        return "Miyuki is already installed."
    except ImportError:
        command = "pip install miyuki-0.7.7-py3-none-any.whl"
        return run_command(command)