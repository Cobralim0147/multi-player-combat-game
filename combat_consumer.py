# combat_consumer.py
# python -c "from combat_consumer import CombatConsumer; CombatConsumer().run()"  
import json
from kafka import KafkaConsumer
from game_constants import AttackType, BlockType
from game_state import GameState

class CombatConsumer:
    def __init__(self, bootstrap_servers=['localhost:29092']):
        self.consumer = KafkaConsumer(
            'combat-actions',
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=True
        )
        self.game_state = GameState()
        self.pending_action = None

    def process_combat(self, attack: str, block: str) -> int:
        damage_table = {
            (AttackType.HEAD.value, BlockType.TOP.value): 0,
            (AttackType.HEAD.value, BlockType.MIDDLE.value): 20,
            (AttackType.HEAD.value, BlockType.BOTTOM.value): 30,
            (AttackType.STOMACH.value, BlockType.TOP.value): 20,
            (AttackType.STOMACH.value, BlockType.MIDDLE.value): 0,
            (AttackType.STOMACH.value, BlockType.BOTTOM.value): 20,
            (AttackType.LEG.value, BlockType.TOP.value): 30,
            (AttackType.LEG.value, BlockType.MIDDLE.value): 20,
            (AttackType.LEG.value, BlockType.BOTTOM.value): 0,
        }
        return damage_table.get((attack, block), 0)

    def run(self):
        print("Combat game started! Waiting for player actions...")
        for message in self.consumer:
            action = message.value
            player_id = action["player_id"]
            action_type = action["action_type"]
            target = action["target"]

            if player_id != self.game_state.current_turn:
                print(f"Not {player_id}'s turn!")
                continue

            if self.pending_action is None:
                self.pending_action = action
                self.game_state.switch_turn()
                print(f"Waiting for {self.game_state.current_turn}'s response...")
            else:
                # Process combat
                attacker_id = self.pending_action["player_id"]
                defender_id = player_id
                damage = self.process_combat(self.pending_action["target"], target)
                
                # Apply damage
                self.game_state.apply_damage(defender_id, damage)
                
                # Print combat results
                print(f"\nCombat Results:")
                print(f"{attacker_id} attacked {self.pending_action['target']}")
                print(f"{defender_id} blocked {target}")
                print(f"Damage dealt: {damage}")
                print(f"\nCurrent Health:")
                print(f"Player 1: {self.game_state.players['player1']['health']}")
                print(f"Player 2: {self.game_state.players['player2']['health']}")
                
                self.pending_action = None
                
                if self.game_state.is_game_over():
                    winner = self.game_state.get_winner()
                    print(f"\nGame Over! {winner} wins!")
                    break
                
                print(f"\n{self.game_state.current_turn}'s turn!")
