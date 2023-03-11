"""
Объединение всех роутеров в один кортеж
"""

from .basic import routers_basic
from .control import routers_control


routers = (*routers_basic, *routers_control)
