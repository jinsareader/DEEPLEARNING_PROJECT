import os

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt

# 이미지 경로 설정
image_dir = 'D:\IMG\TEST'

# 이미지 크기, 배치 크기 설정
IMG_HEIGHT = 150
IMG_WIDTH = 150
BATCH_SIZE = 32

# 데이터 전처리 및 증강
datagen = ImageDataGenerator(
    rescale=1./255,             # 모든 픽셀을 0~1로 스케일링
    validation_split=0.2,       # 80% 학습, 20% 검증
    rotation_range=20,          # 이미지 회전
    width_shift_range=0.2,      # 좌우 이동
    height_shift_range=0.2,     # 상하 이동
    shear_range=0.2,            # 이미지 절단
    zoom_range=0.2,             # 줌 인/아웃
    horizontal_flip=True        # 좌우 반전
)

# 학습 데이터 생성
train_generator = datagen.flow_from_directory(
    image_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary',  # 이진 분류 (스티로폼 vs 비스티로폼)
    subset='training'
)

# 검증 데이터 생성
validation_generator = datagen.flow_from_directory(
    image_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)



# 사전 학습된 VGG16 모델 불러오기 (ImageNet 가중치 사용, Top layer 제외)
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3))

# 사전 학습된 모델의 가중치는 고정
base_model.trainable = False

# 새로운 모델 정의 (Fine-Tuning)
model = models.Sequential()
model.add(base_model)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))  # 이진 분류

# 모델 컴파일
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 요약 출력
model.summary()


# 모델 학습
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // BATCH_SIZE,
    epochs=10  # 필요한 학습 반복 횟수 설정
)

# 모델 저장
model.save('styrofoam_classifier.h5')



# 정확도 시각화
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

# 손실 시각화
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.show()
