import tts.sapi
import words as w
import subprocess
import os
import tkinter as Tk

# initialization
voice = tts.sapi.Sapi()  # voice module load
osk = os.path.abspath(os.path.join('.', 'OSKeyboard.bat'))
print(osk)
cmd_path = "C:\\Program Files\\Common Files\\Microsoft Shared\\ink\\TabTip.exe"
keyboard_process = subprocess.Popen([cmd_path], shell=True)

# voice.set_voice("Anna")
# voice.create_recording('output.wav', "This will be in a wav file")
# voice.set_rate(1)
# voice.say("This will be said faster")

word_count = 0


def main():
    active = True
    use_counter = 0  # counts the times the script's run. on reset, it dumps the words into saved word list.

    while active:
        # actual text to speech
        input_text = input("Type your words here!\n>>> ")
        voice.say(input_text)

        # save the words
        wordlist = input_text.split()  # without a delimiter, it splits at whitespaces, like spaces har har.
        for word in wordlist:
            word = w.clean(word)  # removes anything that isnt a letter
            w.add(word)
        w.dump()

        # for testing
        # print(w.wh.word_list)  # dont uncomment unless u want spam.
        # print(w.wh.get_top_words())


if __name__ == '__main__':
    main()
