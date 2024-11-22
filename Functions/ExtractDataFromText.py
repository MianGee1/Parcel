import re

class ExtractDataFromText:

    def extract_info(self, text):
        # # Regex pattern for tracking number
        # tracking_pattern = 'PK-DEX\d+'
        # Regex pattern for OTP
        otp_pattern = r'\b\d{6}\b'

        # tracking_pattern = r'Tracking Number\s*([A-Z0-9\-]+)'
        # Regex pattern for OTP
        # otp_pattern = r'OTP\s*for Package Collection\s*(\d{6})'

        # Search for tracking number
        # tracking_match = re.search(tracking_pattern, text)
        # tracking_id = tracking_match.group(1) if tracking_match else None
        # otp = text.replace('\n', ' ').split('Package Collection ')[1].strip().split(' ')[0]
        # tracking_number = text.split('Tracking Number ')[1].split('\n')[0]
        # return tracking_id, otp

    def clean_otp(self, otp):
        otp = otp.lower()
        if 'o' in otp:
            otp = otp.replace('o', '0')

        if 'n' in otp:
            otp = otp.replace('n', '11')

        if 's' in otp:
            otp = otp.replace('s', '5')

        return otp

    def clean_tracking(self, tracking):
        tracking = tracking.replace('.', '')
        tracking = tracking.replace(',', '')
        return tracking

    def extract_info_mobile_ss(self, text):
        text = text.strip()
        text = text.replace('\n', ' ')
        get_info = lambda info, key: info.split(key)[1].strip().split(' ')[0]
        try:
            otp = re.search(r'\s(\d{6})' , text).group(0).strip()
            tracking_number = re.search(r'\sPK-DEX\d{8,}\s', text).group(0).strip()
        except:
            tracking_number = get_info(text, 'Tracking Number')
            try:
                otp = get_info(text, 'Package Collection')
            except IndexError:
                otp = get_info(text, 'Provide your OTP')
        otp = self.clean_otp(otp)
        tracking_number = self.clean_tracking(tracking_number)
        return {'tracking_number': tracking_number, 'otp': otp }
