import cv2
import numpy as np
import pytesseract
import os
import json
from collections import defaultdict
from PIL import Image
#
# # Set up Tesseract command
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def process_image(image_path):
    """
    Extracts text from an image and returns it.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    #
    # # Convert to grayscale for better OCR accuracy
    # gray = color_to_gray(image)
    # # Apply a threshold to make the text stand out
    # thresh = gray_to_thresh(gray)
    # # Optionally resize the image for better OCR (enlarge if needed)
    # resized = resize(thresh)
    # # Use Tesseract to extract text
    # text = read_text(image)
    return image

def color_to_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # text = read_text(gray)
    return gray

def gray_to_thresh(gray):
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # text = read_text(thresh)
    return thresh

def resize_image(image):
    resized = cv2.resize(image, dsize=(0,0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LANCZOS4)
    return resized

def read_text(image):
    pil_image = Image.fromarray(image)
    text = pytesseract.image_to_string(pil_image)
    return text

def denoising_image(gray):
    denoised_image = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
    return denoised_image

def sharpened_image(image):
    sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    contrast_adjusted = cv2.convertScaleAbs(sharpened_image, alpha=1.5, beta=30)
    return contrast_adjusted

def clean_image(image):
    kernel = np.ones((3, 3), np.uint8)
    morphological_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return morphological_image
