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
        print('4 - Alterar dados do usuário')
        print('5 - Deletar usuário')
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
                    # usuario = {} #dicionario
                    # campos = ('nome','cpf','email','profissao')  #tupla
                    # print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    # usuario['codigo'] = len(usuarios)
                    # for campo in campos:
                    #     usuario[campo] = input(f'Informe o campo {campo.capitalize()}: ')   
                    #     usuarios.append(usuario)
                    #     print(m.salvar_dados(usuarios, abrir_arquivo))

                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    p.codigo    = len(usuarios)
                    p.nome      = input('Informe o nome: ')
                    p.cpf       = input('Informe o CPF: ')
                    p.email     = input('Informe o e-mail: ')
                    p.profissao = input('Informe a profissão: ')
                    #dict = outra forma de criar dicionarios
                    usuario     = dict(codigo = p.codigo, nome = p.nome, cpf = p.cpf, email = p.email, profissao = p.profissao)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))

                except Exception as e:
                    print(f'Não foi possível realizar a operação. {e}.')

                finally:
                    continue
            
            case '4':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    codigo = int(input('Informe o código do usuário que deseja alterar os dados: '))
                    for campo in usuarios[codigo]:
                        print(f'Valor atual do campo: {campo}: {usuarios[codigo].get(campo)}')
                        novo_dado = input(f'Informe o novo dado do campo {campo} ou aperte "Enter" caso deseje mater o mesmo valor: ')
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado
                        else:
                            ...
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                    
                except Exception as e:
                    print('Não foi possível alterar os dados.')
                
                finally:
                    continue

            case '5':   
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.')
                    codigo = int(input('Informe o código do usuário que deseja deletar: '))
                    nome_deletado = usuarios[codigo]['nome']
                    confirmacao = input(f'Deseja deletar o usuário {nome_deletado}? Digite "SIM" para confirmar: ').upper()
                    if confirmacao == 'SIM':
                        del(usuarios[codigo])
                        print(m.salvar_dados(usuarios, abrir_arquivo))
                        print(f'Usuário {nome_deletado} deletado com sucesso.')
                    else:
                        print(f'Usuário {nome_deletado} não foi excluído.')            

                except Exception as e:
                    print(f'Não foi possível deletar o arquivo.')

                finally:
                    continue

            case _:
                print('Opção inválida.')
                continue