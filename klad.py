# from dateutil.rrule import *
from datetime import datetime, timedelta, date
import requests
import config
import calendar
from bs4 import BeautifulSoup as bs

# a = date(2018, 11, 19)
# b = date(2018, 12, 7)

# for dt in rrule(WEEKLY, dtstart=a, until=b, wkst=MO, byweekday=(MO,WE,FR)):
#     print dt.strftime("%Y-%m-%d")
#     print dt.strftime("%V")

# for key, value in sorted(config.DATES.items()):
#     print(key, value)

