# game_state.py
class GameState:
    def __init__(self):
        self.players = {
            "player1": {"health": 100, "name": "Player 1"},
            "player2": {"health": 100, "name": "Player 2"}
        }
        self.current_turn = "player1"

    def switch_turn(self):
        self.current_turn = "player2" if self.current_turn == "player1" else "player1"

    def apply_damage(self, defender: str, damage: int):
        self.players[defender]["health"] -= damage
        if self.players[defender]["health"] < 0:
            self.players[defender]["health"] = 0

    def is_game_over(self):
        return any(player["health"] <= 0 for player in self.players.values())

    def get_winner(self):
        if not self.is_game_over():
            return None
        return "player1" if self.players["player2"]["health"] <= 0 else "player2"
