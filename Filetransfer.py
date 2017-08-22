import datetime
import os
import shutil


def move_files(source, destination):
    
    now = datetime.datetime.now()
    past = now - datetime.timedelta(hours=24)
    print('The following .txt files were modified in the past 24 hour period: \n')

    for files in os.listdir(source):
        if files.endswith('.txt'):
            path = os.path.join(source, files)
            st = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)

        if mtime > past:
            print('{} ~ last modified {}'.format(path, mtime))
            file_source = os.path.join(source, files)
            file_destination = os.path.join(destination, files)
            shutil.move(file_source, file_destination)
            print("\tMoved {} to {}.\n".format(files, destination))
