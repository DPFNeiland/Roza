import commands
from actions.shortcuts import create_shortcut

while True:
    user = input(">>> ").lower()

    if user in ["exit", "quit"]:
        break

    if user.startswith("create shortcut"):
            name = user.replace("create shortcut", "").strip()
            create_shortcut(name)
            
            continue
    

    for keys, func in commands.commands.items():
        if any(k in user.split() for k in keys):
            func()
            break
    else:
        print("Unknown command")