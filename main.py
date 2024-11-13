import time

from Functions.ImageTextExtraction import process_image
from Functions.ImageTextExtraction import color_to_gray
from Functions.ImageTextExtraction import gray_to_thresh
from Functions.ImageTextExtraction import resize_image
from Functions.ImageTextExtraction import read_text
from Functions.ExtractDataFromText import extract_info
from Automation.parcel_out import ParcelOut

import os

images_path = 'pics'
images = os.listdir(images_path)

result = {}
for image in images:
    data = process_image(f'{images_path}/{image}')

    text = read_text(data)
    info = extract_info(text)
    tracking_number = info.get('tracking_number')
    otp = info.get('otp')
    if len(otp) == 6 and otp.isnumeric():
        result[tracking_number] = otp
        continue
    gray = color_to_gray(data)
    text = read_text(gray)
    info = extract_info(text)
    tracking_number1 = info.get('tracking_number')
    otp = info.get('otp')
    if len(otp) == 6 and otp.isnumeric():
        if tracking_number1 == tracking_number:
            result[tracking_number1] = otp
        else:
            result[tracking_number] = otp
        continue
    thresh = gray_to_thresh(gray)
    text = read_text(thresh)
    info = extract_info(text)
    tracking_number2 = info.get('tracking_number')
    otp = info.get('otp')
    if len(otp) == 6 and otp.isnumeric():
        if tracking_number2 == tracking_number:
            result[tracking_number2] = otp
        else:
            result[tracking_number] = otp
        continue
    resize = resize_image(thresh)
    text = read_text(thresh)
    info = extract_info(text)
    tracking_number3 = info.get('tracking_number')
    otp = info.get('otp')
    if tracking_number3 == tracking_number:
        result[tracking_number3] = otp
    else:
        result[tracking_number] = otp

    out = ParcelOut()
    time.sleep(2)
    out.out(result)




