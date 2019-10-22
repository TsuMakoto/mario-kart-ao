from pyautogui import press, moveTo, click
from time import sleep
from .constants import const_move


class Move:
    # initializer
    def __init__(self):
        moveTo(0, 480, 1)
        sleep(0.4)
        click()

# public

    def left(self, press_count=1):
        return self.__exec(const_move.LEFT_KEY, press_count)

    def right(self, press_count=1):
        return self.__exec(const_move.RIGHT_KEY, press_count)

    def up(self, press_count=1):
        return self.__exec(const_move.UP_KEY, press_count)

    def down(self, press_count=1):
        return self.__exec(const_move.DOWN_KEY, press_count)

# private

    # @param direction is gba's move botton that keyboard mapping.
    # @return press botton chapters
    def __exec(self, direction, press_count=1):
        press_btn = ''
        for _ in range(press_count):
            press_btn += direction
            press(direction)
        return press_btn
