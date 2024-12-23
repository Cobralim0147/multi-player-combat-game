# combat_producer.py
import json
from kafka import KafkaProducer
from game_constants import AttackType, BlockType

class CombatProducer:
    def __init__(self, bootstrap_servers=['localhost:29092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_action(self, player_id: str, action_type: str, target: str):
        action = {
            "player_id": player_id,
            "action_type": action_type,
            "target": target
        }
        self.producer.send('combat-actions', action)
        self.producer.flush()
