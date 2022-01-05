import cv2
import vlc
import time

cap = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        cv2.namedWindow("test")
        image_counter = 0
        while True:
            image, image_frame = cap.read()
            if not image:
                print('failed to capture image')
                break
            cv2.imshow('test capture', image_frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
        # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                image_name = "opencv_frame_{}.png".format(image_counter)
                cv2.imwrite(image_name, image_frame)
                print("{} written!".format(image_name))
                image_counter += 1
cap.release()
cv2.destroyAllWindows()
