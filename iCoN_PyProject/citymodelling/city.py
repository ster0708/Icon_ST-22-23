#Classe che ci permette di modellare una generica città. Per il momento contiene solo nome e probabilità calcolata dalla rete bayesiana

class City:
    def __init__(self, nome, prob):
        self.nome: str = nome
        self.prob: float = prob

    def getNome(self):
        return self.nome

    def getProb(self):
        return self.prob
