import shutil
import os

sourcepath = 'C:/Users/Student/Desktop/FolderA'
source = os.listdir(sourcepath)
dest = 'C:/Users/Student/Desktop/FolderB'


for f in source:
        if f.endswith('.txt'):
            shutil.move(os.path.join(sourcepath,f), os.path.join(dest,f))

print("\tMoved {} to {}.\n".format(f,dest))
    
