class Telebeler :
    def __init__(self, ad ,tam_elaci, yarim_elaci, adi, elave) :
        self.ad = ad
        self.tam_elaci = tam_elaci
        self.yarim_elaci = yarim_elaci
        self.adi = adi
        self.elave = elave

    def __str__(self):
        return f"{self.ad}, {self.tam_elaci} tam əlaçı, {self.yarim_elaci} yarım əlaçı, {self.adi} adi stipendiya alan uşaq var. {self.elave}"
        
informasiyaTexnologiyalari = Telebeler("Informasiya Texnologiyalarında;","12", "5", "3", "Informasiya texnologiyalarında stipendiya almayan tələbə yoxdur.")
energetikaMuhendisliyi = Telebeler("Energetika Mühəndisliyində","2", "1", "4", "Energetika Mühəndisliyində 4 tələbə stipendiya almir.")
komputerMuhendisliyi = Telebeler("Kompüter Mühəndisliyində","1", "5", "3","Kompüter Mühəndisliyində stipendiya almayan tələbə yoxdur.")
ekologiyaMuhendisliyi = Telebeler("Ekologiya Mühəndisliyində","1", "1", "2","Ekologiya Mühəndisliyində 6 tələbə stipendiya almır.")
meliorasiyaMuhendisliyi = Telebeler("Meliorasiya Mühəndisliyində","1", "0", "4","Meliorasiya Mühəndisliyində 5 tələbə stipendiya almır.")
neqliyyatMuhendisliyi = Telebeler("Nəqliyyat Mühəndisliyində","0", "2", "1","Nəqliyyat Mühəndisliyində 7 tələbə stipendiya almır.")


print(informasiyaTexnologiyalari)
print(energetikaMuhendisliyi)
print(komputerMuhendisliyi)
print(ekologiyaMuhendisliyi)
print(meliorasiyaMuhendisliyi)
print(neqliyyatMuhendisliyi)