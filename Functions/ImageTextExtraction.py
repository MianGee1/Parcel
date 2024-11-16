import cv2
import numpy as np
import json
import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class ImageTextExtraction:

    def process_image(self, image):
        image = cv2.imread(image)
        return image

    def color_to_gray(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def gray_to_thresh(self, gray):
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return thresh

    def resize_image(self, image):
        resized = cv2.resize(image, dsize=(0,0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LANCZOS4)
        return resized

    def read_text(self, image):
        pil_image = Image.fromarray(image)
        text = pytesseract.image_to_string(pil_image)
        return text

    def denoising_image(self, gray):
        denoised_image = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
        return denoised_image

    def sharpened_image(self, image):
        sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
        contrast_adjusted = cv2.convertScaleAbs(sharpened_image, alpha=1.5, beta=30)
        return contrast_adjusted

    def clean_image(self, image):
        kernel = np.ones((3, 3), np.uint8)
        morphological_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        return morphological_image
