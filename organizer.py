# Listing, moving and organizing all files available in a folder according to their type
# 4 possibilities: Executables (exe,bat), Images/Videos (jpg,mov), Documents (pdf,docx) and Other
from pathlib import Path
import sys

def path_finder():
    while True:
        raw=input("Paste the folder path here: ").strip().strip("'").strip('"') # ask for the folder to orgnaize and clean it
        pathway=Path(raw) # allows to have the folder formated to a path
        if not (pathway.is_dir()):
            print(f"{pathway} is not a valid folder. Please try again. ")
            continue
        match input(f"About to organize {pathway}. Continue ? (Y/n/quit) ").lower():
            case 'y':
                return pathway
            case 'quit':
                sys.exit("Operation cancelled")
            case _:
                continue

folder=path_finder() # to add to the global loop
    
file_types={
    # add any type/folder couple if needed
    # documents
    ".pdf":"Documents",
    ".docx":"Documents",
    ".xlsx":"Documents",
    ".pptx":"Documents",
    ".csv":"Documents",
    ".txt":"Documents",
    ".doc":"Documents",
    
    # medias
    ".jpeg":"Multimedia",
    ".jpg":"Multimedia",
    ".gif":"Multimedia",
    ".png":"Multimedia",
    ".svg":"Multimedia",
    ".mp4":"Multimedia",
    ".mov":"Multimedia",
    ".mkv":"Multimedia",
    ".mp3":"Multimedia",
    ".wav":"Multimedia",

    # executables and code-related
    ".exe":"Executables",
    ".bat":"Executables",
    ".py":"Executables",
    ".html":"Executables",
    ".css":"Executables",
    ".js":"Executables",
    ".c":"Executables",
    ".cpp":"Executables",
    ".json":"Executables",
    ".msi":"Executables",
    }

def folder_managing(folder):
    for file in folder:
        extension=file.suffix()
        destination=file_types.get(extension.lower(), "Other")
        if destination not in folder:   
            folder.mkdir()
            
""" if folder in FinalPath:
FinalPath[folder]=file"""
