
import cv2, time

video=cv2.VideoCapture(0)

first_frame=None

while True:
    
    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #GaussianBlur removes noise and improve accuracy. 
    #This method takes the parameter of the image, width and size of gaussian kernel(tuple) and sd
    
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    #time.sleep(3)


    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)

    #threshold method expects the image,limits and another threshold method
    thresh_frame=cv2.threshold(delta_frame,65,255,cv2.THRESH_BINARY)[1]

    #to smooth threshold frame, dilate library of cv2 is used ###sophisticated
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)


    cv2.imshow("Grey Frame",gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("thresh_delta",thresh_frame)
    cv2.imshow("Color Frame" , frame)



    key=cv2.waitKey(1)
    print(gray)

    if key==ord('q'):
        break



video.release()
cv2.destroyAllWindows()
