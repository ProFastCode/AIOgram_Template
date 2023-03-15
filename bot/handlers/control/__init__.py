"""
Центр управления
"""

from .add_moderator import router_add_moderator
from .administrator import router_administrator
from .demote_moderator import router_demote_moderator
from .get_moderators import router_get_moderators
from .mailing_list import router_mailing_list
from .moderator import router_moderator

routers_control = (
    router_administrator,
    router_add_moderator,
    router_get_moderators,
    router_demote_moderator,
    router_mailing_list,
    router_moderator,
)
