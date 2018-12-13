# Dependencies
import config
import func
import requests

# Session Setup
s = requests.Session()

# Login
func.login(config.USERNAME, config.PASSWORD)

# Get link
wodlink = func.getLink()

# Check if wodlink returns None
if wodlink is None:
    print('Geen WOD link beschikbaar')
    raise SystemExit(0)

# Check if already registered
if func.isRegistered(wodlink):
    print('Je bent al aangemeld voor deze les.')
    raise SystemExit(0)

# Check if too soon to register
if func.tooSoon(wodlink):
    print('Te vroeg om aan te melden voor deze les.')
    raise SystemExit(0)

# Register for desired class
while not func.isRegistered(wodlink) or func.tooSoon(wodlink):
    func.register(wodlink)
    print('Succesvol aangemeld voor WOD %s' % wodlink)
    # print('WOD voor %s om %s succesvol aangemeld.' % (,))

# Registration Complete

