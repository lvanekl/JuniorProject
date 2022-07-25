import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float, io
from my_functions import to_gray, binarise

# данный код использовался для разложения некоторых из картинок на цветовые составляющие для предположения оптимальных цветовых коэфициентов позже
# разложение проводится двумя способами и они выдают разный результат, почему так - я так и не разобрался

for i in range(1, 2):
    fig, axes = plt.subplots(2, 2, figsize=(16, 16))
    ax = axes.flatten()
    filename = f'images/img{i}.png'
    raw_image = io.imread(filename)

    image_red = binarise(raw_image, r_coef=3, g_coef=0, b_coef=0) * -1 + 1
    image_green = binarise(raw_image, r_coef=0, g_coef=3, b_coef=0) * -1 + 1
    image_blue = binarise(raw_image, r_coef=0, g_coef=0, b_coef=3) * -1 + 1

    ax[0].imshow(raw_image)
    ax[0].set_axis_off()
    ax[1].imshow(image_red, cmap='Reds')
    ax[1].set_axis_off()
    ax[2].imshow(image_green, cmap='Greens')
    ax[2].set_axis_off()
    ax[3].imshow(image_blue, cmap='Blues')
    ax[3].set_axis_off()
    plt.show()


for i in range(1, 2):
    fig, axes = plt.subplots(2, 2, figsize=(16, 16))
    ax = axes.flatten()
    filename = f'images/img{i}.png'
    raw_image = io.imread(filename)

    image_red = to_gray(raw_image, r_coef=3, g_coef=0, b_coef=0) * -1 + 1
    image_green = to_gray(raw_image, r_coef=0, g_coef=3, b_coef=0) * -1 + 1
    image_blue = to_gray(raw_image, r_coef=0, g_coef=0, b_coef=3) * -1 + 1

    ax[0].imshow(raw_image)
    ax[0].set_axis_off()
    ax[1].imshow(image_red, cmap='Reds')
    ax[1].set_axis_off()
    ax[2].imshow(image_green, cmap='Greens')
    ax[2].set_axis_off()
    ax[3].imshow(image_blue, cmap='Blues')
    ax[3].set_axis_off()
    plt.show()
