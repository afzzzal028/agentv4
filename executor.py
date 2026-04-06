import os
import webbrowser

def execute(command):
    cmd = command.lower()

    if "open chrome" in cmd:
        webbrowser.open("https://google.com")
        return "Opened Chrome"

    if "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
        return "Opened YouTube"

    if "open notepad" in cmd:
        os.system("notepad")
        return "Opened Notepad"

    return None