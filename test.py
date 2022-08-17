import datetime
from datetime import timedelta
import time


# assigned regular string date
rain_start = datetime.datetime.now()
rain_end = rain_start + timedelta(minutes=5)
 
 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
     "<t:"+ str(int((time.mktime(rain_end.timetuple()))))+ ":R>")
      

rain_start = datetime.datetime.now()
rain_end = rain_start + timedelta(minutes=5)

"<t:"+ str(int((time.mktime(rain_end.timetuple()))))+ ":R>"