import os
from win32com.client import Dispatch


def get_desktop():
    paths = [
        os.path.join(os.environ["USERPROFILE"], "Desktop"),
        os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop")
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    raise Exception("Desktop folder not found")


def create_bat(name, commands):
    desktop = get_desktop()
    bat_path = os.path.join(desktop, f"{name}.bat")

    with open(bat_path, "w") as f:  # always overwrite
        f.write("\n".join(commands))

    os.system(f'attrib +h "{bat_path}"')

    return bat_path


def create_lnk(name, bat_path, icon_path=None):
    desktop = get_desktop()
    lnk_path = os.path.join(desktop, f"{name}.lnk")

    if os.path.exists(lnk_path):
        os.remove(lnk_path)

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_path)

    shortcut.Targetpath = bat_path
    shortcut.WorkingDirectory = desktop

    if icon_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        full_icon_path = os.path.join(base_dir, icon_path)

        full_icon_path = os.path.abspath(full_icon_path)

        if os.path.exists(full_icon_path):
            shortcut.IconLocation = full_icon_path + ",0"
            print("ICON OK:", full_icon_path)
        else:
            print("❌ Icon not found:", full_icon_path)

    shortcut.save()


def create_shortcut(name):
    presets = {
        "study": [
            "start code",
            "start https://codeforces.com",
            "start https://www.beecrowd.com.br",
            "start https://youtube.com"
        ],
        "dev": [
            "start code",
            "start https://stackoverflow.com"
        ],
        "youtube": [
            "start https://youtube.com"
        ]
    }

    if name not in presets:
        print("Unknown shortcut preset")
        return

    bat_path = create_bat(name, presets[name])

    icon_path = "imgs/icon.ico"

    create_lnk(name, bat_path, icon_path)

    print(f"{name} shortcut created on Desktop")
