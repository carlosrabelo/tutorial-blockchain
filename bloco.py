from hashlib import sha256
import json
import time


class Bloco:

    def __init__(self, indice, hashAnterior, carimboDataHora, hash):

        self.indice = indice
        self.hashAnterior = hashAnterior
        self.carimboDataHora = carimboDataHora
        self.hash = hash

    def calcularHash(self):

        bloco_dump = json.dumps(self.__dict__, sort_keys=True)
        bloco_hash = sha256(bloco_dump.encode()).hexdigest()

        return bloco_hash


bloco_inicial = Bloco(0, [], 0, "0")

bloco_inicial.hash = bloco_inicial.calcularHash()

print(json.dumps(bloco_inicial.__dict__, sort_keys=True))
