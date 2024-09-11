import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 학습된 모델 로드
model = load_model('styrofoam_classifier.h5')

# 카메라 사용을 위한 OpenCV 설정
cap = cv2.VideoCapture(0)
IMG_HEIGHT = 150
IMG_WIDTH = 150
while True:
    ret, frame = cap.read()
    
    # 카메라에서 받은 이미지를 모델 입력 크기로 조정
    img = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # 동일한 전처리 과정 적용

    # 예측 수행
    prediction = model.predict(img)

    # 예측 결과에 따라 스티로폼 여부 표시
    if prediction > 0.5:
        label = 'Styrofoam'
    else:
        label = 'Not Styrofoam'

    # 화면에 예측 결과 출력
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Styrofoam Detector', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라와 창 닫기
cap.release()
cv2.destroyAllWindows()
