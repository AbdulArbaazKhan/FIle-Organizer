import os


def creat_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def moving(file_type, folder):
    for move_files in file_type:
        creat_if_not_exists(folder)
        os.replace(move_files, f"{folder}/{move_files}")


if __name__ == '__main__':
    files = os.listdir()
    files.remove("files_organizer.py")
    image_Exts = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in image_Exts]
    zip_Exts = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"]
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zip_Exts]
    doc_Exts = [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in doc_Exts]
    exe_Exts = [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".wsf", ]
    executables = [file for file in files if os.path.splitext(file)[1].lower() in exe_Exts]
    audio_Exts = [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"]
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audio_Exts]
    prog_Exts = [".c", ".class", ".cpp", ".cs", ".h", ".java", ".pl", ".sh", ".swift", ".vb"]
    programming = [file for file in files if os.path.splitext(file)[1].lower() in prog_Exts]
    media_Exts = [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv", ".webm"]
    videos = [file for file in files if os.path.splitext(file)[1].lower() in media_Exts]
    html_Exts = [".html", ".mhtml", ".xmls", "php"]
    html_pages = [file for file in files if os.path.splitext(file)[1].lower() in html_Exts]
    others = [other for other in files if (
    os.path.splitext(other)[1].lower() not in image_Exts, zip_Exts, audio_Exts, media_Exts, prog_Exts, exe_Exts,
    doc_Exts) and os.path.isfile(other)]
    moving(images, "Images")
    moving(documents, "Documents")
    moving(zips, "Zips")
    moving(executables, "Exe")
    moving(audios, "Audios")
    moving(videos, "Videos")
    moving(html_pages, "Html")
    moving(others, "Others")
