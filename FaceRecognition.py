import cv2 as cv

cap = cv.VideoCapture(0)

# Загрузка классификатора Хаара для лиц
face_cascade = cv.CascadeClassifier('/home/theo110/Documents/Projects/OpenCV/haarcascade_frontalface_default.xml')

while True:
    if cv.waitKey(1) == 27:
        break
# Загрузка изображения
    _, image = cap.read()

# Преобразование в серый цвет
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Рисование прямоугольников вокруг лиц
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Отображение изображения
    cv.imshow('asd', image)
#cv.waitKey(0)
