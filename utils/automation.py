import webbrowser
import os

def handle_automation(query):
    query = query.lower()

    commands = {
        "open youtube": lambda: webbrowser.open("https://youtube.com"),
        "open google": lambda: webbrowser.open("https://google.com"),
        "open gmail": lambda: webbrowser.open("https://mail.google.com"),
        "open facebook": lambda: webbrowser.open("https://facebook.com"),
        "open instagram": lambda: webbrowser.open("https://instagram.com"),
        "open linkedin": lambda: webbrowser.open("https://linkedin.com"),
        "open github": lambda: webbrowser.open("https://github.com"),
        "open stackoverflow": lambda: webbrowser.open("https://stackoverflow.com"),
        "open whatsapp web": lambda: webbrowser.open("https://web.whatsapp.com"),
        "open twitter": lambda: webbrowser.open("https://twitter.com"),
    }

    for command in commands:
        if command in query:
            commands[command]()
            return f"Executing: {command}"

# 💬 Basic chat responses
    chat_responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! I'm your AI assistant.",
        "hey": "Hey! Ready to assist you.",
        "how are you": "I'm doing great! Thanks for asking 😊",
        "your name": "I'm your AI voice assistant.",
        "who are you": "I'm an AI assistant built to help you like ChatGPT.",
        "good morning": "Good morning! Have a productive day",
        "good night": "Good night! Sleep well 🌙",
        "thank you": "You're welcome! 😊",
        "thanks": "Happy to help!",
        "bye": "Goodbye! Take care 👋",
        "love you":"Thank you but i am not human"
    }

    for key in chat_responses:
        if key in query:
            return chat_responses[key]
    
    # 💻 System apps
    system_apps = {
        "open notepad": "notepad",
        "open calculator": "calc",
        "open paint": "mspaint",
        "open cmd": "cmd",
        "open file explorer": "explorer"
    }

    for app in system_apps:
        if app in query:
            os.system(system_apps[app])
            return f"Opening {app}"


    # 📂 Folders
    if "open downloads" in query:
        os.startfile(os.path.expanduser("~/Downloads"))
        return "Opening Downloads folder"

    if "open documents" in query:
        os.startfile(os.path.expanduser("~/Documents"))
        return "Opening Documents folder"

    if "open desktop" in query:
        os.startfile(os.path.expanduser("~/Desktop"))
        return "Opening Desktop folder"

    # # ⏰ Time & Date
    # if "time" in query:
    #     return datetime.datetime.now().strftime("Current time is %H:%M:%S")

    # if "date" in query:
    #     return datetime.datetime.now().strftime("Today's date is %d-%m-%Y")

    # if "day" in query:
    #     return datetime.datetime.now().strftime("Today is %A")

    # 🔌 Power control (use carefully)
    if "shutdown" in query:
        os.system("shutdown /s /t 5")
        return "Shutting down system"

    if "restart" in query:
        os.system("shutdown /r /t 5")
        return "Restarting system"

    if "log off" in query:
        os.system("shutdown -l")
        return "Logging off"

    # 🔍 Quick Google search
    if "search" in query:
        search = query.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search}")
        return f"Searching for {search}"

    # ▶️ YouTube search/play
    if "play" in query:
        song = query.replace("play", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        return f"Playing {song} on YouTube"
    
    return None