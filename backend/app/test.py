from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Saldo:
    valor_cent: int

    @property
    def valor(self):
        return self.valor_cent / 100


transacoes: list[Transacao] = []


class CentroDeCusto:
    def __init__(self, nome):
        self.id = id(self)
        self.nome = nome
        self.saldos: dict[Saldo] = {}


@dataclass
class Transacao:
    remetente: Pessoa
    destinatario: Pessoa
    metadados: dict | None = None
    valor_cent: int


class TransacaoService:
    def realizar_transacao(
        self, remetente: Pessoa, destinatario: Pessoa, valor_cent: int
    ):
        if valor_cent > remetente.saldo.valor_cent:
            raise ValueError("Saldo insuficiente")
        transacao = Transacao(remetente, destinatario, valor_cent)
        transacoes.append(transacao)
        remetente.enviar(valor_cent)
        destinatario.receber(remetente, valor_cent)


class Pessoa:
    def __init__(self, nome, idade, saldo: Saldo):
        self.id = id(self)
        self.nome = nome
        self.idade = idade
        self.saldo = saldo

    def receber(self, pessoa: Pessoa, valor_cent: int):
        self.saldo.valor_cent += valor_cent

    def enviar(self, valor_cent):
        if valor_cent > self.saldo.valor_cent:
            raise ValueError("Saldo insuficiente")

        self.saldo.valor_cent -= valor_cent
