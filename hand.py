import cv2
import mediapipe as mp
import serial
import socket

#ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

cap = cv2.VideoCapture(0)
hand_mp = mp.solutions.hands
draw_mp = mp.solutions.drawing_utils
with hand_mp.Hands(static_image_mode = False, max_num_hands = 1, min_detection_confidence =0.6, min_tracking_confidence = 0.8) as hand:
    while True:
        check, frame = cap.read()
        if not check:
            print("Camera Not Found")
        frame_2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_2 = hand.process(frame_2)
        if result_2.multi_hand_landmarks:
            for hand_landmark in result_2.multi_hand_landmarks:
                draw_mp.draw_landmarks(frame, hand_landmark, hand_mp.HAND_CONNECTIONS)
# Middle And Thumb Finger touching
                ls1 = result_2.multi_hand_landmarks[0].landmark[12]
                ls2 = result_2.multi_hand_landmarks[0].landmark[4]
                x1 = ls1.x
                y1 = ls1.y
                x2 = ls2.x
                y2 = ls2.y
                
                z1 = ((ls1.z)**2)*100000
                z2 = ((ls2.z)**2)*100000

                x = (x2 -x1)**2
                y = (y2 -y1)**2
                dist = (x+y)**0.5
                sqz = (z2-z1)**2
                depth_calc = round(sqz**0.5)
                #print(depth_calc) #This is for Debugging
                if dist < 0.1 and depth_calc < 500 and depth_calc >2:
                    #ser.write(b"on\n")
                    #print("Finger's Touching") #This is for Debugging
                    socket_laptop.send(b'on\n')
                #ser.write(b"off\n")
                else:
                    socket_laptop.send(b'off\n')
        cv2.imshow("Camera", frame)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
#ser.close()
cap.release()
cv2.destroyAllWindows()
socket_laptop.close()
