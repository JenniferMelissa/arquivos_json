
#importar dataclass
from dataclasses import dataclass 

#criar classe pessoa
#definindo @dataclass eles nao precisa fazer o getter e setter pois ja vem definido e os atributos ja ficam como private
#dataclass so funciona com o python mais recente

@dataclass
class Pessoa:
    codigo:    int #private
    nome:      str #private
    cpf:       str #private
    email:     str #private
    profissao: str #private

    #destrutor 
    def __del__(self):
        return f'O objeto {self.nome} de código {self.codigo} foi destruido.'