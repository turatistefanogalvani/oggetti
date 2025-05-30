class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def scheda(self):
        return f"Veicolo - Marca: {self.marca}, Modello: {self.modello}"

class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        super().__init__(marca, modello)
        self.numero_porte = numero_porte
    
    def scheda(self):
        return f"Auto - Marca: {self.marca}, Modello: {self.modello}, Numero di porte: {self.numero_porte}"

class AutoElettrica(Auto):
    def __init__(self, marca, modello, autonomia):
        super().__init__(marca, modello)
        self.autonomia_km = autonomia
    
    def scheda(self):
        return f"Moto - Marca: {self.marca}, Modello: {self.modello}, Cilindrata: {self.autonomia_km} "
    

    
auto1 = Auto("Fiat", "Panda", 5)
moto1 = AutoElettrica("Yamaha", "MT-07", 100)


print(auto1.scheda())  
print(moto1.scheda())