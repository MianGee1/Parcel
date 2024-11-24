import json
import os

from Functions.ImageTextExtraction import ImageTextExtraction
from Functions.ExtractDataFromText import ExtractDataFromText

class TrackingList:
    def extract_tracking(self, text, tracking_number):
        extract_tracking = ExtractDataFromText()

        if not tracking_number:
            tracking_number = extract_tracking.extract_tracking_number(text)

        return tracking_number



    # def tracking_list(self):
    #     images_path = "pics"
    #     images = os.listdir(images_path)
    #
    #     result = {}
    #     image_extraction = ImageTextExtraction()
    #     extract_data = ExtractDataFromText()
    #
    #     for image in images:
    #         data = image_extraction.process_image(f'{images_path}/{image}')
    #         text = image_extraction.read_text(data)
    #
    #         info = extract_data.extract_info_mobile_ss(text)
    #         tracking_number = info.get('tracking_number')
    #         otp = info.get('otp')
    #
    #         if len(otp) == 6 and otp.isnumeric() and len(tracking_number) == 15:
    #             result[tracking_number] = otp
    #             continue
    #
    #         gray = image_extraction.color_to_gray(data)
    #         text = image_extraction.read_text(gray)
    #
    #         info = extract_data.extract_info_mobile_ss(text)
    #         tracking_number1 = info.get('tracking_number')
    #         otp = info.get('otp')
    #
    #         if len(otp) == 6 and otp.isnumeric():
    #             if tracking_number1 == tracking_number:
    #                 result[tracking_number1] = otp
    #             else:
    #                 result[tracking_number] = otp
    #             continue
    #
    #         thresh = image_extraction.gray_to_thresh(gray)
    #         text = image_extraction.read_text(thresh)
    #
    #         info = extract_data.extract_info_mobile_ss(text)
    #         tracking_number2 = info.get('tracking_number')
    #         otp = info.get('otp')
    #
    #         if len(otp) == 6 and otp.isnumeric():
    #             if tracking_number2 == tracking_number:
    #                 result[tracking_number2] = otp
    #             else:
    #                 result[tracking_number] = otp
    #             continue
    #
    #         resize = image_extraction.resize_image(thresh)
    #         text = image_extraction.read_text(resize)
    #
    #         info = extract_data.extract_info_mobile_ss(text)
    #         tracking_number3 = info.get('tracking_number')
    #         otp = info.get('otp')
    #
    #         if tracking_number3 == tracking_number:
    #             result[tracking_number3] = otp
    #         else:
    #             result[tracking_number] = otp
    #
    #     return result


    def tracking_list(self):
        images_path = "pics"
        images = os.listdir(images_path)

        result = {}
        not_extracted = []
        image_extraction = ImageTextExtraction()
        extractor = ExtractDataFromText()

        for image in images:
            data = image_extraction.process_image(f'{images_path}/{image}')

            # Process through multiple cleaning and text-reading steps

            for step in ['original','gray', 'resize', 'thresh']:

                if step == 'original':
                    text = image_extraction.read_text(data)
                else:
                    data = self.extract_text_from_step(data, image_extraction, step)
                    text = image_extraction.read_text(data)

                info = extractor.extract_info_mobile_ss(text)

                tracking_number = info.get('tracking_number')
                otp = info.get('otp')

                if tracking_number and otp:
                    if len(tracking_number) == 15 and len(otp) == 6:
                        result[tracking_number] = otp
                        if image in not_extracted:
                            not_extracted = list(set(not_extracted))
                            not_extracted.remove(image)
                        break  # Stop processing further once valid data is found
                    else:
                        not_extracted.append(image)
                else:
                    not_extracted.append(image)
            not_extracted = list(set(not_extracted))

        for image in not_extracted:
            data = image_extraction.process_image(f'{images_path}/{image}')

            # Process through multiple cleaning and text-reading steps

            for step in ['original', 'gray', 'denoising', 'sharpening', 'thresh', 'resize']:

                if step == 'original':
                    text = image_extraction.read_text(data)
                else:
                    data = self.extract_text_from_step(data, image_extraction, step)
                    text = image_extraction.read_text(data)

                info = extractor.extract_info_mobile_ss(text)

                tracking_number = info.get('tracking_number')
                otp = info.get('otp')

                if tracking_number and otp:
                    if len(tracking_number) == 15 and len(otp) == 6:
                        result[tracking_number] = otp
                        if image in not_extracted:
                            not_extracted = list(set(not_extracted))
                            not_extracted.remove(image)
                        break  # Stop processing further once valid data is found
                    else:
                        not_extracted.append(image)
                else:
                    not_extracted.append(image)

        print(not_extracted, '\n', len(not_extracted))


        return result


    def extract_text_from_step(self, data, image_extraction, step):
        temp = data
        if step == 'gray':
            data = image_extraction.gray_image(data)
        elif step == 'denoising':
            data = image_extraction.denoising_image(data)
        elif step == 'resize':
            data = image_extraction.resize_image(data)
        elif step == 'sharpening':
            data = image_extraction.sharpened_image(data)
        elif step == 'thresh':
            data = image_extraction.thresh_image(data)
        elif step == 'morphological':
            data = image_extraction.morphological_image(data)

        if data is None:
            return temp
        else:
            return data



