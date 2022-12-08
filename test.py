import datetime
from datetime import timedelta
import time


# assigned regular string date
rain_start = datetime.datetime.now()
rain_end = rain_start + timedelta(minutes=5)
 
print(int(rain_end.strftime("%Y%m%d%H%M%S")))

