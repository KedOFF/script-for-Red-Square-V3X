import time
import ctypes
from ctypes import wintypes

# Константы виртуальных клавиш громкости
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002

def press_volume_up():
    ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
    ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)

def press_volume_down():
    ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
    ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)

def change_volume():
    while True:
        # Увеличиваем громкость до 100% (на всякий случай несколько раз)
        for _ in range(10):  # 10 шагов вверх
            press_volume_up()
            time.sleep(0.01)
        time.sleep(3)  # Держим громкость
        
        # Уменьшаем на 1 шаг (до 99%)
        press_volume_down()
        time.sleep(0.01)

if __name__ == "__main__":
    change_volume()