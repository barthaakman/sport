# Dependencies
import datetime
from bs4 import BeautifulSoup as bs
import requests
import config
import calendar

# Session Setup
s = requests.Session()


def login(username, password):
    loginpayload = {'username': username, 'password': password}
    link = 'https://crossfit1693.crossbit.nl/cbm/account/inloggen/?post=1'
    # with requests.Session() as s:
    r = s.post(link, data=loginpayload, verify=True)
    if r.status_code == requests.codes.ok:
        return


def getLink():
    resdate = datetime.datetime.now() + datetime.timedelta(days=3)
    resdate_full = resdate.strftime('%d-%m-%Y')
    resdate_week = resdate.strftime('%V')
    resdate_year = resdate.strftime('%Y')
    resweekday = calendar.day_name[resdate.weekday()]

    if resweekday not in config.DATES:
        print('{} is geen gewenste traindag'.format(resweekday))
        return

    restime = config.DATES.get(resweekday, "")

    payload = {'weekNr': resdate_week, 'year': resdate_year, 'trainer': 'all', 'locatie': '1'}

    link = 'https://crossfit1693.crossbit.nl/cbm/calendar.ajax.php'
    r = s.post(link, data=payload, verify=True)
    soup = bs(r.content, 'lxml')

    attrs = {"data-time-start": restime, "data-date": resdate_full}
    attrsthurs = {"data-start": restime, "data-workout": "WOD"}

    if resdate.weekday() == 3:
        link = soup.find("span", attrs=attrsthurs)
        href = link.get('data-href')
    else:
        link = soup.find("a", attrs=attrs)
        href = link.get('href')

    wodlink = "https://crossfit1693.crossbit.nl/cbm/{}".format(href)
    return wodlink


# Verify successful WOD registration
def isRegistered(wodlink):
    sourceTMP = s.get(wodlink)
    soupTMP = bs(sourceTMP.content, 'lxml')
    for group in soupTMP.find_all('a'):
        if ("AFMELDEN" in group.text):
            return True
    return False


# Check if registering is already possible
def tooSoon(wodlink):
    sourceTMP = s.get(wodlink)
    soupTMP = bs(sourceTMP.content, 'lxml')
    for group in soupTMP.find_all('p'):
        if ("Aanmelden is nog niet mogelijk" in group.text):
            return True
    return False


# Register for a WOD
def register(wodlink):
    reglink = wodlink + "/aanmelden"
    # Registration
    s.get(reglink)
    return
