__author__ = 'Hibiki'

# python supplied modules
import subprocess

from utils import pretty_subprocess

def init():
    pretty_subprocess(['./shells/init.sh'], 'init.sh')


def screenshot(fname):
    pretty_subprocess(['./shells/cap.sh', fname], 'cap.sh')


def clean():
    pretty_subprocess(['./shells/cleanup.sh'], 'cleanup.sh')

'''
    This function doesn't use pretty_subprocess because
    we are not running a script.
'''
def tap(x, y):
    subprocess.call(['adb', 'shell', 'input', 'tap', str(x), str(y)])
