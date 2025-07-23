import os
import shutil
import logging

logging.basicConfig(filename='organizer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

audio_ext = (".mp3", ".wav", ".flac")
video_ext = (".mp4", ".mov", ".mkv")
image_ext = (".jpg", ".jpeg", ".png", ".gif", ".svg")
doc_ext = (".pdf", ".docx", ".txt", ".xlsx")

def move_file(file, folder):
    try:
        os.makedirs(folder, exist_ok=True)
        shutil.move(file, folder)
        logging.info(f"Moved: {file} → {folder}")
    except Exception as e:
        logging.error(f"Failed to move {file}: {e}")

source = r"C:\Users\STALIN\OneDrive\Desktop\Stalin_edits"
os.chdir(source)

for file in os.listdir():
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1].lower()
        if ext in audio_ext:
            move_file(file, os.path.join(source, "audio"))
        elif ext in video_ext:
            move_file(file, os.path.join(source, "video"))
        elif ext in image_ext:
            if "screenshot" in file.lower():
                move_file(file, os.path.join(source, "screenshots"))
            else:
                move_file(file, os.path.join(source, "images"))
        elif ext in doc_ext:
            move_file(file, os.path.join(source, "documents"))
        else:
            move_file(file, os.path.join(source, "others"))
