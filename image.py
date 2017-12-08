import imageio
import numpy as np
import cv2
from PIL import Image


def get_mean_rgb(image):
    means = []
    for i in range(0, 3):
        means.append(np.mean(image[:, :, i]))
    return means


def normalize_image(image):
    hsv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    hsv[:, :, 2] = 128
    hsv[:, 2, :] = 128
    normalized_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return normalized_image


def generate_hash(image, sections):
    height = len(image)
    width = len(image[0])
    without_frame = image[height // 10: 9 * height // 10, width // 10: 9 * width // 10]

    height = len(without_frame)
    width = len(without_frame[0])

    image_hash = []
    for h in range(sections):
        for w in range(sections):
            h_min = (h * height) // sections
            h_max = ((h + 1) * height) // sections
            w_min = (w * width) // sections
            w_max = ((w + 1) * width) // sections

            image_hash.extend(get_mean_rgb(without_frame[h_min:h_max, w_min:w_max]))

    return image_hash


def process_image(filename):
    average_image = []
    length = 1

    reader = imageio.get_reader(filename)
    for index, image in enumerate(reader):
        if index == 0:
            height, width, colors = image.shape
            average_image = np.zeros((height, width, colors), np.float)

        average_image = np.add(average_image, image)
        length = index + 1

    average_image = np.divide(average_image, length)
    average_image = np.array(np.round(average_image), dtype=np.uint8)

    normalized_image = normalize_image(average_image)
    return generate_hash(image=normalized_image, sections=10)
