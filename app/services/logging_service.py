import os
from  datetime import datetime

def log(tag="", message=""):
    path="app/logs/log.txt"
    directory= os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path,"a") as log:
        log.write(f'{{"time":"{datetime.now()}","tag":"{tag}","message":"{message}"}}\n')