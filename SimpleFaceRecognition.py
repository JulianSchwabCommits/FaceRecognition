import cv2
import threading
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0 
face_match = False
face_found = False
reference_img = cv2.imread("G:\My Drive\Coding\FaceRecognitionPython\Julian1.jpg")
def check_face(frame):
    global face_match
    global face_found
    
    try:
        if DeepFace.verify(frame, reference_img.copy())["verified"]:
            face_match = True
            face_found = True
        else:
            face_match = False
            face_found = True
    except ValueError:
        face_match = False
        face_found = False


# Main Loop
while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30  == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            
            except ValueError:
                pass
        counter += 1

        if face_match and face_found:
            cv2.putText(frame,"Hi, Julian", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,255,0), 3)
        elif face_found and not face_match:
            cv2.putText(frame,"Face found no match!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,165,225), 3)     
        elif not face_found and not face_match:
            cv2.putText(frame,"Face not found!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 3)            

        cv2.imshow("Video",frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
