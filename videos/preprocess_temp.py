import os
import shutil
import glob
import srt2txt
import update_videos_temp

filenames = glob.glob('./temp/*.mp4')

for i in filenames:
    filename = i[:-4]
    srt2txt.convert_srt2txt(filename)
    os.system('ffmpeg -threads 2 -v 0 -i '+filename+'.mp4 '+filename+'.mp3')

os.system('mv ./temp/* ./source_temp/')
update_videos_temp.update_videos()
