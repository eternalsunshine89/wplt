import time


def sleep(t=2):
    time.sleep(t)


def now():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def now_without_symbol():
    return time.strftime('%Y%m%d%H%M%S')
