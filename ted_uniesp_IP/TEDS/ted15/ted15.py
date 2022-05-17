# LOCAIS PARA ARMAZENAR OS DADOS 
dados = {}
funcionarios = []
try:
    # MENU INTERATIVO
    def menu() :
        option = int(input('''
    [1] - Cadastrar um funcionário
    [2] - Mostrar todos os funcionários
    [3] - Editar Funcionario
    [4] - Excluir um funcionário
    [5] - Adicionar um aumento de salário
    [6] - Sair do programa
    '''))

        return option
    # FUNÇÃO DE CADASTRO DE DADOS E CHECAGEM
    def cadastra_funcionario():
        
        codigo = input("Codigo do funcionário...")
        if codigo in dados:
            print("O Funcionario já esta cadastrado !")
        else:
            nome = input("Nome do funcionário...")
            email = input("Email do funcionário...")
            dataDeAdmissao = input("Data de admissao do funcionário...dd/mm/aaaa...")
            salario = input("Salario do funcionário...")
            funcionariosdados = (codigo, nome, email, dataDeAdmissao, salario)
            funcionarios.append(funcionariosdados)
            dados[codigo] = [nome,email,dataDeAdmissao,salario]
            print(dados)
            
    # MOSTRAR OS FUNCIONARIOS CADASTRADOS
    def mostrar_funcionarios() :
        for funcionario in funcionarios:
            print(f" Codigo do funcionario: {funcionario[0]} Nome: {funcionario[1]} E-mail: {funcionario[2]} Data Admissao: {funcionario[3]} Salario:R$ {funcionario[4]}")
    # REMOVER OS FUNCIONARIOS CADASTRADOS
    def remover():
        codigo=str(input("Digite o codigo do funcionario :"))
        if codigo in dados:
            del dados [codigo]
            for funcionario in funcionarios:
                funcionarios.remove(funcionario)
            print("Funcionario removido com sucesso!")

        else:
            print("Funcionario  não encontrado. Tente novamente!")
    # EDITAR DADOS DE CADASTRO
    def edit():
        codigo=str(input("Digite o codigo do funcionario:"))
        if codigo in dados:
            for funcionario in funcionarios:
                funcionarios.remove(funcionario)
                codigo = input("Codigo do funcionário...")
                nome = input("Nome do funcionário...")
                email = input("Email do funcionário...")
                dataDeAdmissao = input("Data de admissao do funcionário...dd/mm/aaaa...")
                salario = input("Salario do funcionário...")
                funcionariosdados = (codigo, nome, email, dataDeAdmissao, salario)
                funcionarios.append(funcionariosdados)
                dados[codigo] = [nome,email,dataDeAdmissao,salario]
                print("Alterações feitas com sucesso!")
            else:
                print("Nome alterado com sucesso!")
    # ATUALIZAR O SALARIO DO FUNCIONARIO         
    def editsalario():
        codigo=str(input("Digite o codigo do funcionario:"))
        if codigo in dados:
            for funcionario in funcionarios:
                funcionarios.remove(funcionario)
                codigo = input("Codigo do funcionário...")
                nome = input("Nome do funcionário...")
                email = input("Email do funcionário...")
                dataDeAdmissao = input("Data de admissao do funcionário...dd/mm/aaaa...")
                salario = input("Digite o novo salario do funcionário...")
                funcionariosdados = (codigo, nome, email, dataDeAdmissao, salario)
                funcionarios.append(funcionariosdados)
                dados[codigo] = [nome,email,dataDeAdmissao,salario]
                print("Alterações feitas com sucesso!")
            else:
                print("Nome alterado com sucesso!")

    #FUNÇÕES DE VARIAVEIS DE REPETIÇÃO
    def programa() :

        while True:
            option = menu()

            if option == 1 :
                cadastra_funcionario()
            if option == 2 :
                mostrar_funcionarios()
            if option == 3 :
                edit()
            if option == 4 :
                remover()
            if option == 5 :
                editsalario()
            elif option == 6 :
                print("Obrigado! Volte sempre.")    
                break

    programa()
except:
    print("ERRO FAVOR INSERIR AS CREDENCIAIS DE FORMA INTELIGENTE")