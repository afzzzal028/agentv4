import os

def execute(cmd):
    if "notepad" in cmd:
        os.system("notepad")
        return "Opened Notepad"

    if "chrome" in cmd:
        os.system("start chrome")
        return "Opened Chrome"

    return "Unknown command"