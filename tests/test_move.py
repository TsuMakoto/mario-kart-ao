from .context import mario_kart_ai
import unittest
import pyautogui


class TestMove(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.move = mario_kart_ai.move.Move()

    @classmethod
    def tearDownClass(cls):
        # 入力文字を削除して終了
        pyautogui.hotkey('ctrl', 'u')

    def test_left(self):
        return self.assertEqual('h', TestMove.move.left())

    def test_left_ten_press(self):
        return self.assertEqual('hhhhhhhhhh',
                                TestMove.move.left(press_count=10))

    def test_right(self):
        return self.assertEqual('l', TestMove.move.right())

    def test_right_ten_press(self):
        return self.assertEqual('llllllllll',
                                TestMove.move.right(press_count=10))

    def test_up(self):
        return self.assertEqual('k', TestMove.move.up())

    def test_up_ten_press(self):
        return self.assertEqual('kkkkkkkkkk',
                                TestMove.move.up(press_count=10))

    def test_down(self):
        return self.assertEqual('j', TestMove.move.down())

    def test_down_ten_press(self):
        return self.assertEqual('jjjjjjjjjj',
                                TestMove.move.down(press_count=10))


if __name__ == "__main__":
    unittest.main()
