import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import savReaderWriter
import locale
import os
from sav2acces import *
locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')


write_ms_access_file("someFile.sav")

