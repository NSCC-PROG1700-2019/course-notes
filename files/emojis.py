import sys

emojis = {
    'alien': '\U0001F47D',
    'pumpkin': '\U0001F383',
    'ghost': '\U0001F47B',
    'zombie': '\U0001F9DF',
    'spider': '\U0001F577',
    'bat': '\U0001F987',
    'skull': '\U0001F480',
    'clown': '\U0001F921',
    'poison': '\U0001F571',
    'elf': '\U0001F9DD',
    'witch': '\U0001F9D9',
    'vampire': '\U0001F9DB',
    'spy': '\U0001F575',
    'robot': '\U0001F916',
    'poop': '\U0001F4A9'
}

# print(sys.argv)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("Usage: emojis.py <name>")
            sys.exit(-1)
        else:
            for n in sys.argv[1:]:
                show_emoji(n)
            print()


def show_emoji(name):
    if name in emojis:
        print(emojis[name], end='')


if __name__ == '__main__':
    main()
