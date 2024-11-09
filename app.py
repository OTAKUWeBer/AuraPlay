from sources import *
import subprocess
import os

def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.run(['cls'], shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.run(['clear'])

def choose_platform():
    print("Choose a platform to search for your song:")
    print("1. YouTube")
    print("2. Spotify (Requires client ID and secret)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        clear_screen()
        yt()
    elif choice == "2":
        clear_screen()
        spotify()
    else:
        print("Invalid choice. Please try again.")
        choose_platform()

def app():
    choose_platform()

if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        print("\nProgram exited.")
