import numpy as np
import cv2 as cv
import imutils
import cv2

# параметры цветового фильтра
hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)
img = cv.imread("C:\\45\\000.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV )
# меняем цветовую модель с BGR на HSV
thresh = cv.inRange(hsv, hsv_min, hsv_max )
# применяем цветовой фильтр
# ищем контуры и складируем их в переменную contours
contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#попытка нарисовать хотябы линию на картинке (не работает)
c = max(contours, key = cv.contourArea)
M = cv2.moments(c)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print (cX,cY)
else:
    cX, cY = 0,0
    print (cX,cY)

# отображаем контуры поверх изображения
cv.drawContours(img, contours, -1, (255, 0, 0), 2, cv.LINE_AA, hierarchy, 0)
cv.imshow('contours', img)
cv.drawContours(img, contours, -1, (255, 0, 0), 2, cv.LINE_AA, hierarchy, 2)
# выводим итоговое изображение в окно
cv.imshow('All_con', img)
cv.imshow('thresh', thresh)
cv.waitKey()
cv.destroyAllWindows()