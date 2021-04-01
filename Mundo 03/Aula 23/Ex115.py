import Modulos


print('1 - Pessoas cadastradas')
print('2 - Cadastrar nova Pessoa')
print('3 - Sair do Sistema')
print('-' * 40)
opcao = int(input('Selecione sua Opção: '))

if opcao == 1:
    print(Modulos.pessoasCadastradas())
elif opcao == 2:
    print(Modulos.cadastrarPessoas())
elif opcao == 3:
    print('Sistema finalizado!')
