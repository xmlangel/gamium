from typing import Optional


class QueryObjectInteractableOptions:
    def __init__(
        self,
        check_moving: Optional[bool] = True,
        check_raycast: Optional[bool] = True,
    ):
        self.check_moving = check_moving
        self.check_raycast = check_raycast
