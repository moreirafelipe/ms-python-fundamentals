#helpers.py
from colorama import init
init()

from colorama import Fore, Back, Style

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + 'Warning!!')
    print(Fore.BLUE + message)