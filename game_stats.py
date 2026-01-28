from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        saved = self.get_saved_high_score()
        self.high_score = saved["score"]
        self.high_score_name = saved["name"]


    def get_saved_high_score(self):
        """Gets high score record from file, if it exists.
        Returns dict: {"score": int, "name": str}
        """
        path = Path('high_score.json')
        try:
            contents = path.read_text(encoding="utf-8")
            data = json.loads(contents)

            # 新格式
            score = int(data.get("score", 0))
            name = str(data.get("name", "")).strip()
            return {"score": score, "name": name}

        except FileNotFoundError:
            return {"score": 0, "name": ""}
        except:
            print("""请检查 high_score.json 文件格式：{"score": , "name": ""}""")
            raise SystemExit


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
