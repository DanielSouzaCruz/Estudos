from Gerente import Gerente
from Funcionario import Funcionario


class Trabalhador(Gerente,Funcionario):
    def __init__(self,nome,cpf,setor,cargo):
        super().__init__(nome,cpf,setor,cargo);
        print('trabalhador');