from app.core.tools import repeat_every
import os

def event_startup_create_folder():
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, 'statics')
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        list_file_folder = ['excel','mp3','video','images']
        for folder in list_file_folder:
            os.makedirs(os.path.join(new_folder_path, folder))

events = [v for k, v in locals().items() if k.startswith('event_startup_')]