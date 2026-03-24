from actions.browser import open_youtube
from actions.system import open_vscode, open_edge
from actions.study import study_mode

commands = {
    ("youtube", "yt"): open_youtube,
    ("edge", "browser"): open_edge,
    ("vscode", "code"): open_vscode,
    ("study",): study_mode,
}