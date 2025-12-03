import random
from collections import defaultdict
from os.path import dirname, join, realpath


def vypis_statistiku(seznam):
    if not seznam:
        print("Seznam je prazdny.")
        return

    soucet = sum(seznam)
    nejvetsi = max(seznam)
    nejmensi = min(seznam)
    pocet_parnych = sum(1 for x in seznam if x % 2 == 0)
    pocet_neparnych = sum(1 for x in seznam if x % 2 != 0)
    prumer = soucet / len(seznam)

    print(f"Soucet: {soucet}")
    print(f"Nejvetsi: {nejvetsi}")
    print(f"Nejmensi: {nejmensi}")
    print(f"Pocet sudych: {pocet_parnych}")
    print(f"Pocet lichych: {pocet_neparnych}")
    print(f"Prumer: {prumer}")


def read_nums():
    seznam = []
    while True:
        vstup = input("Piste cisla anebo stop: ")

        if vstup.lower() == "stop":
            break

        try:
            seznam.append(int(vstup))
        except ValueError:
            print("Neplatny vstup, zadejte cislo nebo stop.")

    return seznam

def spocitej_znaky(text):
    text = text.lower()
    znak_count = defaultdict(int)
    for znak in text:
        if znak !=' ':
            znak_count[znak]+=1
    return dict(znak_count)

def pridej_studenta(seznam, jmeno, znamky):
    seznam.append({"jmeno": jmeno, "znamky": znamky})


def nejlepsi_student(seznam_studentu):
    if not seznam_studentu:
        print("Seznam studentu je prazdny.")
        return

    nejlepsi = None
    nejlepsi_prumer = float('inf')

    for student in seznam_studentu:
        prumer = sum(student["znamky"]) / len(student["znamky"])
        if prumer < nejlepsi_prumer:
            nejlepsi_prumer = prumer
            nejlepsi = student["jmeno"]

    print(f"Nejlepsi student je {nejlepsi} s prumerem {nejlepsi_prumer:.2f}")

def read_log_file(file_name="system.log"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.readlines()

def errors(lines):
    error_lines = [line for line in lines if "ERROR" in line]
    with open("errors_only.txt", "w") as file:
        file.writelines(error_lines)


def sifruj(text, posun):
    vysledek = ""
    for znak in text:
        if znak.isalpha():
            start = ord('A') if znak.isupper() else ord('a')
            novy_znak = chr(start + (ord(znak) - start + posun) % 26)
            vysledek += novy_znak
        else:
            vysledek += znak
    return vysledek

def main():
    cisla = read_nums()
    vypis_statistiku(cisla)

    text = input("Zadejte text pro spocitej_znaky: ")
    vysledek = spocitej_znaky(text)
    print("Počet výskytů znaků:", vysledek)

    studenti = []
    pridej_studenta(studenti, "Jan", [1, 2, 3])
    pridej_studenta(studenti, "Eva", [1, 1, 2])
    pridej_studenta(studenti, "Petr", [2, 3, 2])
    nejlepsi_student(studenti)

    log_lines = read_log_file()
    errors(log_lines)

    sifrovany_text = sifruj("AbC jKl!", 3)
    print(sifrovany_text)




if __name__ == "__main__":
    main()
