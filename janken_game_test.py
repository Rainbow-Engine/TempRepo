import unittest
from unittest.mock import patch
import io
import sys
import janken_game  # 上記のじゃんけんプログラムのファイル名

class JankenGameTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_janken_player_loses(self, mock_input, mock_stdout):
        janken_game.janken()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "あなたの負けです！")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_janken_player_wins(self, mock_input, mock_stdout):
        janken_game.janken()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "あなたの勝ちです！")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_janken_draw(self, mock_input, mock_stdout):
        janken_game.janken()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "引き分けです！")

if __name__ == '__main__':
    unittest.main()