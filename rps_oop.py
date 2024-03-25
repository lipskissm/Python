from random import choice
from datetime import datetime

RESULT_WIN = 1
RESULT_TIE = 0
RESULT_LOSS = -1

all_choices = ["rock", "paper", "scissors"]


class GameRound:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.result = None

    @staticmethod
    def game_logic(player_choice, computer_choice):
        game_rules = {
            ("rock", "paper"): RESULT_LOSS,
            ("rock", "scissors"): RESULT_WIN,
            ("paper", "rock"): RESULT_WIN,
            ("paper", "scissors"): RESULT_LOSS,
            ("scissors", "rock"): RESULT_LOSS,
            ("scissors", "paper"): RESULT_WIN,
        }
        if player_choice == computer_choice:
            return RESULT_TIE
        else:
            return game_rules[(player_choice, computer_choice)]
        
    def run(self):
        '''This returns a boolean value, indicating
        if the round is completed (True) or not, 
        if the player decided to quit (False)'''
        while True:
            self.player_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ")

            if self.player_choice == 'q':
                return False

            if self.player_choice not in all_choices:
                print("Invalid choice")
                continue
            else:
                break

        self.computer_choice = choice(all_choices)
        print(f"You chose: {self.player_choice}, computer chose: {self.computer_choice}")

        self.result = GameRound.game_logic(self.player_choice, self.computer_choice)
        return True


class TimedGameRound(GameRound):
    def __init__(self):
        super().__init__()
        self.duration = None
        
    def run(self):
        started_at = datetime.now()
        round_completed = super().run()
        ended_at = datetime.now()
        self.duration = (ended_at - started_at).total_seconds()
        return round_completed


class Game:
    def __init__(self, language='en'):
        self._rounds = []
        if language not in ['lt', 'en']:
            raise ValueError('Unsupported language!')
        self.language = language
    
    def run(self):
        while True:
            round = TimedGameRound()
            completed = round.run()
            if completed:
                self._rounds.append(round)
                self.announce_result(round.result)
            else:
                break
        self.game_summary()
    
    def announce_result(self, result):
        result_messages_en = {
            RESULT_TIE: "It's a tie!",
            RESULT_WIN: "You win!",
            RESULT_LOSS: "You lose!",
        }
        result_messages_lt = {
            RESULT_TIE: "Lygiosios!",
            RESULT_WIN: "Laimėjai!",
            RESULT_LOSS: "Pralaimėjai!",
        }
        if self.language == 'en':
            print(result_messages_en[result])
        elif self.language == 'lt':
            print(result_messages_lt[result])

    def game_summary(self):
        win_count, tie_count, loss_count = 0, 0, 0
        for g in self._rounds:
            if g.result == RESULT_LOSS:
                loss_count += 1
            elif g.result == RESULT_TIE:
                tie_count += 1
            elif g.result == RESULT_WIN:
                win_count += 1
        print(f"Win count: {win_count}, tie count: {tie_count}, loss count: {loss_count}")

        # Longest game round
        game_log_sorted = sorted(self._rounds, key=lambda g: g.duration, reverse=True)
        lr = game_log_sorted[0]
        print(f"Longest round duration: {lr.duration} {lr.player_choice}/{lr.computer_choice}")


game = Game(language='lt')
game.run()