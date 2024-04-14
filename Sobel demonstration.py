#Импортируем библиотеки
import cv2
import numpy as np
my_photo = cv2.imread('MyPhoto.jpg',cv2.IMREAD_GRAYSCALE)#Загружаем фотографию  в оттенках серого с помощью функции, сохраняем ее в переменную.
kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])#ранее описанные матрицы для применения свертки с помощью функции
im = cv2.filter2D(my_photo, -1, kernel)#Применяем свертку к изображению
cv2.imshow('MyPhoto', im )
cv2.waitKey(0)
cv2.destroyAllWindows()
#Последние строчки позволяют отобразить измененное изображение