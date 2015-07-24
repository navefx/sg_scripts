__author__ = 'nxn3370'

from shotgun_api3 import Shotgun
from core import conf

sg = Shotgun( conf.site, conf.script, conf.api_key )