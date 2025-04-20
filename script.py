import time
from pycaw.pycaw import AudioUtilities
from pycaw.pycaw import IAudioEndpointVolume

def set_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 0, None)
    volume_interface = interface.QueryInterface(IAudioEndpointVolume)
    volume_interface.SetMasterVolumeLevelScalar(volume, None)

def change_volume():
    while True:
        # Установим громкость на 100%
        set_volume(1.0)
        time.sleep(4)  # Громкость держится на 100% в течение 4 секунд
        
        # Снизим громкость до 99%
        set_volume(0.99)
        time.sleep(0.01)  # Поднимемся до 100% через 0.1 секунды

if __name__ == "__main__":
    change_volume()
