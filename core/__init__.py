import imp
import os
try:
    import pyfiglet
except ImportError:
    pip = lambda : os.system('pip2 install pyfiglet')
    pip()

