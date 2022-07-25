import numpy as np

# *названия для функций выбраны разные, но это не несет какого-то скрытого смысла

# данный модуль содержит две функции, выполняющих одну и ту же задачу - перевод изображения в градацию серого, 
# при заданных весовых коэфициентах для каждого цвета (предполагается что сумма коэфициентов = 3)
# функция to_gray использует возможности numpy для эффективной работы с матрицами и работает значительно быстрее функции binarise
# функция binarise работает итеративно и очень медленно, поэтому она не использовалась в основной программе

def to_gray(img, r_coef=1.0, g_coef=1.0, b_coef=1.0):
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    return (r * r_coef + g * g_coef + b * b_coef) // 3


def binarise(img, r_coef=1.0, g_coef=1.0, b_coef=1.0):
    binarised_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
    for i in range(len(img)):
        for j in range(len(img[i])):
            binarised_img[i][j] = (img[i][j][0] * r_coef + img[i][j][1] * g_coef + img[i][j][2] * b_coef) // 3
    return binarised_img