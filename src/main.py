import commands

while True:
    user = input(">>> ").lower()

    if user in ["exit", "quit"]:
        break

    found = False

    for keys, func in commands.commands.items():
        if any(k in user for k in keys):
            func()
            found = True
            break

    if not found:
        if user.startswith("search"):
            query = user.replace("search", "").strip()
            from executables import search
            search(query)
        else:
            print("Unknown command")