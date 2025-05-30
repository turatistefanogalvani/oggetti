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
    def __init__(self, marca, modello, numero_porte, autonomia):
        super().__init__(marca, modello, numero_porte)
        self.autonomia_km = autonomia
    
    def scheda(self):
        return f"Auto Elettrica - Marca: {self.marca}, Modello: {self.modello}, Numero di porte: {self.numero_porte}, Autonomia: {self.autonomia_km} km"

# Oggetti
auto1 = Auto("Fiat", "Panda", 5)
auto_elettrica1 = AutoElettrica("Tesla", "Model 3", 4, 450)

# Output
print(auto1.scheda())  
print(auto_elettrica1.scheda())
