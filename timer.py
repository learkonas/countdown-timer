import time
import pygame
import keyboard
import threading
import os

sound_files = os.listdir("sounds")                            ## checking the appropriate wav files are included
num_sound_files = len(sound_files) -2                               # exclude the 0.wav and cannon.wav files
sound_files = [file[:-4] for file in sound_files]                   # to remove the '.wav' file ending
sound_files = [int(file) for file in sound_files if file.isdigit()] # remove the 'cannon' item and return an array of integers
sound_files.sort()                                                  # sort the integers in ascending order
for i in range(len(sound_files)-1):
    if sound_files[i+1] - sound_files[i] != 1:
        print(f"Warning: you may lack a {sound_files[i+1]-1}.wav sound file. Please check the /sounds/ folder.")
        continue_status = input("Enter 'n' to stop and enter anything else to continue: ")
        if continue_status == 'n':
            exit()

base_countdown = 0
while base_countdown <= 0 or base_countdown > 20:
    try:
        base_countdown = int(input("\nHow many seconds would you like for each turn?\n")) #  https://evolution.voxeo.com/library/audio/prompts/numbers/index.jsp
    except:
        print(f"Please enter a number between 0 and {num_sound_files}.")

pygame.mixer.init()
sound = {i: pygame.mixer.Sound(f"sounds\{i}.wav") for i in range(base_countdown+1)}
start = pygame.mixer.Sound("sounds\cannon.wav")

countdown_lock = threading.Lock()
need_to_stop = False

print(f"\n\nPrepare to play!")
countdown = 10
while countdown > 0:
    sound[countdown].play() 
    countdown -= 1  
    time.sleep(1) 
start.play() 
time.sleep(1) 

countdown = base_countdown
print(f"\nGame starting with a {countdown} second timer.\n")
def countdown_timer():
    global countdown
    global need_to_stop

    while countdown > 0:
        if need_to_stop == True:
            exit()
        with countdown_lock:  # Ensure thread safety
            seconds = countdown

        if seconds % 2 == 0:
            print(f"{seconds} seconds remaining...")
        elif seconds == 1:
            print("1 second remaining!!")
        else:
            print(f"{seconds} seconds remaining....")
        sound[seconds].play()  # Play the corresponding sound
        time.sleep(1)  # Wait one second
        with countdown_lock:  # Decrement in a thread-safe manner
            countdown -= 1

    sound[0].play()  # Play final sound when countdown reaches zero
    print("No time left!")
    time.sleep(3)  # Wait before restarting or exiting
    exit()

# Function to reset the countdown when any key is pressed
def reset_on_key_press(event):
    global countdown
    global need_to_stop

    if keyboard.is_pressed("tab"):
        need_to_stop = True
        countdown_thread.join()
    else:
        with countdown_lock:  # Ensure thread safety
            if countdown == 1:
                print("Timer reset with ONE SECOND remaining!!!")
            else:
                if countdown < base_countdown:
                    print(f"Timer reset with {countdown} seconds remaining.\n")
            if countdown < base_countdown:
                countdown = base_countdown + 1  # Reset the countdown
    time.sleep(0.3)

keyboard.hook(reset_on_key_press)  # This listens for any key press

countdown_thread = threading.Thread(target=countdown_timer)
countdown_thread.start() 
countdown_thread.join()