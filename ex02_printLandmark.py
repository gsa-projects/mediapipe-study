import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

for lm in mp_pose.PoseLandmark:
    print(lm.name)

# 출력 결과
# PoseLandmark.NOSE
# PoseLandmark.LEFT_EYE_INNER
# PoseLandmark.LEFT_EYE
# PoseLandmark.LEFT_EYE_OUTER
# PoseLandmark.RIGHT_EYE_INNER
# PoseLandmark.RIGHT_EYE
# PoseLandmark.RIGHT_EYE_OUTER
# PoseLandmark.LEFT_EAR
# PoseLandmark.RIGHT_EAR
# PoseLandmark.MOUTH_LEFT
# PoseLandmark.MOUTH_RIGHT
# PoseLandmark.LEFT_SHOULDER
# PoseLandmark.RIGHT_SHOULDER
# PoseLandmark.LEFT_ELBOW
# PoseLandmark.RIGHT_ELBOW
# PoseLandmark.LEFT_WRIST
# PoseLandmark.RIGHT_WRIST
# PoseLandmark.LEFT_PINKY
# PoseLandmark.RIGHT_PINKY
# PoseLandmark.LEFT_INDEX
# PoseLandmark.RIGHT_INDEX
# PoseLandmark.LEFT_THUMB
# PoseLandmark.RIGHT_THUMB
# PoseLandmark.LEFT_HIP
# PoseLandmark.RIGHT_HIP
# PoseLandmark.LEFT_KNEE
# PoseLandmark.RIGHT_KNEE
# PoseLandmark.LEFT_ANKLE
# PoseLandmark.RIGHT_ANKLE
# PoseLandmark.LEFT_HEEL
# PoseLandmark.RIGHT_HEEL
# PoseLandmark.LEFT_FOOT_INDEX
# PoseLandmark.RIGHT_FOOT_INDEX
