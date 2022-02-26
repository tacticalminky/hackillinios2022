class Item:
    name = ""
    x = 0
    y = 0
    w = 0
    h = 0
    time = 0
    missing = 0
    def __init__(item, name, x, y, w, h):
        item.name = name
        item.x = x
        item.y = y
        item.w = w
        item.h = h
        item.time = 0
        item.missing = 0

trash = [Item]
total = 0
total_paper = 0
total_plastic = 0
total_garbage = 0

def AddTrash(name, x, y, w, h):
    for item in trash:
        if ((item.name == name) and (50 > (abs(abs(x - (w / 2)) - abs(item.x - (item.w / 2))))) and (50 > (abs(abs(y - (h / 2)) - abs(item.y - (item.h / 2)))))):
            item.x = x
            item.y = y
            item.w = w
            item.h = h
            item.time = item.time + 1
            item.missing = 0
            return
    trash.append(Item(name, x, y, w, h))
    Add(name)
            

def GetItems(time):
    toReturn = [Item]
    for item in trash:
        if item.time >= time:
            toReturn.append(item)
    return toReturn

def Sort():
    for item in trash:
        if item.missing > 10:
            trash.remove(item)
        item.missing = item.missing + 1
    if (len(trash) == 0 ):
        AddTrash("empty", 0, 0, 0, 0)

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