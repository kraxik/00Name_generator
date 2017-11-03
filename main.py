import sys

from modules import generate_name

def main():
    race = input("Choose race from orc/elf/human/undead/troll: ")
    if (race.lower() == 'orc'):
        name = generate_name.get_name('orc')
    elif (race.lower() == 'elf'):
        name = generate_name.get_name('elf')
    elif (race.lower() == 'human'):
        name = generate_name.get_name('human')
    elif (race.lower() == 'undead'):
        name = generate_name.get_name('undead')
    elif (race.lower() == 'troll'):
        name = generate_name.get_name('troll')
    else:
        print("Incorrectly entered race. Try again!")
        sys.exit(1)

    print("Name: " + name)

if __name__ == "__main__":
    main()