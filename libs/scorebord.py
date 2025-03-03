import simplejson as json

class Scoreboard:
    def __init__(self):
        self.scores = []

    def add(self, name, score):
        self.scores.append({'name': name, 'score': score})

    def total_score(self, name):
        return sum(player['score'] for player in self.scores if player['name'] == name)

    def get_winner(self):
        if not self.scores:
            return "No players yet"
        return max(self.scores, key=lambda player: player['score'])['name']

    def __str__(self):
        # Sorteer de scores aflopend en formatteer de output
        sorted_scores = sorted(self.scores, key=lambda player: player['score'], reverse=True)
        return "\n".join(f"{player['name']}: {player['score']}" for player in sorted_scores)

    @staticmethod
    def save_to_json(filename, scoreboard):
        with open(filename, 'w') as f:
            json.dump(scoreboard.scores, f, indent=4)

    @staticmethod
    def load_from_json(filename):
        sb = Scoreboard()
        try:
            with open(filename, 'r') as f:
                scores = json.load(f)
                if scores is not None:
                    sb.scores = scores
        except (FileNotFoundError, json.JSONDecodeError):
            # Bestand bestaat niet of is ongeldig, geef een nieuw scorebord terug.
            pass
        return sb
