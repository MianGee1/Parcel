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

    def gray_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def thresh_image(self, image):
        thresh = cv2.adaptiveThreshold( image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        return thresh

    def resize_image(self, image):
        resized = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        return resized

    def read_text(self, image):
        pil_image = Image.fromarray(image)
        text = pytesseract.image_to_string(pil_image)
        return text

    def denoising_image(self, image):
        denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

        # denoised_image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
        return denoised_image

    def sharpened_image(self, image):
        sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
        contrast_adjusted = cv2.convertScaleAbs(sharpened_image, alpha=1.5, beta=30)
        return contrast_adjusted

    def morphological_image(self, image):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        morph_result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        return morph_result



