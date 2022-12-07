from words.config import WORDS_FILE
from words.custom_exceptions import GameOver
from words.data_reader import CSVGetter
from words.game_process import GameProcess


def play():
    data_reader = CSVGetter(WORDS_FILE)
    game = GameProcess(data_reader)
    game.play()


if __name__ == '__main__':
    while True:
        try:
            play()
        except GameOver as err:
            print(f'You completed {err.score} words')
            y = input('Enter: Y if you want to try again')
            if y.lower() != 'y':
                break
