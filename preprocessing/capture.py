from datetime import datetime
from time import sleep

import imutils
import mediapipe as mp
import cv2
import csv
import os
import numpy as np

path = "captures"
file_base = path + "/squats_back_1010"
file = file_base + "_3d.csv"
file_2 = file_base + "_2d.csv"

is_upper = False

num_coords = 33
if is_upper:
    num_coords = 25

header = []
for ind in range(1, num_coords + 1):
    header += ["x{}".format(ind), "y{}".format(ind), "z{}".format(ind), "v{}".format(ind)]

header_2 = []
for ind in range(1, num_coords + 1):
    header_2 += ["x{}".format(ind), "y{}".format(ind)]

with open(file, mode='w', newline="") as out:
    csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(header)
with open(file_2, mode='w', newline="") as out:
    csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(header_2)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    joints = []
    cap = cv2.VideoCapture(0)
    counter = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = imutils.resize(image, height=480)
        image = imutils.resize(image, width=640)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

        try:
            landmarks = results.pose_landmarks.landmark
            if is_upper:
                landmarks = landmarks[:25]

            row = list(np.array(
                [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in landmarks]).flatten())
            row_2 = list(np.array(
                [[landmark.x, landmark.y] for landmark in landmarks]).flatten())

            with open(file, mode='a', newline="") as out:
                csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(row)
            with open(file_2, mode='a', newline="") as out:
                csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(row_2)
        except:
            pass

        cv2.imshow("Video", image)
        counter += 1
        if cv2.waitKey(10) & 0xFF == ord('q') or counter == 500:
            break
