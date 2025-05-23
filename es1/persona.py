class Persona:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.voti = []

    def aggiungi_voto(self, voto): 
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print("voto non valido")

    def media_voti(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti) / len(self.voti)

    def print_nome(self):
        print(self.nome)
        print(self.classe)
        print(self.media_voti())
        