import imutils
import mediapipe as mp
import cv2
import csv
import os
import numpy as np

rootpath = "squats/reps/images"

file = "squats/reps/dataset/squats.csv.csv"

num_coords = 33

landmarks = []
for ind in range(1, num_coords + 1):
    landmarks += ["x{}".format(ind), "y{}".format(ind), "z{}".format(ind), "v{}".format(ind)]
landmarks += ["class"]

classes = os.listdir(rootpath)
with open(file, mode='w', newline="") as out:
    csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

for class_name in classes:
    class_path = rootpath + "/" + class_name
    files = [class_path + "/" + f for f in os.listdir(class_path) if os.path.isfile(class_path + '/' + f)]
    for f in files:
        print(f)
        if f.split(".")[-1] == "mp4":
            mp_drawing = mp.solutions.drawing_utils
            mp_pose = mp.solutions.pose
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                cap = cv2.VideoCapture(f)
                joints = []
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
                                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                                                                     circle_radius=2),
                                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2,
                                                                     circle_radius=2))

                    # Extract landmarks
                    try:
                        landmarks = results.pose_landmarks.landmark
                        if num_coords == 25:
                            landmarks = landmarks[:25]
                        row = list(np.array(
                            [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in
                             landmarks]).flatten())
                        row += [class_name]

                        with open(file, mode='a', newline="") as out:
                            csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            csv_writer.writerow(row)

                    except:
                        pass

                    # cv2.imshow("Video", image)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
            continue
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            frame = cv2.imread(f, 0)

            # Recolor image to RGB
            try:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except Exception as ex:
                cap = cv2.VideoCapture(f)
                success, image = cap.read()
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
                if num_coords==25:
                    landmarks = landmarks[:25]
                row = list(np.array(
                    [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in landmarks]).flatten())
                row += [class_name]

                with open(file, mode='a', newline="") as out:
                    csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row)

            except:
                pass

            # cv2.imshow('image', image)
