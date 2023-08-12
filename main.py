# write your code here
def print_game(symbols):
    print("---------")
    for i in range(0, 7, 3):
        print(f"| {symbols[i]} {symbols[i+1]} {symbols[i+2]} |")
    print("---------")
symbols = list("         ")
print_game(symbols)
finish = False
for i in range(9):
    while not finish:
        pos_1, pos_2 = list(input().split(" "))
        if pos_1.isdigit() and pos_2.isdigit():  # Both characters are numbers.
            if int(pos_1) > 3 or int(pos_2) > 3:
                print("Coordinates should be from 1 to 3!")
            else:  # Both numbers are between 1 and 3.
                indice = (int(pos_1) - 1) * 3 + (int(pos_2) - 1)
                elemento = symbols[indice]
                if elemento == " " or elemento == "_":
                    if i % 2 == 0:
                        symbols[indice] = "X"
                    else:
                        symbols[indice] = "O"
                    ls = [symbols[0] + symbols[1] + symbols[2], symbols[3] + symbols[4] + symbols[5],
                          symbols[6] + symbols[7] + symbols[8], symbols[0] + symbols[3] + symbols[6],
                          symbols[1] + symbols[4] + symbols[7], symbols[2] + symbols[5] + symbols[8],
                          symbols[0] + symbols[4] + symbols[8], symbols[6] + symbols[4] + symbols[2]]
                    print_game(symbols)
                    if ("XXX" in ls and "OOO" in ls) or abs(symbols.count("X") - symbols.count("O")) >= 2:
                        print("Impossible")
                        finish = True
                        break
                    elif "_" not in symbols and " " not in symbols and "XXX" not in ls and "OOO" not in ls:
                        print("Draw")
                        finish = True
                        break
                    elif ("_" in symbols or " " in symbols) and "XXX" not in ls and "OOO" not in ls:
                        # print("Game not finished")
                        break
                    elif "XXX" in ls:
                        print("X wins")
                        finish = True
                        break
                    elif "OOO" in ls:
                        print("O wins")
                        finish = True
                        break
                else:
                    print("This cell is occupied! Choose another one!")
        else:
            print("You should enter numbers!")
    if finish:
        break
