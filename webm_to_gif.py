import os
from moviepy.editor import VideoFileClip

for file in os.listdir(os.getcwd()):
    if file.endswith(".webm"):
        print(f'Converting {file}')
        try:
            video = VideoFileClip(file)
            new_file_name = f"{file.split('.webm')[0]}.gif"
            video.write_gif(new_file_name)
            print(f'Successfully converted {file} to {new_file_name}\n')
        except Exception as e:
            print(f'Error converting {file}: {e}')
input('Process finished, press enter to exit')
