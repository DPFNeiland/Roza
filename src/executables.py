import os, webbrowser


## Some applications
def open_youtube():
    os.system("start https://youtube.com")

def open_edge():
    os.system("start msedge")

def open_vscode():
    os.system("code")

def open_browser_and_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def dev_mode():
    os.system("start msedge")
    os.system("code")
    webbrowser.open("https://stackoverflow.com")


## Some workstations
def study_mode():
    print("Starting study mode...")
    
    os.system("code")  # VS Code
    webbrowser.open("https://codeforces.com")
    webbrowser.open("https://www.beecrowd.com.br")
    webbrowser.open("https://youtube.com")

def video_mode():
    print("Opening YouTube...")
    webbrowser.open("https://youtube.com")

def search(query):
    print(f"Searching for: {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

