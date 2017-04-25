import pygame

pygame.mixer.pre_init(frequency=16000, size=-16, channels=2)
pygame.mixer.init()
pygame.mixer.music.load("sample.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
