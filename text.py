with open("TEST.md", "r+") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] += " \n "
    f.writelines(lines)