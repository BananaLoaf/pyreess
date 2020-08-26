import argparse

from pyreess import DESCRIPTION
from pyreess.generator import Generator

import pyperclip


LENGTH = "LENGTH"

DIGITS = "DIGITS"
LOWERCASE = "LOWERCASE"
UPPERCASE = "UPPERCASE"
SYMBOLS = "SYMBOLS"

SHOW = "SHOW"


def ask(message: str, pos: str = "y", neg: str = "n"):
    while True:
        resp = input(message + " [y/n] ").lower()
        if resp == pos:
            return True
        elif resp == neg:
            return False


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-len", type=int, default=15, help="Output length (default: %(default)s)", dest=LENGTH)
    parser.add_argument("-sh", type=int, default=3,
                        help="Length of shown output. If negative, output will be fully shown (default: %(default)s)", dest=SHOW)

    alphabet_group = parser.add_argument_group("Alphabet settings")
    alphabet_group.add_argument("-d", action="store_true", help="Use digits", dest=DIGITS)
    alphabet_group.add_argument("-l", action="store_true", help="Use lowercase", dest=LOWERCASE)
    alphabet_group.add_argument("-u", action="store_true", help="Use uppercase", dest=UPPERCASE)
    alphabet_group.add_argument("-s", action="store_true", help="Use symbols", dest=SYMBOLS)

    args = parser.parse_args()

    ################################################################
    length = getattr(args, LENGTH)
    show = getattr(args, SHOW)
    if show > length or show < 0:
        show = length

    digits = getattr(args, DIGITS)
    lowercase = getattr(args, LOWERCASE)
    uppercase = getattr(args, UPPERCASE)
    symbols = getattr(args, SYMBOLS)
    if not (digits or lowercase or uppercase or symbols):
        parser.print_help()
        parser.error("At least one alphabet related flag in required!")

    ################################################################
    source = input("Input string: ")
    if not source:
        print("Empty input string!")
        raise KeyboardInterrupt

    salt = input("Salt: ")
    if not (source or salt):
        print("Empty input string or salt!")
        raise KeyboardInterrupt

    gen = Generator(source=source.encode("utf-8"), salt=salt.encode("utf-8"))
    gen.set_rules(digits=digits,
                  lowercase=lowercase,
                  uppercase=uppercase,
                  symbols=symbols)
    output = gen.generate(length=length)

    ################################################################
    print("----------------")
    print("Output:")
    print(output[:show] + "*" * (len(output) - show))

    print("----------------")
    if ask("Copy output to the clipboard?"):
        pyperclip.copy(output)
        print("Done!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
