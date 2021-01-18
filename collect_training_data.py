
import cv2
import os
import sys

label_name = input("Enter name : ")
num_samples = 200
img_save = 'training_data'
img_class = os.path.join(img_save, label_name)

try:
    os.mkdir(img_save)
except FileExistsError:
    pass
try:
    os.mkdir(img_class)
except FileExistsError:
    print("{} directory already exists.".format(img_class))
    print("All images gathered will be saved along with existing items in this folder")

cap = cv2.VideoCapture(0)

start = False
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    if count == num_samples:
        break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        roi = frame[100:500, 100:500]
        save_path = os.path.join(img_class, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
            (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('s'):
        start = not start

    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
