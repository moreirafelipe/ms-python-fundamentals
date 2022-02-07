#Import module as namespace
import helpers
helpers.display('Not a warning')

#Import all into current namespace
from helpers import *
display('Not a warning')

#Import specific items into current namespace
from helpers import display
display('Not a warning')

#Install python packages
#pip install colorama

#Install from a list of packages
#pip install -r requirements.txt

#requirements.txt
#colorama