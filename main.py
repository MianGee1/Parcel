import time
from Functions.TrackingList import TrackingList
from Automation.parcel_out import ParcelOut

images_path = 'pics'
tracking = TrackingList()
result = tracking.tracking_list(images_path)

out = ParcelOut()
time.sleep(2)
out.out(result)




