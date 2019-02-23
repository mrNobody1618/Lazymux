import imp
import os
try:
    import pyfiglet
except ImportError:
    # Change below command to pip2 install pyfiglet before commiting for termux
    pip = lambda : os.system('pip install pyfiglet')
    pip()

