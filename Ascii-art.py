import os
import msvcrt
from colorama import Fore, init

init(autoreset=True)

# ---------------- COLORS ----------------
COLORS = {
    '1': Fore.RED,
    '2': Fore.GREEN,
    '3': Fore.YELLOW,
    '4': Fore.BLUE,
    '5': Fore.MAGENTA,
    '6': Fore.CYAN,
    '7': Fore.WHITE
}

# ---------------- ASCII FONT ----------------
ASCII_FONT = {
    'A': ["  ***  ", " *   * ", " ***** ", " *   * ", " *   * "],
    'B': [" ****  ", " *   * ", " ****  ", " *   * ", " ****  "],
    'C': ["  **** ", " *     ", " *     ", " *     ", "  **** "],
    'D': [" ****  ", " *   * ", " *   * ", " *   * ", " ****  "],
    'E': [" ***** ", " *     ", " ****  ", " *     ", " ***** "],
    'F': [" ***** ", " *     ", " ****  ", " *     ", " *     "],
    'G': ["  **** ", " *     ", " *  ** ", " *   * ", "  **** "],
    'H': [" *   * ", " *   * ", " ***** ", " *   * ", " *   * "],
    'I': [" ***** ", "   *   ", "   *   ", "   *   ", " ***** "],
    'J': ["   *** ", "    *  ", "    *  ", " *  *  ", "  **   "],
    'K': [" *   * ", " *  *  ", " ***   ", " *  *  ", " *   * "],
    'L': [" *     ", " *     ", " *     ", " *     ", " ***** "],
    'M': [" *   * ", " ** ** ", " * * * ", " *   * ", " *   * "],
    'N': [" *   * ", " **  * ", " * * * ", " *  ** ", " *   * "],
    'O': ["  ***  ", " *   * ", " *   * ", " *   * ", "  ***  "],
    'P': [" ****  ", " *   * ", " ****  ", " *     ", " *     "],
    'Q': ["  ***  ", " *   * ", " *   * ", " *  ** ", "  **** "],
    'R': [" ****  ", " *   * ", " ****  ", " *  *  ", " *   * "],
    'S': ["  **** ", " *     ", "  ***  ", "     * ", " ****  "],
    'T': [" ***** ", "   *   ", "   *   ", "   *   ", "   *   "],
    'U': [" *   * ", " *   * ", " *   * ", " *   * ", "  ***  "],
    'V': [" *   * ", " *   * ", " *   * ", "  * *  ", "   *   "],
    'W': [" *   * ", " *   * ", " * * * ", " ** ** ", " *   * "],
    'X': [" *   * ", "  * *  ", "   *   ", "  * *  ", " *   * "],
    'Y': [" *   * ", "  * *  ", "   *   ", "   *   ", "   *   "],
    'Z': [" ***** ", "    *  ", "   *   ", "  *    ", " ***** "],

    '0': ["  ***  ", " *   * ", " *   * ", " *   * ", "  ***  "],
    '1': ["   *   ", "  **   ", "   *   ", "   *   ", " ***** "],
    '2': ["  ***  ", " *   * ", "   **  ", "  *    ", " ***** "],
    '3': [" ****  ", "     * ", "  ***  ", "     * ", " ****  "],
    '4': [" *  *  ", " *  *  ", " ***** ", "    *  ", "    *  "],
    '5': [" ***** ", " *     ", " ****  ", "     * ", " ****  "],
    '6': ["  ***  ", " *     ", " ****  ", " *   * ", "  ***  "],
    '7': [" ***** ", "    *  ", "   *   ", "  *    ", "  *    "],
    '8': ["  ***  ", " *   * ", "  ***  ", " *   * ", "  ***  "],
    '9': ["  ***  ", " *   * ", "  **** ", "     * ", "  ***  "],

    ' ': ["       ", "       ", "       ", "       ", "       "]
}

# ---------------- LOGOS ----------------
HEART = [
    " **   ** ",
    "**** ****",
    " ********",
    "  ****** ",
    "   ****  ",
    "    **   "
]

SMILE = [
    "    *****  ",
    " *         * ",
    "*   *   *   *",
    "*           *",
    "*   *****   *",
    " *         * ",
    "    *****  "
]


def clear():
    os.system('cls')

def pause():
    print("\nPress any key to continue...")
    msvcrt.getch()

def choose_color():
    clear()
    print("Choose Color:\n")
    print("1. Red\n2. Green\n3. Yellow\n4. Blue\n5. Magenta\n6. Cyan\n7. White")
    key = msvcrt.getch().decode(errors="ignore")
    return COLORS.get(key, Fore.WHITE)

def print_ascii(text, color):
    for row in range(5):
        for ch in text.upper():
            print(color + ASCII_FONT.get(ch, ASCII_FONT[' '])[row], end="  ")
        print()

def print_logo(logo, color):
    for line in logo:
        print(color + line)

# ---------------- MODES ----------------
def single_character():
    ch = input("Enter one character: ")
    if len(ch) != 1:
        print("Only ONE character allowed!")
        return
    print_ascii(ch, choose_color())

def words_mode():
    text = input("Enter word(s): ")
    if not text.replace(" ", "").isalpha():
        print("Only alphabets allowed!")
        return
    print_ascii(text, choose_color())

def numbers_mode():
    text = input("Enter numbers: ")
    if not text.isdigit():
        print("Only numbers allowed!")
        return
    print_ascii(text, choose_color())

# ---------------- MENU ----------------
def main_menu():
    while True:
        clear()
        print("ASCII ART GENERATOR\n")
        print("1. Single Character")
        print("2. Words")
        print("3. Numbers")
        print("4. Heart Logo")
        print("5. Smile Logo")
        print("6. Exit\n")
        print("Press a key (1-6)...")

        choice = msvcrt.getch().decode(errors="ignore")
        clear()

        if choice == '1':
            single_character()
        elif choice == '2':
            words_mode()
        elif choice == '3':
            numbers_mode()
        elif choice == '4':
            print_logo(HEART, choose_color())
        elif choice == '5':
            print_logo(SMILE, choose_color())
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

        pause()

# ---------------- START ----------------
if __name__ == "__main__":
    main_menu()
