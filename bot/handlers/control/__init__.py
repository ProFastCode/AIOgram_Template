"""
Центр управления
"""

from .administrator import router_administrator
from .add_moderator import router_add_moderator
from .get_moderators import router_get_moderators
from .demote_moderator import router_demote_moderator

routers_control = (
    router_administrator,
    router_add_moderator,
    router_get_moderators,
    router_demote_moderator,
)
