from .panel import router_panel
from .add_moderator import router_add_moderator
from .get_moderators import router_get_moderators

routers_control = (router_panel, router_add_moderator, router_get_moderators)
