import pyautogui as pag
import time

screenWidth, screenHeight = pag.size()
urlBarX, urlBarY = (546, 99)

urls = [
    'https://crowncoinscasino.com/',
    'https://realprize.com/',
    'https://lonestarcasino.com/',
    'https://taofortune.com/',
    'https://nolimitcoins.com/',
    'https://fortunewins.com/',
    'https://www.wowvegas.com/',
    'https://www.chumbacasino.com/',
    'https://funrize.com/',
    'https://acebet.cc/',
    'https://luckystake.com/'
]

claim_steps = {
    'https://crowncoinscaino.com/': {
        'login': [
            # click (x, y)
            # wait some time
            # click (x, y)
            # ...
        ],
        'claim': [
            # click (x, y)
            # wait some time
            # click (x, y)
            # ...
        ]
    },
    'https://realprize.com/': {
        'login': [],
        'claim': []
    },
    'https://lonestarcasino.com/': {
        'login': [],
        'claim': []
    },
    'https://taofortune.com/': {
        'login': [],
        'claim': []
    },
    'https://nolimitcoins.com/': {
        'login': [],
        'claim': []
    },
    'https://fortunewins.com/': {
        'login': [],
        'claim': []
    },
    'https://www.wowvegas.com/': {
        'login': [],
        'claim': []
    },
    'https://www.chumbacasino.com/': {
        'login': [],
        'claim': []
    },
    'https://funrize.com/': {
        'login': [],
        'claim': []
    },
    'https://acebet.cc/': {
        'login': [],
        'claim': []
    },
    'https://luckystake.com/': {
        'login': [],
        'claim': []
    }
}

def navigate_to_url(url):
    pag.click(urlBarX, urlBarY)
    pag.hotkey('ctrl', 'a')
    print('Navigating to URL: ', url)
    pag.write(url, interval=0.1)
    pag.press('enter')

def logged_in():
    # check for words like log out or log in

    pag.hotkey('ctrl', 'f')
    pag.write('Log In', interval=0.1)
    # check screen coordinates for "1/1"

    if True:
        return True
    else:
        return False

def log_in():
    pass

for url in urls:
    time.sleep(10)
    navigate_to_url(url)

    if logged_in:
        continue
    else:
        log_in()

    # claim daily rewards
    time.sleep(10)