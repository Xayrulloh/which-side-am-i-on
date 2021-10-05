import os
class Qayodaman:
    def __init__(self, tomon=None, xolat="toriga"):
        self.tomon = tomon
        self.xolat = xolat

    def qaysi_biri(self):
        while self.tomon != "exit":
            self.tomon = input("Qayoqqa harakatlanmoqchisiz (onga|chapga|orqaga)\nTugatishni hohlasangiz exitni bosing\n").strip().lower()
            while not self.tomon:
                self.tomon = input("Xato kiritdingiz qayta urinib koring \nQayoqqa harakatlanmoqchisiz (onga|chapga|orqaga)\nTugatishni hohlasangiz exitni bosing\n").strip().lower()
                os.system("cls")
            if self.tomon == "onga":
                self.onga_nechta()
                os.system("cls")
            elif self.tomon == "chapga":
                self.chapga_nechta()
                os.system("cls")
            elif self.tomon == "orqaga":
                self.orqaga_nechta()
                os.system("cls")
            elif self.tomon == "exit":
                print(f"siz {self.xolat} qarab turbsiz")

    def onga_nechta(self):
        print(self.xolat, "qarab turbsiz")
        if self.xolat == "toriga":
            nechtaligi = input("necha martda: ")
            while not nechtaligi.isdigit():
                print("Invalid syntax try again")
                nechtaligi = input("necha martda")
            nechtaligi = int(nechtaligi)
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "toriga"
            elif nechtaligi == 1:
                self.xolat = "onga"
            elif nechtaligi == 2:
                self.xolat = "orqaga"
            elif nechtaligi == 3:
                self.xolat = "chapga"
        elif self.xolat == "onga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "onga"
            elif nechtaligi == 1:
                self.xolat = "orqaga"
            elif nechtaligi == 2:
                self.xolat = "chapga"
            elif nechtaligi == 3:
                self.xolat = "toriga"
        elif self.xolat == "orqaga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "orqaga"
            elif nechtaligi == 1:
                self.xolat = "chapga"
            elif nechtaligi == 2:
                self.xolat = "toriga"
            elif nechtaligi == 3:
                self.xolat = "onga"
        elif self.xolat == "chapga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "chapga"
            elif nechtaligi == 1:
                self.xolat = "toriga"
            elif nechtaligi == 2:
                self.xolat = "onga"
            elif nechtaligi == 3:
                self.xolat = "orqaga"

    def chapga_nechta(self):
        print(self.xolat, "qarab turbsiz")
        if self.xolat == "toriga":
            nechtaligi = input("necha martda: ")
            while not nechtaligi.isdigit():
                print("Invalid syntax try again")
                nechtaligi = input("necha martda")
            nechtaligi = int(nechtaligi)
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "toriga"
            elif nechtaligi == 1:
                self.xolat = "chapga"
            elif nechtaligi == 2:
                self.xolat = "orqaga"
            elif nechtaligi == 3:
                self.xolat = "onga"
        elif self.xolat == "onga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "onga"
            elif nechtaligi == 1:
                self.xolat = "toriga"
            elif nechtaligi == 2:
                self.xolat = "chapga"
            elif nechtaligi == 3:
                self.xolat = "orqaga"
        elif self.xolat == "orqaga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "orqaga"
            elif nechtaligi == 1:
                self.xolat = "onga"
            elif nechtaligi == 2:
                self.xolat = "toriga"
            elif nechtaligi == 3:
                self.xolat = "chapga"
        elif self.xolat == "chapga":
            nechtaligi = int(input("necha martda: "))
            while nechtaligi > 4:
                nechtaligi -= 4
            if nechtaligi == 0:
                self.xolat = "chapga"
            elif nechtaligi == 1:
                self.xolat = "orqaga"
            elif nechtaligi == 2:
                self.xolat = "onga"
            elif nechtaligi == 3:
                self.xolat = "toriga"

    def orqaga_nechta(self):
        print(self.xolat, "qarab turbsiz")
        if self.xolat == "toriga":
            nechtaligi = input("necha martda\n")
            while not nechtaligi.isdigit():
                print("Invalid syntax try again")
                nechtaligi = input("necha martda")
            nechtaligi = int(nechtaligi)
            while nechtaligi > 2:
                nechtaligi -= 2
            if nechtaligi == 0:
                self.xolat = "toriga"
            elif nechtaligi == 1:
                self.xolat = "orqaga"
        elif self.xolat == "onga":
            nechtaligi = int(input("necha martda"))
            while nechtaligi > 2:
                nechtaligi -= 2
            if nechtaligi == 0:
                self.xolat = "onga"
            elif nechtaligi == 1:
                self.xolat = "chapga"
        elif self.xolat == "orqaga":
            nechtaligi = int(input("necha martda"))
            while nechtaligi > 2:
                nechtaligi -= 2
            if nechtaligi == 0:
                self.xolat = "orqaga"
            elif nechtaligi == 1:
                self.xolat = "toriga"
        elif self.xolat == "chapga":
            nechtaligi = int(input("necha martda"))
            while nechtaligi > 2:
                nechtaligi -= 2
            if nechtaligi == 0:
                self.xolat = "chapga"
            elif nechtaligi == 1:
                self.xolat = "onga"


qaqqa = Qayodaman()
qaqqa.qaysi_biri()

