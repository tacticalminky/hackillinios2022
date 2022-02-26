class Item:
    name = ""
    x = 0
    y = 0
    time = 0
    missing = 0
    def __init__(item, name, x, y):
        item.name = name
        item.x = x
        item.y = y
        item.time = 0
        item.missing = 0

trash = [Item]
total = 0
total_paper = 0
total_plastic = 0
total_garbage = 0

def AddTrash(name, x, y):
    for item in trash:
        if item.name is name:
            if (20 > abs(abs(x) - abs(item.x)) and 20 > abs(abs(y) - abs(item.y))):
                item.x = x
                item.y = y
                item.time = item.time + 1
                item.missing = 0
            else:
                trash.append(Item(name, x, y))
                Add(name)

        else:
            trash.append(Item(name, x, y))
            Add(name)

def GetItems(time):
    toReturn = [Item]
    for item in trash:
        if item.time >= time:
            toReturn.append(item)
    return toReturn

def Sort():
    for item in trash:
        if item.missing > 10 and len(trash) > 1:
            trash.remove(item)
        item.missing = item.missing + 1

def GetBin():
    if trash[0].name == "paper":
        return 0
    elif trash[0].name == "plastic":
        return 1
    else:
        return 2

def Add(name):
    global total_paper, total_garbage, total_plastic, total
    if name == "paper":
        total_paper = total_paper + 1
    if name == "plastic":
        total_plastic = total_plastic + 1
    if name == "garbage":
        total_garbage = total_garbage + 1
    total = total + 1