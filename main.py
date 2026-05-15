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
            (935, 723)
        ]
    },
    'https://realprize.com/': {
        'login': [],
        'claim': [
            (962, 909)
        ]
    },
    'https://lonestarcasino.com/': {
        'login': [],
        'claim': [
            (956, 854)
        ]
    },
    'https://taofortune.com/': {
        'login': [],
        'claim': [
            (45, 170),
            (70, 286),
            (828, 514),
            (45, 170),
            (94, 327),
            (952, 825)
        ]
    },
    'https://nolimitcoins.com/': {
        'login': [],
        'claim': [
            (1146, 452),
            # click menu button
            (45, 155),
            (964, 596),
            (959, 751),
            (1147, 381),
            # click menu button
            (45, 155),
            # click daily reward
            (126, 581),
            # click claim rewards
            (959, 813),
            # click collect
            (952, 797)
        ]
    },
    'https://fortunewins.com/': {
        'login': [
            # click login
            (1370, 161),
            # click next login
            (1229, 680)
        ],
        'claim': [
            # click get coins
            (1370, 147),
            # click free coins
            (1091, 248),
            # click collect
            (536, 651)
        ]
    },
    'https://www.wowvegas.com/': {
        'login': [],
        'claim': [
            # click menu
            (42, 159)
        ]
    },
    'https://www.chumbacasino.com/': {
        'login': [
            # click login
            (1265, 195),
            # click next login
            (275, 672)
        ],
        'claim': [
            # click get coins
            (1695, 149),
            # click daily bonus
            (1057, 260),
            # scroll down dunno yet
            (-1, -1),
            # click claim
            (951, 862)
        ]
    },
    'https://funrize.com/': {
        'login': [],
        'claim': [
            # click free spin
            (41, 352),
            # click spin
            (962, 504),
            # click x
            (1397, 195),
            # click daily rewards
            (92, 406),
            # click collect
            (729, 792)
        ]
    },
    'https://luckystake.com/': {
        'login': [
            # click login
            (1375, 182),
            # click email box
            (937, 606),
            # click email
            (951, 652),
            # click sign in
            (957, 766)
        ],
        'claim': [
            # click claim
            (964, 863)
        ]
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
    time.sleep(5)
    navigate_to_url(url)

    # claim daily rewards
    for step in claim_steps[url]['claim']:
        print(step)
        print(step[0], step[1])
        if step[0] == -1 and step[1] == -1:
            pag.scroll(-3)
        pag.click(step[0], step[1])
        time.sleep(5)