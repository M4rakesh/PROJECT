import cv2
import numpy as np

# Чтение изображения
image = cv2.imread('Untitled.png', cv2.IMREAD_UNCHANGED)

# Если изображение имеет альфа-канал, то его нужно убрать
if image.shape[2] == 4:
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# Преобразование в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение бинаризации (пороговой обработки) для выделения объектов
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Нахождение контуров
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Масштаб: количество метров на пиксель (например, 0.01 метра на пиксель)
scaling_factor = 0.01  # Можете настроить это значение в зависимости от вашего изображения

# Перебор контуров и вычисление площади каждого из них в пикселях
for contour in contours:
    area_pixels = cv2.contourArea(contour)
    # Конвертация площади из пикселей в квадратные метры
    area_meters = area_pixels * (scaling_factor ** 2)
    print(f'Площадь объекта: {area_meters} м²')

    # Для визуализации, можно нарисовать контуры на изображении
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Показать изображение с контурами
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
