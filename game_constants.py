# game_constants.py
from enum import Enum

class AttackType(Enum):
    HEAD = "head"
    STOMACH = "stomach"
    LEG = "leg"

class BlockType(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"

class PlayerAction:
    def __init__(self, player_id: str, action_type: str, target: str):
        self.player_id = player_id
        self.action_type = action_type
        self.target = target
