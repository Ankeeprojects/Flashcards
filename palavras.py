import pandas
import random

class Palavras:
    def __init__(self, ficheiro):
        try:
            dataframe = pandas.read_csv(ficheiro)
        except FileNotFoundError:
            dataframe = pandas.read_csv("data/french_words.csv")

        self.dicionario = dataframe.to_dict(orient="records")
        self.palavra = random.choice(self.dicionario)
        self.ficheiro = ficheiro

    def acertou(self):
        self.dicionario.remove(self.palavra)

        data = pandas.DataFrame(self.dicionario)
        data.to_csv(self.ficheiro)

        self.palavra = random.choice(self.dicionario)


    def falhou(self):
        self.palavra = random.choice(list(self.dicionario))