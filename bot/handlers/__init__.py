from .command_start import router_command_start
from .reset_state import router_reset_state
from .control import routers_control


routers = (*routers_control, router_reset_state, router_command_start)
