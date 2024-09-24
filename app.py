#ideia deste projeto: criar objeto (Pessoa) e iremos manipula-lo e ao final iremos gravar esses dados no .json e ele vai listar os dados do .json em nosso programa

#importacoes
import os
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    #instanciar Pessoa
    p = Pessoa(0,'','','','')

    #instanciar Manipulador
    m = Manipulador()

    while True:
        print('1 - Criar novo arquivo JSON')
        print('2 - Abrir e ler arquivo JSON')
        print('3 - Salvar novo usuário')
        print('0 - Sair do programa')

        opcao = input('Informe opção desejada: ')

        #limpar o console
        os.system('cls')

        match opcao:
            case '0':
                print('Programa encerrado.')
                break

            case '1':
                novo_arquivo = input('Informe o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continue

            case '2':
                    abrir_arquivo = input('Informe o nome do arquivo que deseja abrir: ')
                    try:
                        os.system('cls')
                        usuarios = m.abrir_arquivo(abrir_arquivo)
                        print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                        for i in range(len(usuarios)):
                            for campo in usuarios[i]:
                                print(f'{campo.capitalize()}: {usuarios[i].get(campo)}.')
                            print(f'\n{'-'*30}\n')

                    except Exception as e:
                        print(f'Não foi possível abrir o arquivo. {e}.')
                    
                    finally: #é executado apos o try ou except, nao faz diferenca, mas sempre é executado
                        continue
            
            case '3':
                try:
                    usuario = {} #dicionario
                    campos = ('nome','cpf','email','profissao')  #tupla
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    usuario['codigo'] = len(usuarios)
                    for campo in campos:
                        usuario[campo] = input(f'Informe o campo {campo.capitalize()}: ')   ''
                        usuarios.append(usuario)
                        print(m.salvar_dados(usuarios, abrir_arquivo))

                except Exception as e:
                    print(f'Não foi possível realizar a operação. {e}.')

                finally:
                    continue

            case _:
                print('Opção inválida.')
                continue