# Dependencies
import datetime
import calendar
import requests
from bs4 import BeautifulSoup as bs
import config
import func

# Session Setup
s = requests.Session()


def getLink():
    resdate = datetime.datetime.now() + datetime.timedelta(days=3)
    resdate_full = resdate.strftime('%d-%m-%Y')
    resdate_week = resdate.strftime('%V')
    resdate_year = resdate.strftime('%Y')
    resweekday = calendar.day_name[resdate.weekday()]

    if resweekday not in config.DATES:
        return

    restime = config.DATES.get(resweekday, "")

    payload = {'weekNr': resdate_week, 'year': resdate_year, 'trainer': 'all', 'locatie': '1'}

    link = 'https://crossfit1693.crossbit.nl/cbm/calendar.ajax.php'
    r = s.post(link, data=payload, verify=True)
    soup = bs(r.content, 'lxml')

    attrs = {"data-time-start": restime, "data-date": resdate_full}
    attrsthurs = {"data-start": restime, "data-workout": "WOD"}

    if datetime.datetime.today().weekday() == 3:
        link = soup.find("span", attrs=attrsthurs)
        href = link.get('data-href')
    else:
        link = soup.find("a", attrs=attrs)
        href = link.get('href')

    wodlink = "https://crossfit1693.crossbit.nl/cbm/{}".format(href)
    return wodlink


linkje = getLink()

print(linkje)

print(func.tooSoon('https://crossfit1693.crossbit.nl/cbm/training-info/19-12-2018/17:00/2853/'))
print(func.isRegistered('https://crossfit1693.crossbit.nl/cbm/training-info/12-12-2018/19:00/2808/'))
