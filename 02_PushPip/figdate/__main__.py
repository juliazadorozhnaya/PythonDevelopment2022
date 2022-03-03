import time
import pyfiglet
import sys


def date(fmt, font):
    result = pyfiglet.Figlet(font=font)
    return result.renderText(time.strftime(fmt, time.gmtime()))


fmt = '%Y %d %b %A'
font = 'graceful'

if len(sys.argv) == 2:
    fmt = sys.argv[1]
elif len(sys.argv) == 3:
    font = sys.argv[2]

print(date(fmt=fmt, font=font))