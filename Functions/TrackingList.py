import json
import os

from Functions.ImageTextExtraction import ImageTextExtraction
from Functions.ExtractDataFromText import ExtractDataFromText

class TrackingList:

    def tracking_list(self):
        images_path = "pics"
        images = os.listdir(images_path)

        result = {}
        image_extraction = ImageTextExtraction()
        extract_data = ExtractDataFromText()

        for image in images:
            data = image_extraction.process_image(f'{images_path}/{image}')
            text = image_extraction.read_text(data)

            info = extract_data.extract_info_mobile_ss(text)
            tracking_number = info.get('tracking_number')
            otp = info.get('otp')

            if len(otp) == 6 and otp.isnumeric():
                result[tracking_number] = otp
                continue

            gray = image_extraction.color_to_gray(data)
            text = image_extraction.read_text(gray)

            info = extract_data.extract_info_mobile_ss(text)
            tracking_number1 = info.get('tracking_number')
            otp = info.get('otp')

            if len(otp) == 6 and otp.isnumeric():
                if tracking_number1 == tracking_number:
                    result[tracking_number1] = otp
                else:
                    result[tracking_number] = otp
                continue

            thresh = image_extraction.gray_to_thresh(gray)
            text = image_extraction.read_text(thresh)

            info = extract_data.extract_info_mobile_ss(text)
            tracking_number2 = info.get('tracking_number')
            otp = info.get('otp')

            if len(otp) == 6 and otp.isnumeric():
                if tracking_number2 == tracking_number:
                    result[tracking_number2] = otp
                else:
                    result[tracking_number] = otp
                continue

            resize = image_extraction.resize_image(thresh)
            text = image_extraction.read_text(resize)

            info = extract_data.extract_info_mobile_ss(text)
            tracking_number3 = info.get('tracking_number')
            otp = info.get('otp')

            if tracking_number3 == tracking_number:
                result[tracking_number3] = otp
            else:
                result[tracking_number] = otp

        return result
