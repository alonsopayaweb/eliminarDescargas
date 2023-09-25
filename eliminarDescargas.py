import os, shutil
 
user = os.getlogin()
dir = 'C:/Users/' + user + '/Downloads'

for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)