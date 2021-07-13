def intro(msg):
    intro = msg
    print()
    print(intro)
    print("-" * len(intro))
    print()

def outro(msg):
    outro = f"End of {msg}"
    print()
    print("-" * len(outro))
    print(outro)
    print("=" * len(outro))
    print()

def display(symbols):
    menu = f"""How do you want to display the {symbols}?
    1) Horizontally
    2) Vertically
    Orientation: """
    orientation = int(input(menu))
    print("-" * 80)
    print(end="\t")
    return orientation

def punctuation():
    # Punctuation
    intro("Hebrew Punctuation")

    orientation = display("Punctuation")
    
    punctuation = ("Maqaf", "Paseq", "Sof Pasuq", "Nun Hafukha")

    if orientation == 1:
        print("\u05BE", punctuation[0], end="\t")
        print("\u05C0", punctuation[1], end="\t")
        print("\u05C3", punctuation[2], end="\t")
        print("\u05C6", punctuation[3])
    elif orientation == 2:
        print("\u05BE", punctuation[0])
        print("\u05C0", punctuation[1])
        print("\u05C3", punctuation[2])
        print("\u05C6", punctuation[3])

    outro("Punctuation")

def hebrew_horiz():
    letters = ("Alef", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin", "Het", "Tet", "Yod",
        "Final Kaf", "Kaf", "Lamed", "Final Mem", "Mem", "Final Nun", "Nun", "Samekh",
        "Ayin", "Final Pe", "Pe", "Final Tsadi", "Tsadi", "Qof", "Resh", "Shin", "Tav")
    # From Alef to Final Nun
    for i in range(16):
        if i < 10:
            print(chr(int("0x05D" + str(i), base=16)), letters[i], end="\t")
        else:
            print(chr(int("0x05D" + chr(55+i), base=16)), letters[i], end="\t")

    # From Nun to Tav
    for i in range(11):
        if i < 10:
            print(chr(int("0x05E" + str(i), base=16)), letters[16+i], end="\t")
        else:
            print(chr(int("0x05E" + chr(55+i), base=16)), letters[16+i], end="\t")

    print()
    
def hebrew_vert():
    letters = ("Alef", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin", "Het", "Tet", "Yod",
        "Final Kaf", "Kaf", "Lamed", "Final Mem", "Mem", "Final Nun", "Nun", "Samekh",
        "Ayin", "Final Pe", "Pe", "Final Tsadi", "Tsadi", "Qof", "Resh", "Shin", "Tav")
    # From Alef to Final Nun
    intro("From Alef to Final Nun")
    for i in range(16):
        if i < 10:
            print(chr(int("0x05D" + str(i), base=16)), letters[i])
        else:
            print(chr(int("0x05D" + chr(55+i), base=16)), letters[i])
    outro("Letters From Aleft to Final Nun")

    # From Nun to Tav
    intro("From Nun to Tav")
    for i in range(11):
        if i < 10:
            print(chr(int("0x05E" + str(i), base=16)), letters[16+i])
        else:
            print(chr(int("0x05E" + chr(55+i), base=16)), letters[16+i])

    outro("Letters From Nun to Tav")
    
def letters():
    intro("Hebrew Letters")

    orientation = display("Letters")

    if orientation == 1: hebrew_horiz()
    elif orientation == 2: hebrew_vert()
            

def punct_lig_horiz():
    punct_lig = ("Yiddish Double Vav", "Yiddish Vav Yod",
                 "Yiddish Double Yod", "Geresh", "Gershayim")

    for i in range(5):
        if i == 0: intro("Hebrew Ligature Yiddish")
        elif i == 3:
            print()
            outro("Hebrew Ligature Yiddish")
            intro("Punctuation")
        print(chr(int("0x05F" + str(i), base=16)), punct_lig[i], end="\t")
        if i == 4:
            print()
            outro("Punctuation")
        
def punct_lig_vert():
    punct_lig = ("Yiddish Double Vav", "Yiddish Vav Yod",
                 "Yiddish Double Yod", "Geresh", "Gershayim")
    # From Yiddish Double Vav to Gershayim
    for i in range(5):
        if i == 0: intro("Hebrew Ligature Yiddish")
        elif i == 3:
            outro("Hebrew Ligature Yiddish")
            intro("Punctuation")
        print(chr(int("0x05F" + str(i), base=16)), punct_lig[i])
        if i == 4: outro("Punctuation")
        
def punct_lig():
    orientation = display("Ligature and Punctuation")
    if orientation == 1: punct_lig_horiz()
    elif orientation == 2: punct_lig_vert()

menu = """What do you want to print?
1) Hebrew Punctuation
2) Hebrew Letters
3) Hebrew Ligature Yiddish
0) Quit
Source: https://en.wikipedia.org/wiki/Unicode_and_HTML_for_the_Hebrew_alphabet
Your choice: """

condition = True
while condition:
    choice = int(input(menu))
    if choice == 1: punctuation()
    elif choice == 2: letters()
    elif choice == 3: punct_lig()
    elif choice == 0: condition = False
    else: print("You have to type 0 or 1 or 2 or 3 otherwise you'll see this message")

    
