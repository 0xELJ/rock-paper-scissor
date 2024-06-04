import unittest
from game import play_round

class TestGame(unittest.TestCase):
    def test_play_round(self):
        self.assertEqual(play_round("rock", "scissor"), "You win!")
        self.assertEqual(play_round("rock", "rock"), "It's a tie!")
        self.assertEqual(play_round("rock", "paper"), "You lose!")
        self.assertEqual(play_round("paper", "rock"), "You win!")
        self.assertEqual(play_round("paper", "paper"), "It's a tie!")
        self.assertEqual(play_round("paper", "scissor"), "You lose!")
        self.assertEqual(play_round("scissor", "paper"), "You win!")
        self.assertEqual(play_round("scissor", "scissor"), "It's a tie!")
        self.assertEqual(play_round("scissor", "rock"), "You lose!")
        self.assertEqual(play_round("invalid", "rock"), "Invalid choice!")

if __name__ == "__main__":
    unittest.main()