from unittest import TestCase

from words.custom_exceptions import GameOver, WordCompleted
from words.game_process import GameProcess


class FakeReader:
    def get_random_word(self):
        return "test"


class GameProcessTestCase(TestCase):
    """
    run tests -> setUp() -> test_game_process_init() -> tearDown() -> setUp() -> ...
    """

    def setUp(self) -> None:
        self.game_process = GameProcess(
            FakeReader()
        )

    def test_game_process_init(self):
        self.assertEqual(self.game_process.word, "test")

    def test_hidden_word_shows_asterisks_only(self):
        """
        1 step - initialize game process
        2 step - call method
        3 step - assertion
        """
        self.assertEqual(self.game_process.hidden_word, '*' * 4)

    def test_hidden_word_shows_asterisks_and_letters(self):
        """
        1 step - initialize game process
        2 step - call method
        3 step - assertion
        """
        self.game_process.used_letters = ['t']
        self.assertEqual(self.game_process.hidden_word, 't**t')
        # assert game_process.hidden_word == 't**t'

    def test_stop_game_raise_exception(self):
        with self.assertRaises(GameOver):
            self.game_process.stop_game()

    def test_validate_letter_non_alpha_character(self):
        self.assertIsNone(self.game_process.validate_letter("45"))

    def test_validate_letter_already_used_letters(self):
        self.game_process.used_letters.append("p")
        self.assertIsNone(self.game_process.validate_letter("p"))

    def test_validate_letter_correct_letter(self):
        used_letters_before = len(self.game_process.used_letters)
        self.game_process.validate_letter('e')
        used_letters_after = len(self.game_process.used_letters)
        self.assertGreater(used_letters_after, used_letters_before)
        self.assertEqual(self.game_process.hidden_word, '*e**')

    def test_validate_letter_word_complete(self):
        self.game_process.used_letters = ['t', 's']
        with self.assertRaises(WordCompleted):
            self.game_process.validate_letter('e')

    def test_validate_letter_incorrect_letter(self):
        tries_before = self.game_process.tries
        self.game_process.validate_letter("q")
        tries_after = self.game_process.tries

        self.assertLess(tries_after, tries_before)
        self.assertIn('q', self.game_process.used_letters)

    def test_validate_letter_raise_game_over(self):
        self.game_process.tries = 1
        with self.assertRaises(GameOver):
            self.game_process.validate_letter("m")
