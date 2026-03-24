from actions.system import open_vscode
from actions.browser import open_youtube
import webbrowser

def study_mode():
    open_vscode()
    webbrowser.open("https://codeforces.com")
    webbrowser.open("https://www.beecrowd.com.br")
    open_youtube()
