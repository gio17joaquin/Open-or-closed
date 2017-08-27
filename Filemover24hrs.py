from datetime import *
import os.path
import shutil

source = 'C:/Users/Student/Desktop/FolderA'
destination = 'C:/Users/Student/Desktop/FolderB'
files = os.listdir(source)
current = datetime.now()


def moveFiles(file_list):
    for each in file_list:
        if each.endswith('.txt'):
            mtime = os.path.getmtime(source + '/' + each)
            date = datetime.fromtimestamp(mtime)

        if date > (current-timedelta(1)) and each.endswith('.txt'):
            shutil.move(source + '/' + each, destination)
            print("\tMoved {}, to {}.\n".format(each, destination))


moveFiles(files)
