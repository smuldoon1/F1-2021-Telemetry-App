def BytesToName(nameBytes):
    name = ""
    for i in range(48):
        if nameBytes[i] == 0:
            break
        name = name + chr(nameBytes[i])
    return name
