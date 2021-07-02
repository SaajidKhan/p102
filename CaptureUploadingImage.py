import cv2
import dropbox 
import time
import random

start_time=time.time()
def take_snapshot():
    num=random.randint(0,101)
    videoCaptureObject=cv2.VideoCapture(0)
    res=True
    while(res):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(num)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        res=False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='IveWSznJJhIAAAAAAAAAAVyy1xiFZvHMu2S75upc_wjy-7ILkuoI2FSh2YiY_PXz'
    file=img_name

    file_from=file
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File has uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()

