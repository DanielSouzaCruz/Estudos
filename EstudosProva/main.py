# from Carro import Carro
#
# if __name__ == '__main__':
#
#     carro1 = Carro('Hyundai','Creta', '433-444',100,4,4);
#
#     carro1.to_string()
#     print(carro1.get_velocidade_maxima())

from Pessoa import Pessoa
from Gerente import Gerente
from Funcionario import Funcionario
from Trabalhador import Trabalhador
if __name__ == '__main__':
    g1 = Gerente('Paulo','222222222','Administrativo');
    f1 = Funcionario('Luis','3333333','Rh');
    p1 = Pessoa('Ana','1111111')
    t1 = Trabalhador('teste','22222','adm','auxiliar')
    p1.to_string();
    f1.to_string();
    g1.to_string();
    t1.to_string();