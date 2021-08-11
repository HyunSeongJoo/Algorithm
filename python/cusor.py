# initString = 'abcd'
# command = ['L', 'PZ', 'L', 'D','R','Ix']
#
# cursor = len(initString)
# for i in command:

InitString2 = "abcd"
InitString = ""
command = ["L", "PZ", "L", "D", "R", "Ix"]
command2 = ["Pa", "Pb", "L", "Ic", "Id"]


def L_command(Cursor: int):
    Cursor -= 1
    if Cursor <= 0:
        Cursor = 0
    return Cursor


def R_command(Cursor: int, stringlength):
    Cursor += 1
    if Cursor >= stringlength:
        Cursor = stringlength
    return Cursor


def D_Command(Cursor: int, message: str):
    a = message[:Cursor - 1] + message[Cursor:]
    Cursor = L_command(Cursor)
    return Cursor, a


def P_Command(Cursor: int, message: str, word):
    a = message[:Cursor] + word + message[Cursor:]
    Cursor = R_command(Cursor, len(a))
    return Cursor, a


def I_Command(Cursor: int, message: str, word):
    if Cursor >= (len(message)):
        P_Command(Cursor, message, word)
    a = message[:Cursor] + word + message[Cursor + 1:]
    Cursor = R_command(Cursor, len(a))
    return Cursor, a


answer = ""
answer = InitString2
cursor = len(answer)
for i in command:
    if len(i) >= 2:
        if i[0] == "I":
            cursor, answer = I_Command(int(cursor), answer, i[1])
        elif i[0] == "P":
            cursor, answer = P_Command(int(cursor), answer, i[1])
    elif i == "D":
        cursor, answer = D_Command(int(cursor), answer)
    elif i == "R":
        cursor = R_command(int(cursor), len(answer))
    elif i == "L":
        cursor = L_command(int(cursor))
print(answer)