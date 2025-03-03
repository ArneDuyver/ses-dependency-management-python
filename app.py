import random
from libs.scorebord import Scoreboard

def main():
    # Laad het scorebord vanuit het JSON-bestand (als het bestaat)
    sb = Scoreboard.load_from_json('highscores.json')
    
    print("Welcome to the Higher or Lower game!")
    print("This is the current leaderboard:\n", sb, "\n")
    print("Guess if the next number will be higher or lower.")
    
    current_number = random.randint(1, 100)
    score = 0
    playing = True

    while playing:
        print("Current number:", current_number)
        guess = input("Will the next number be higher or lower? (h/l): ").lower().strip()
        next_number = random.randint(1, 100)
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            print("Correct! The next number was:", next_number)
            score += 1
        else:
            print("Wrong! The next number was:", next_number)
            playing = False
        current_number = next_number

    print("Game over! Your final score:", score)
    name = input("What is your name? ")
    sb.add(name, score)
    print("This is the new leaderboard:\n", sb, "\n")
    Scoreboard.save_to_json('highscores.json', sb)

if __name__ == '__main__':
    main()