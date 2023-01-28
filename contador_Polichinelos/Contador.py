import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture(0)
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence = 0.5, min_detection_confidence = 0.5) # Variável de detecção
draw = mp.solutions.drawing_utils # Esenha as linhas e pontos no vídeo
contador = 0
check = True

while(1):
    ret, img = video.read()

    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)  # Recebe o video e retorna o pontos
    points = results.pose_landmarks  # Extrai do video as coordenadas dos pontos
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape

    if points:
        # Foot
        peDY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)
        peDX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)
        peEY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y * h)
        peEX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x * w)

        # Hands
        moDY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * h)
        moDX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * w)
        moEY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * h)
        moEX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * w)

        # Distância dos pontos
        distMO = math.hypot(moDY - moEY, moDX - moEX)
        distPE = math.hypot(peDY - peEY, peDX - peEX)

        print(f'Mãos {distMO} e Pés {distPE}')

        if check == True and distMO <= 150 and distPE >= 150:
            contador += 1
            check = False
        if distMO > 150 and distPE < 150:
            check = True

    texto = f'Qtd {contador}'

    cv2.putText(img, texto, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)


    cv2.imshow("Video", img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()