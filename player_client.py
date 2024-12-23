# player_client.py
from combat_producer import CombatProducer
from game_constants import AttackType, BlockType

def main():
    producer = CombatProducer()
    player_id = input("Enter your player ID (player1 or player2): ").strip()
    
    while True:
        print("\nYour turn!")
        print("1. Attack")
        print("2. Block")
        action_type = input("Choose your action (1 or 2): ").strip()
        
        if action_type == "1":
            print("\nChoose attack target:")
            print("1. Head")
            print("2. Stomach")
            print("3. Leg")
            target = input("Enter target (1-3): ").strip()
            target_map = {"1": "head", "2": "stomach", "3": "leg"}
            target = target_map.get(target, "head")
        else:
            print("\nChoose block position:")
            print("1. Top")
            print("2. Middle")
            print("3. Bottom")
            target = input("Enter position (1-3): ").strip()
            target_map = {"1": "top", "2": "middle", "3": "bottom"}
            target = target_map.get(target, "top")
        
        producer.send_action(player_id, action_type, target)
        print("Action sent! Waiting for other player...")

if __name__ == "__main__":
    main()