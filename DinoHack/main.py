import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
import time


def isCollide(data):
    for i in range(475, 580):
        for j in range(525, 555):
            if data[i, j] < 200:
                return True
    return False


def hit(key):
    pyautogui.press(key)


if __name__ == "__main__":
    print("Hey boi, game about to start in 3 seconds")
    time.sleep(3)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")

    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(400, 540):
    #     for j in range(500, 560):
    #         data[i, j] = 0
    # image.show()
