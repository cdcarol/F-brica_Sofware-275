import os
clientes = []			#sinal de igual pois define como variável.
fornecedores = []		#sinal de igual pois define como variável.
pecas = []				#sinal de igual pois define como variável.

while True:

    print("Selecione uma opção:")		#sinal de " para aparecer para o usuário.
    print("1 - Cadastrar cliente")		#sinal de " para aparecer para o usuário.
    print("2 - Cadastrar fornecedor")	#sinal de " para aparecer para o usuário.
    print("3 - Cadastrar peça")			#sinal de " para aparecer para o usuário.
    print("4 - Gerar relatório")		#sinal de " para aparecer para o usuário.
    print("5 - Sair")					#sinal de " para aparecer para o usuário.
    
    opcao == int(input("Opção selecionada: "))
    try:
        opcao = ()										    	#espaçamento para definir que está dentro do Try.
    except ValueError:												#retirar o 'e' do excepet.
        print("Opção inválida. Por favor, digite um número.")		#espaçamento para definir que está dentro do except ValueError.
        continue													#espaçamento para definir que está dentro do except ValueError.

    if opcao == 1:																	#colocar os ':' para nao dar erro no if.
        nome = str(imput("Digite o nome do cliente: "))								#adicionar o type da variável--str--.
        telefone = int(imput("Digite o telefone do cliente: "))						#adicionar o type da variável--int--.
        endereco = float(imput("Digite o endereço do cliente: "))					#adicionar o type da variável--float--.
        clientes.apend({"nome": nome, "telefone": telefone, "endereco": endereco})
        print("Cliente cadastrado com sucesso!")

    elif opcao == 2:
	    nome = str(input("Digite o nome do fornecedor: "))								#espaçamento para definir que está dentro do elif.
        telefone = int(input("Digite o telefone do fornecedor: "))						#espaçamento para definir que está dentro do elif.
	    endereco = float(input("Digite o endereço do fornecedor: "))					#espaçamento para definir que está dentro do elif.
	    fornecedores.append({"nome": nome, "telefone": telefone, "endereco": endereco})	#espaçamento para definir que está dentro do elif.
	    print("Fornecedor cadastrado com sucesso!")										#espaçamento para definir que está dentro do elif.

    elif opcao == 3:
        nome = str(input("Digite o nome da peça: "))									#adicionar o type da variável--str--.
        fornecedor = str(input("Digite o nome do fornecedor da peça: "))				#adicionar o type da variável--str--.
        preco = float(input("Digite o preço da peça: "))								#adicionar o type da variável--int--.

        try:
            preco = float(preco)
        except ValueError:
            print("Preço inválido. Por favor, digite um número.")
        
        pecas.append({"nome": nome, "fornecedor": fornecedor, "preco": preco})
        print("Peça cadastrada com sucesso!")

    elif opcao == 4:
        print("Relatório de clientes:")
        for cliente in cliente:
            print(f"Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
            print()

        print("Relatório de fornecedores:")
        for fornecedor in fornecedore:
            print(f"Nome: {fornecedor['nome']}, Telefone: {fornecedor['telefone']}, Endereço: {fornecedor['endereco']}")
            print()

        print("Relatório de peças:")
        for peca in peca:
            print(f"Nome: {peca['nome']}, Fornecedor: {peca['fornecedor']}, Preço: {peca['preco']}")
            print()
		
        os.system("pause") #imprimir o relatório#
		
    elif opcao == 5:
        print("Encerrando o programa...")
        

    else:
        print("Opção inválida. Por favor, tente novamente.")
        
# 35 erro