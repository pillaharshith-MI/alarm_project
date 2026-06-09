import pygame
import time
import datetime

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("Wake up! It's time!")

            pygame.mixer.init()
            pygame.mixer.music.load("alarm_sound.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

set_alarm()