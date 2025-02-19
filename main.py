import speech_recognition as sr
import pyttsx3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame



light = mpimg.imread('light_on.jpg')
temperature=mpimg.imread('temperature.jpg')
song=mpimg.imread('song.png')


# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("Command:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""

# Main function
def main():
    while True:
        command = listen_command()
        if "lights" in command:
            speak("Turning on the lights.")
            plt.imshow(light)
            plt.show()
            # Add code to control lights here
        elif "temperature" in command:
            speak("Setting temperature to 72 degrees Fahrenheit.")
            plt.imshow(temperature)
            plt.show()
            # Add code to control temperature here
        elif "song" in command:
            speak("Playing your favorite music.")
            pygame.mixer.init()
            pygame.mixer.music.load('song.mp3')
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            # Add code to play music here
        elif "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
