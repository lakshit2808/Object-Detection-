import cv2 , time
import pandas
from datetime import datetime

video = cv2.VideoCapture(0)
status_data = [None , None]
time_data = []
df = pandas.DataFrame(columns=["Start" , "END"])

first_frame = None
while True:
    #x =+ 1
    status = 0
    ret , frame  = video.read()
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # this will show the gray screen
    blur_frame = cv2.GaussianBlur(gray_frame , (21,21) , 0) # this will blur the image
    #print(check)
    #print(frame)
    if first_frame is None:
        first_frame = gray_frame
        continue

    diff_bwt_frame = cv2.absdiff(first_frame , gray_frame) # this will give the diff b/t 2 frame
    thresh_diff = cv2.threshold(diff_bwt_frame , 20 ,255, cv2.THRESH_BINARY)[1] # this will make the obj white
    thresh_diff = cv2.dilate(thresh_diff , None , iterations= 2) # it'll make obj more smooth

    (cnts, _) = cv2.findContours(thresh_diff.copy() ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE ) # this will find the moving obj

    for countor in cnts:
        if cv2.contourArea(countor) < 5000: # this loop will capture the obj who is < 10000 pixel
            continue
        (x ,y , w ,h) = cv2.boundingRect(countor)
        cv2.rectangle(frame , (x ,y)  , (x+w , y+h) , (0,255,0) ,5)
        status = 1

    #time.sleep(.0000001)

    print(status)

for i in range(0,len(time_data) , 2):
    df= df.append({"Start" : time_data[i] , "END" : time_data[i+1] } , ignore_index=True)
#print(x)
df.to_csv("time.csv")
video.release()

cv2.destroyAllWindows()