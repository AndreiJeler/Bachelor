import imutils
import mediapipe as mp
import cv2
import csv
import os
import numpy as np

path_root = "squats"

rootpath = path_root + "/correctness/videos"
dataset_path = path_root + "/correctness/dataset"

file_full = path_root + "/correctness/dataset/full/squats_full"
file_full_2d = path_root + "/correctness/dataset/full/squats_full_2d"

num_coords = 33

header = []
for ind in range(1, num_coords + 1):
    header += ["x{}".format(ind), "y{}".format(ind), "z{}".format(ind), "v{}".format(ind)]

header_2 = []
for ind in range(1, num_coords + 1):
    header_2 += ["x{}".format(ind), "y{}".format(ind)]

header_full = header + ["class"]
header_full_2d = header_2 + ["class"]

classes = os.listdir(rootpath)

for class_name in classes:
    print(class_name)
    class_path = rootpath + "/" + class_name
    files = [class_path + "/" + f for f in os.listdir(class_path) if os.path.isfile(class_path + '/' + f)]
    class_full_dataset = file_full + "_" + class_name + ".csv"
    class_full_dataset_2d = file_full_2d + "_" + class_name + ".csv"

    with open(class_full_dataset, mode='w', newline="") as out:
        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header_full)

    with open(class_full_dataset_2d + "_" + class_name + ".csv", mode='w', newline="") as out:
        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header_full_2d)

    i = 100
    for f in files:
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        print(f)

        file = dataset_path + "/partial/3d/" + class_name + "_" + str(i) + ".csv"
        file_2 = dataset_path + "/partial/2d/" + class_name + "_" + str(i) + "_2.csv"

        with open(file, mode='w', newline="") as out:
            csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(header)
        with open(file_2, mode='w', newline="") as out:
            csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(header_2)

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
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # landmarks = landmarks[:25]

                    row = list(np.array(
                        [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in
                         landmarks]).flatten())
                    row_2 = list(np.array(
                        [[landmark.x, landmark.y] for landmark in landmarks]).flatten())

                    with open(file, mode='a', newline="") as out:
                        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(row)
                    with open(file_2, mode='a', newline="") as out:
                        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(row_2)

                    with open(class_full_dataset, mode='a', newline="") as out:
                        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(row)
                    with open(class_full_dataset_2d, mode='a', newline="") as out:
                        csv_writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(row_2)

                except:
                    pass

                #cv2.imshow("Video", image)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            i += 1
