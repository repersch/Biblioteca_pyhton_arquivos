#verifica se um arquivo existe
def existe_arquivo(arquivo):
    import os
    if os.path.exists(arquivo):
        return True
    else:
        return False
    

#tranforma o arquivo em lista
def obter_base_dados(arquivo):
    base_dados = []
    if existe_arquivo(arquivo):
        arq = open(arquivo, "r")
        for linha in arq:
            linha = linha.split(";")
            base_dados.append(linha)
        return base_dados
    else:
        print(f"O arquivo {arquivo} não pode ser aberto.")

        

#apresenta o submenu de usuários
def sub_usuários(usuários):
    opção = 0
    while opção != "6":
        print("\n---------------------------\n"
              "    Submenu de Usuários:\n"
              "---------------------------\n"
              "1. Listar todos\n"
              "2. Listar elemento \n"
              "3. Incluir\n"
              "4. Alterar\n"
              "5. Excluir\n"
              "6. Voltar\n")
        opção = input("Digite a opção desejada: ")
        while opção not in "123456":
            opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")
            

        #lista todos os dados dos usuários cadastrados   
        if opção == "1":
            contagem = 1 
            for pessoa in range(len(usuários)):
                print(f"\n  -- Usuário {contagem} --\n")
                print(f"CPF: {usuários[pessoa][0]}\n"
                        f"Nome: {usuários[pessoa][1]}\n"
                        f"Rua: {usuários[pessoa][2]}\n"
                        f"Número: {usuários[pessoa][3]}\n"
                        f"CEP: {usuários[pessoa][4]}")
                print("E-mail(s):")
                emails = usuários[pessoa][5].split(" ")
                for endereço in emails:
                    print(f"\t{endereço}")
                print("Telefone(s):")
                telefones = usuários[pessoa][6].split(" ")
                for telefone in telefones:
                    print(f"\t{telefone}")
                print(f"Data de nascimento: {usuários[pessoa][7]}\n"
                      f"Profissão: {usuários[pessoa][8]}")
                contagem += 1
            if len(usuários) == 0:
                print("Não existem usuários cadastrados")
    
           
        #lista os dados de um usuários específico buscado pelo cpf              
        if opção == "2":
            pessoa = input("\nDigite o CPF: ").strip()
            busca = False
            for cadastro in range(len(usuários)):
                if pessoa in usuários[cadastro][0]:
                    print(f"\nNome: {usuários[cadastro][1]}")
                    print(f"Rua: {usuários[cadastro][2]}")
                    print(f"Número: {usuários[cadastro][3]}")
                    print(f"CEP: {usuários[cadastro][4]}")
                    print("E-mail(s):")
                    emails = usuários[cadastro][5].split(" ")
                    for endereço in emails:
                        print(f"\t{endereço}")
                    print("Telefone(s):")
                    telefones = usuários[cadastro][6].split(" ")
                    for telefone in telefones:
                        print(f"\t{telefone}")
                    print(f"Data de nascimento: {usuários[cadastro][7]}")
                    print(f"Profissão: {usuários[cadastro][8]}")
                    busca = True
            if not busca:
                print("CPF não cadastrado.")
                                      
            
        #inclui dados de um novo usuário
        if opção == "3":
            arq_usuários = open("cadastro_usuarios.txt", "a")
            lista_usuários = usuários
            busca = False
            num_cpf = input("CPF (somente números): ").strip()
            while len(num_cpf) != 11 or num_cpf.isdigit() == False :
                num_cpf = input("CPF inválido. Digite o CPF (somente números): ").strip()
            for cadastro in range(len(lista_usuários)): #verifica se o e cpf já existe no arquivo
                if num_cpf in lista_usuários[cadastro][0]:
                    busca = True
                    print("CPF já cadastrado.")  
            if not busca:
                usuário = []
                usuário.append(num_cpf)
                arq_usuários.write(f"{num_cpf};")
                usuário.append(input("Nome: "))
                arq_usuários.write(f"{usuário[1]};")
                usuário.append(input("Rua: "))
                arq_usuários.write(f"{usuário[2]};")
                usuário.append(input("Número: "))
                arq_usuários.write(f"{usuário[3]};")
                num_cep = input("CEP (somente números): ").strip()
                while len(num_cep) != 8 or num_cep.isdigit() == False:
                    num_cep = input("CEP inválido. Digite o CEP (somente números): ").strip()
                usuário.append(num_cep)
                arq_usuários.write(f"{usuário[4]};")
                lista_emails = []
                resp = "S"
                while resp in "S":
                    end_email = input("E-Mail: ")
                    if end_email in lista_emails:
                        print("E-Mail já cadastrado")
                    else:
                        lista_emails.append(end_email)
                        arq_usuários.write(f"{end_email} ")
                    resp = input("Cadastrar outro e-mail? [S/N] ").strip().upper()
                usuário.append(lista_emails)
                arq_usuários.write(";")
                lista_telefones = []
                resp = "S"
                while resp in "S":
                    num_telefone = input("Telefone: ")
                    if num_telefone in lista_telefones:
                        print("Telefone já cadastrado.")
                    else:
                        lista_telefones.append(num_telefone)
                        arq_usuários.write(f"{num_telefone} ")
                    resp = input("Cadastrar outro telefone? [S/N] ").strip().upper()
                usuário.append(lista_telefones)
                usuário.append(input("Data de nascimento: "))
                arq_usuários.write(f";{usuário[7]};")
                usuário.append(input("Profissão: "))
                arq_usuários.write(f"{usuário[8]};")
                arq_usuários.write('\n')
                arq_usuários.close()
                lista_usuários.append(usuário)
                print("-- Usuário cadastrado com sucesso --")
                usuários = obter_base_dados("cadastro_usuarios.txt")

      

        #altera os dados de um usuário já cadastrado, busca pelo cpf
        if opção == "4":
            pessoa = input("Digite o CPF: ").strip()
            busca = False
            for cadastro in range(len(usuários)): #faz as alterações e salva na lista
               if pessoa in usuários[cadastro][0]:
                    print(f"\nUsuário: {usuários[cadastro][1]}\n"
                          "-- Digite apenas os dados que serão alterados: ")
                    nome = input("Nome: ").strip()
                    if len(nome) > 0:
                        usuários[cadastro][1] = nome
                    rua = input("Rua: ").strip()
                    if len(rua) > 0:
                        usuários[cadastro][2] = rua
                    número = input("Número: ").strip()
                    if len(número) > 0:
                        usuários[cadastro][3] = número
                    CEP = input("CEP: ")
                    if len(CEP) > 0:
                        while len(CEP) != 8 or CEP.isdigit() == False:
                            CEP = input("CEP inválido. Digite o CEP (somente números): ").strip()
                        usuários[cadastro][4] = CEP
                    email = input("E-mail: ").strip()
                    if email not in usuários[cadastro][5]: 
                        if len(email) != 0:
                            usuários[cadastro][5] += (email + " ")
                    else:
                        print("E-mail já cadastrado.")
                    telefone = input("Telefone: ")
                    if telefone not in usuários[cadastro][6]:
                        if len(telefone) != 0:
                            usuários[cadastro][6] += (telefone + " ")
                    else:
                        print("Telefone já cadastrado.")
                    data_nascimento = input("Data de nascimento: ")
                    if len(data_nascimento) > 0:
                        usuários[cadastro][7] = data_nascimento
                    profissão = input("Profissão: ")
                    if len(profissão) > 0:
                        usuários[cadastro][8] = profissão
                    print("Dados alterados com sucesso!")
                    busca = True

            arq_usuários = open("cadastro_usuarios.txt", "w") #subscreve todos os registros no arquivo
            for registro in range(len(usuários)):
                arq_usuários.write(f"{usuários[registro][0]};")
                arq_usuários.write(f"{usuários[registro][1]};")
                arq_usuários.write(f"{usuários[registro][2]};")
                arq_usuários.write(f"{usuários[registro][3]};")
                arq_usuários.write(f"{usuários[registro][4]};")
                arq_usuários.write(f"{usuários[registro][5]};")
                arq_usuários.write(f"{usuários[registro][6]};")
                arq_usuários.write(f"{usuários[registro][7]};")
                arq_usuários.write(f"{usuários[registro][8]};")
                arq_usuários.write("\n")
            arq_usuários.close()
                
            if not busca:
                print("CPF não cadastrado.")
            usuários = obter_base_dados("cadastro_usuarios.txt")

                          
        #exclui os dados de um usuário cadastrado, busca pelo cpf       
        if opção == "5":
            pessoa = input("Digite o CPF: ").strip()
            busca = False
            for cadastro in range(len(usuários)):
                if pessoa == usuários[cadastro][0]:
                    print(f"\nExcluir usuário: {usuários[cadastro][1]}")
                    resposta = input("Confirmar? [S/N]: ").upper().strip()
                    while resposta not in "SN":
                        resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
                    if resposta == "S":
                        print(f"Usuário -- {usuários[cadastro][1]} -- excluído com sucesso.")
                        del usuários[cadastro]
                        busca = True
                        break
                    else:
                        busca = True
                        
            arq_usuários = open("cadastro_usuarios.txt", "w")
            for registro in range(len(usuários)):
                arq_usuários.write(f"{usuários[registro][0]};")
                arq_usuários.write(f"{usuários[registro][1]};")
                arq_usuários.write(f"{usuários[registro][2]};")
                arq_usuários.write(f"{usuários[registro][3]};")
                arq_usuários.write(f"{usuários[registro][4]};")
                arq_usuários.write(f"{usuários[registro][5]};")
                arq_usuários.write(f"{usuários[registro][6]};")
                arq_usuários.write(f"{usuários[registro][7]};")
                arq_usuários.write(f"{usuários[registro][8]};")
                arq_usuários.write("\n")
            arq_usuários.close()
            usuários = obter_base_dados("cadastro_usuarios.txt")
                
            if not busca:
                print("CPF não cadastrado.")
            
                    

#apresenta o submenu de livros
def sub_livros(livros):
    opção = 0
    while opção != "6":
        print("\n---------------------------\n"
              "     Submenu de Livros:\n"
              "---------------------------\n"
              "1. Listar todos\n"
              "2. Listar elemento \n"
              "3. Incluir\n"
              "4. Alterar\n"
              "5. Excluir\n"
              "6. Voltar\n")
        opção = input("Digite a opção desejada: ")
        while opção not in "123456":
            opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")
            

        #lista todos os dados dos livros cadastrados   
        if opção == "1":
            contagem = 1
            for livro in range(len(livros)):
                print(f"\n  -- Livro {contagem} --\n"
                      f"ISBN: {livros[livro][0]}\n"
                      f"Título: {livros[livro][1]}\n"
                      f"Gênero: {livros[livro][2]}\n"
                      "Autor(es):")
                autores = livros[livro][3].split("    ")
                for autor in autores:
                    print(f"\t{autor}")
                print(f"Número de páginas: {livros[livro][4]}")
                contagem += 1
            if len(livros) == 0:
                print("Não existem livros cadastrados.")


        #lista os dados de um livro específico, busca pelo isbn        
        if opção == "2":
            isbn= input("\nDigite o ISBN do livro que deseja listar: ")
            busca = False
            for cadastro in range(len(livros)):
                if isbn in livros[cadastro][0]:
                    print(f"Título: {livros[cadastro][1]}")
                    print(f"Gênero: {livros[cadastro][2]}")
                    print(f"Autores: ")
                    autores = livros[livro][3].split("    ")
                    for autor in autores:
                        print(f"\t{autor}")
                    print(f"Número de páginas: {livros[cadastro][4]}")
                    busca = True
            if not busca:
                print("ISBN não cadastrado.")
                
                
        #inclui um novo livro no cadastro
        if opção == "3":
            arq_livros = open("cadastro_livros.txt", "a")
            busca = False
            isbn = input("\nISBN do livro a ser cadastrado: ").strip()
            while len(isbn) != 13 or isbn.isdigit() == False:
                isbn = input("ISBN inválido. Digite o ISBN do Livro (somente números): ").strip()
            if len(livros) != 0:
                for cadastro in range(len(livros)):#verifica se o isbn já existe no arquivo
                    if isbn in livros[cadastro][0]:
                        busca = True
                        print('ISBN já cadastrado')
            if not busca or len(livros) == 0:
                livro = []
                livro.append(isbn)
                arq_livros.write(f"{isbn};")
                livro.append(str(input("Insira o Título do livro: ")))
                arq_livros.write(f"{livro[1]};")
                livro.append(str(input("Insira o Gênero do livro: ")))
                arq_livros.write(f"{livro[2]};")
                list_autores = [ ]
                escolha = "S"
                while escolha in "S":
                    autor = input("Insira o Autor do livro: ")
                    list_autores.append(autor)
                    arq_livros.write(f"{autor}    ")
                    escolha = input("Este livro possui mais de um autor? [S/N] ").strip().upper()
                livro.append(list_autores)
                arq_livros.write(";")
                livro.append(input("Número de páginas: "))
                arq_livros.write(f"{livro[4]};")
                arq_livros.write("\n")
                arq_livros.close()
                livros.append(livro)
                print("\nLivro Adicionado com Sucesso!")
            livros = obter_base_dados("cadastro_livros.txt")
                

        #altera os dados de um livro já cadastrado, busca pelo isbn
        if opção == "4":
            isbn = input("Digite o ISBN do livro: ").strip()
            busca = False
            for cadastro in range(len(livros)):
                if isbn in livros[cadastro][0]:
                    print(f"\nLivro: {livros[cadastro][1]}\n"
                          "-- Digite apenas os dados que serão alterados: ")
                    titulo = input("Título do livro: ").strip()
                    if len(titulo) > 0:
                        livros[cadastro][1] = titulo
                    genero = input("Gênero do livro: ").strip()
                    if len(genero) > 0:
                        livros[cadastro][2] = genero
                    autor = input("Autor(es) do livro: ")
                    if autor not in livros[cadastro][3]: 
                        livros[cadastro][3] += (autor + "    ")
                    else:
                        print("Este autor já está registrado")
                    num_pag = input("Número de páginas do livro: ")
                    if len(num_pag) > 0:
                        livros[cadastro][4] = num_pag
                    print("\n-- Dados alterados com sucesso! --")
                    busca = True

            arq_livros = open("cadastro_livros.txt", "w")#subscreve todos os registros do arquivo
            for registro in range(len(livros)):
                arq_livros.write(f"{livros[registro][0]};")
                arq_livros.write(f"{livros[registro][1]};")
                arq_livros.write(f"{livros[registro][2]};")
                arq_livros.write(f"{livros[registro][3]};")
                arq_livros.write(f"{livros[registro][4]};")
                arq_livros.write("\n")
            arq_livros.close()
                
            if not busca:
                print("ISBN não cadastrado.")
            livros = obter_base_dados("cadastro_livros.txt")
                
        #exclui os dados de um livro cadastrado, busca pelo isbn
        if opção == "5":
            livro = input("Digite o ISBN: ").strip()
            busca = False
            for exclude in range(len(livros)):
               if livro in livros[exclude][0]:
                    print(f"\nExcluir Livro: {livros[exclude][1]}")
                    busca = True
                    resposta = input("Confirmar? [S/N]: ").upper().strip()
                    while resposta not in "SN":
                        resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
                    if resposta == "S":
                        print(f"Livro -- {livros[exclude][1]} -- excluído com sucesso.")
                        del livros[exclude]
                        break
                    
            arq = open("cadastro_livros.txt", "w")
            for exc in range(len(livros)):
                arq.write(f"{livros[exc][0]};")
                arq.write(f"{livros[exc][1]};")
                arq.write(f"{livros[exc][2]};")
                arq.write(f"{livros[exc][3]};")
                arq.write(f"{livros[exc][4]};")
                arq.write("\n")
            arq.close()
            livros = obter_base_dados("cadastro_livros.txt")
                                      
            if not busca:
                print("ISBN não cadastrado.")
            
            
#apresenta o submenu de empréstimos
def sub_empréstimos(usuários, livros, empréstimos):
    print("\n---------------------------\n"
          "  Submenu de Empréstimos:\n"
          "---------------------------\n"
          "1. Listar todos\n"
          "2. Listar elemento \n"
          "3. Incluir\n"
          "4. Alterar\n"
          "5. Excluir\n"
          "6. Voltar\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "123456":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")


    #lista todos os empréstimos cadastrados
    if opção == "1":
        contagem = 1
        for registro in range(len(empréstimos)):
            print(f"\n  -- Empréstimo {contagem} --\n")
            print(f"CPF: {empréstimos[registro][0]}")
            print(f"ISBN: {empréstimos[registro][1]}")
            print(f"Data de Retirada: {empréstimos[registro][2]}")
            print(f"Data de Devolução: {empréstimos[registro][3]}")
            print(f"Valor Diário da Multa por atraso: R${float(empréstimos[registro][4]):.2f}")
            contagem += 1
        if len(empréstimos) == 0:
            print("Não existem empréstimos cadastrados.")
            

    #lista os dados de um empréstimo específico, busca pelo cpf, isbn e data de retirada       
    if opção == "2":
        list_emprest = ()
        cpf_emprest = input("Digite o CPF da pessoa que realizou o empréstimo: ")
        isbn_list = input("Digite o ISBN do livro que foi emprestado: ")
        ret_list = input("Digite a data de retirada do empréstimo(xx/xx/xxxx): ")
        list_emprest = (cpf_emprest, isbn_list, ret_list)
        if list_emprest in empréstimos:
            print("\nAqui estão as informações que você solicitou:\n")
            print("CPF:", list_emprest[0])
            print(f"ISBN: {list_emprest[1]}\n"
                      f"Data de Retirada: {list_emprest[2]}\n"
                      f"Data de Devolução: {empréstimos[list_emprest][0]}\n"
                      f"Valor Diário da Multa por atraso: {empréstimos[list_emprest][1]}")
        else:
            print("Este empréstimo não está nos registros de empréstimos.")


    #inclui os dados de um novo empréstimo       
    if opção == "3":
        arq_empréstimos = open("cadastro_emprestimos.txt", "a")
        empréstimo = ()
        busca = False
        cpf = input("Digite o CPF (somente números): ").strip()
        while not busca:
            for cadastro in range(len(usuários)):
                if len(cpf) != 11 or cpf.isdigit() == False:
                    cpf = input("CPF inválido. Digite o CPF (somente números): ")
                elif cpf in usuários[cadastro][0]:
                    busca = True
                    print(f"Usuário: -- {usuários[cadastro][1]} --")
            if not busca:
                cpf = input("CPF não cadastrado. Digite o CPF (somente números): ")      
        isbn = input("Digite o ISBN do livro: ")
        busca = False
        while not busca:
            for cadastro in range(len(livros)):
                if len(isbn) != 13 or isbn.isdigit() == False:
                    isbn = input("ISBN inválido. Digite o ISBN: ")
                elif isbn in livros[cadastro][0]:
                    busca = True
                    print(f"Livro: -- {livros[cadastro][1]} --")
            if not busca:
                isbn = input("ISBN não cadastrado. Digite o ISBN: ")       
        data_retirada = input("Data de retirada[xx/xx/xxxx]: ")
        empréstimo = (cpf, isbn, data_retirada)
        for info in range(len(empréstimo)):
            arq_empréstimos.write(f"{empréstimo[info]};")
        lista_empréstimos = [ ]
        lista_empréstimos.append(empréstimo)
        lista_empréstimos.append(input("Data de devolução[xx/xx/xxxx]: "))
        arq_empréstimos.write(f"{lista_empréstimos[1]};")
        lista_empréstimos.append(float(input("Valor diário da Multa por Atraso: R$")))
        arq_empréstimos.write(f"{lista_empréstimos[2]};")
        arq_empréstimos.write("\n")
        arq_empréstimos.close()
        print("-- Empréstimo cadastrado com sucesso --")
        empréstimos = obter_base_dados("cadastro_emprestimos.txt")


    #altera os dados de um empréstimo já cadastrado, busca por cpf, isbn e data de retirada 
    if opção == "4":
        alter_emprest =()
        cpf_alter = input("Digite o CPF da pessoa que realizou o Empréstimo: ")
        isbn_alter = input("Digite o ISBN do livro referente ao empréstimo: ")
        data_alter = input("Digite a Data em que o livro foi retirado(xx/xx/xxxx): ")
        alter_emprest = (cpf_alter, isbn_alter, data_alter)
        busca = False
        infos_alterar = ()
        for cadastro in range(len(empréstimos)):
            infos_alterar = (empréstimos[cadastro][0], empréstimos[cadastro][1], empréstimos[cadastro][2])
            if infos_alterar == alter_emprest:
                data_dev = input("Digite a nova data de devolução se deseja alterá-la: ")
                if len(data_dev) > 0:
                    empréstimos[cadastro][3] = data_dev
                valor_mul = input("Digite o novo valor da multa de atraso caso deseja alterá-la: R$")
                if len(valor_mul) > 0:
                    empréstimos[cadastro][4] = float(valor_mul)
                print("\n-- Dados alterados com sucesso! --")
                busca = True

        arq_empréstimos = open("cadastro_emprestimos.txt", "w")#subscreve todos os registros do arquivo
        for registro in range(len(empréstimos)):
            arq_empréstimos.write(f"{empréstimos[registro][0]};")
            arq_empréstimos.write(f"{empréstimos[registro][1]};")
            arq_empréstimos.write(f"{empréstimos[registro][2]};")
            arq_empréstimos.write(f"{empréstimos[registro][3]};")
            arq_empréstimos.write(f"{empréstimos[registro][4]};")
            arq_empréstimos.write("\n")
        arq_empréstimos.close()
                              
        if not busca:
            print("Empréstimo não cadastrado")
        empréstimos = obter_base_dados("cadastro_emprestimos.txt")
            

    #exclui os dados de um empréstimo cadastrado, busca por cpf, isbn e data de retirada     
    if opção == "5":
        emprest_del=()
        cpf_del = input("Digite o CPF da pessoa que realizou empréstimo que deseja deletar da lista: ")
        isbn_del = input("Digite o ISBN do livro referente à esse empréstimo: ")
        data_del = input("Digite a data de retirada referente à esse empréstimo: ")
        emprest_del = (cpf_del, isbn_del, data_del)
        busca = False
        for cadastro in range(len(empréstimos)):
            infos_excluir = ()
            infos_excluir = (empréstimos[cadastro][0], empréstimos[cadastro][1], empréstimos[cadastro][2])
            if emprest_del == infos_excluir:
                print(f"\nExcluir Empréstimo: {emprest_del}")
                
                resposta = input("Confirmar? [S/N]: ").upper().strip()
                while resposta not in "SN":
                    resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
                if resposta == "S":
                    print("Empréstimo excluído com sucesso.")
                    del empréstimos[cadastro]
                    busca = True
                    break
                    
        archive = open("cadastro_emprestimos.txt", "w")
        for exc in range(len(empréstimos)):
            archive.write(f"{empréstimos[exc][0]};")
            archive.write(f"{empréstimos[exc][1]};")
            archive.write(f"{empréstimos[exc][2]};")
            archive.write(f"{empréstimos[exc][3]};")
            archive.write(f"{empréstimos[exc][4]};")
            archive.write("\n")
        archive.close()
        emprestimos = obter_base_dados("cadastro_emprestimos.txt")
        
        if not busca:
            print("Empréstimo não cadastrado.")
        
                

#retorna um relatório dos usuários com com mais de x anos de idade, x é fornecido pelo usuário
def usuários_idade(usuários, idade): 
    from datetime import datetime
    quantidade = 0
    usuários_idade_maior = []
    arq_usuários_idade = open("relatorio_usuarios_idade.txt", "w")
    print("\nSalvando informações em arquivo...")
    arq_usuários_idade.write(f"Registro de usuários com mais de {idade} anos: \n\n")
    for pessoa in range(len(usuários)):
        idade_usuário = datetime.now().year - int(usuários[pessoa][7][-4:])
        if idade_usuário > idade:
            print(f"\nCPF: {usuários[pessoa][0]}\n"
                  f"Nome: {usuários[pessoa][1]}\n"
                  f"Rua: {usuários[pessoa][2]}\n"
                  f"Número: {usuários[pessoa][3]}\n"
                  f"CEP: {usuários[pessoa][4]}\n"
                  "E-mail(s):")
            emails = usuários[pessoa][5].split(" ")
            for end in emails:
                print(f"\t{end}")
            print("Telefone(s): ")
            telefones = usuários[pessoa][6].split(" ")
            for tel in telefones:
                print(f"\t{tel}")
            print(f"Data de nascimento: {usuários[pessoa][7]}\n"
                  f"Profissão: {usuários[pessoa][8]}")
            print("*" * 50)
            quantidade += 1
            #salvando no arquivo
            if existe_arquivo("relatorio_usuarios_idade.txt"):
                arq_usuários_idade.write(f"\nCPF: {usuários[pessoa][0]}\n")
                arq_usuários_idade.write(f"Nome: {usuários[pessoa][1]}\n")
                arq_usuários_idade.write(f"Rua: {usuários[pessoa][2]}\n")
                arq_usuários_idade.write(f"Número: {usuários[pessoa][3]}\n")
                arq_usuários_idade.write(f"CEP: {usuários[pessoa][4]}\n")
                arq_usuários_idade.write("E-mail(s): \n")
                emails = usuários[pessoa][5].split(" ")
                for end in emails:
                    arq_usuários_idade.write(f"\t{end}\n")
                arq_usuários_idade.write("Telefone(s): \n")
                telefones = usuários[pessoa][6].split(" ")
                for tel in telefones:
                    arq_usuários_idade.write(f"\t{tel}\n")
                arq_usuários_idade.write(f"Data de nascimento: {usuários[pessoa][7]}\n")
                arq_usuários_idade.write(f"Profissão: {usuários[pessoa][8]}\n")
                arq_usuários_idade.write('*'*50) 
                
            else:
                print("O arquivo 'relatorios_usuarios_idade.txt' não pode ser aberto.")
    print(f"\nQuantidade de usuários com idade maior que {idade} anos: {quantidade}.")
    if quantidade == 0:
        print(f"Não existem usuários cadastrados com mais de {idade} anos.")
        arq_usuários_idade.write(f"Não existem usuários cadastrados com mais de {idade} anos.")
    arq_usuários_idade.close()

  

#lista os livros com mais de x autores, x é fornecido pelo usuário
def autores_livro(livros, quantidade):
    arq_quant_autores = open("relatorio_livros_por_quantidade_autores.txt", "w")
    arq_quant_autores.write(f"Relatório de livros com {quantidade} ou mais autores: \n\n")
    print("Salvando informações no arquivo...")
    busca = False
    for livro in range(len(livros)):
        autores = livros[livro][3].split("    ")
        quant_autores = len(autores) - 1
        if quant_autores >= quantidade:
            print(f"\nISBN: {livros[livro][0]}\n"
                  f"Título: {livros[livro][1]}\n"
                  f"Gênero: {livros[livro][2]}\n"
                  "Autor(es):")
            for nome in autores:
                print(f"\t{nome}")
            print(f"Número de páginas: {livros[livro][4]}")
            print("*" * 50)
            busca = True

            if existe_arquivo("relatorio_livros_por_quantidade_autores.txt"):
                arq_quant_autores.write(f"\nISBN: {livros[livro][0]}\n")
                arq_quant_autores.write(f"Título: {livros[livro][1]}\n")
                arq_quant_autores.write(f"Gênero: {livros[livro][2]}\n")
                arq_quant_autores.write("Autor(es): \n")
                for nome in autores:
                    arq_quant_autores.write(f"\t{nome}\n")
                arq_quant_autores.write(f"Número de páginas: {livros[livro][4]}\n")
                arq_quant_autores.write("*" * 50)
    arq_quant_autores.close()     
    if not busca:
        print(f"Não existem livros cadastrados com mais que {quantidade} autores.")


#lista os empréstimos que devem ser devolvidos entre as datas x e y, x e y fornecidos pelo usuário
def dados_empréstimos(usuários, livros, empréstimos, data_inicial, data_final):
    arq_emprest_dat = open("relatorio_emprestimos_entre_datas.txt", "w")
    arq_emprest_dat.write(f"Relatório de empréstimos com data de entrega entre {data_inicial} e {data_final}: \n\n")
    print("Salvando informações no arquivo...")
    busca = False
    from datetime import datetime
    data_inicial_ = datetime.strptime(data_inicial, '%d/%m/%Y').date()
    data_final_ = datetime.strptime(data_final, '%d/%m/%Y').date()
    for empréstimo in range(len(empréstimos)):
        data = datetime.strptime(empréstimos[empréstimo][3], '%d/%m/%Y').date()
        if data > data_inicial_ and data <= data_final_:
            busca = True
            cpf = empréstimos[empréstimo][0]
            print(f"\nCPF: {cpf}")
            arq_emprest_dat.write(f"\nCPF: {cpf}\n")
            for info in range(len(usuários)):
                if cpf == usuários[info][0]:
                    print(f"Nome: {usuários[info][1]}")
                    arq_emprest_dat.write(f"Nome: {usuários[info][1]}\n")
            isbn = empréstimos[empréstimo][1]
            print(f"ISBN: {isbn}")
            arq_emprest_dat.write(f"ISBN: {isbn}\n")
            for info in range(len(livros)):
                if isbn == livros[info][0]:
                    print(f"Título: {livros[info][1]}")
                    arq_emprest_dat.write(f"Título: {livros[info][1]}\n")
            data_retirada = empréstimos[empréstimo][2]
            print(f"Data de retirada: {data_retirada}")
            arq_emprest_dat.write(f"Data de retirada: {data_retirada}\n")
            print(f"Data de devolução: {empréstimos[empréstimo][3]}")
            arq_emprest_dat.write(f"Data de devolução: {empréstimos[empréstimo][3]}\n")
            print(f"Valor diário da multa por atraso: R${float(empréstimos[empréstimo][4]):.2f}")
            arq_emprest_dat.write(f"Valor diário da multa por atraso: R${float(empréstimos[empréstimo][4]):.2f}\n")
            arq_emprest_dat.write("*"*50)

    if not busca:
        print(f"Não existem empréstimos com data de entrega entre {data_inicial} e {data_final}.")
        arq_emprest_dat.write(f"Não existem empréstimos com data de entrega entre {data_inicial} e {data_final}.")
        
    arq_emprest_dat.close()
          
            
#submenu de opções de relatórios
def sub_relatórios(usuários, livros, empréstimos):
    print("\n---------------------------\n"
          "   Submenu de Relatórios:\n"
          "---------------------------\n"
          "1. Listar os usuários com mais de X anos de idade\n"
          "2. Listar os livros que tenham mais do que X autores\n"
          "3. Listar dados de empréstimos\n"
          "4. Voltar\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "1234":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 4: ")
        
    if opção == "1":
        idade = int(input("\nLista de todos os usuários com idade maior que (digite a idade desejada): "))
        usuários_idade(usuários, idade)
        

    if opção == "2":
        quantidade = int(input("\nLista de todos os livros que possuem a quantidade de autores maior que (digite a quantidade desejada): "))
        autores_livro(livros, quantidade)

    if opção == "3":
        print("Digite as datas inicial e final para ver os empréstimos que devem ser devolvidos entre tais datas:")
        data_inicial = input("Data inicial [xx/xx/xxxx]: ")
        data_final = input("Data final [xx/xx/xxxx]: ")
        dados_empréstimos(usuários, livros, empréstimos, data_inicial, data_final)


    
          
###################programa principal######################################################################
#cria o arquivo e o transforma em lista
open("cadastro_usuarios.txt", "a") 
usuários = obter_base_dados("cadastro_usuarios.txt")
open("cadastro_livros.txt", "a")
livros = obter_base_dados("cadastro_livros.txt")
open("cadastro_emprestimos.txt", "a")
empréstimos = obter_base_dados("cadastro_emprestimos.txt")

opção = 0
while opção != "5":
    print("\n---------------------------\n"
              "      Menu de opções:\n"
              "---------------------------\n"
              "1. Submenu de Usuários\n"
              "2. Submenu de Livros\n"
              "3. Submenu de Empréstimos\n"
              "4. Submenu de Relatórios\n"
              "5. Sair\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "12345":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 5: ")
        
    if opção == "1":
        sub_usuários(usuários)
         
    if opção == "2":
        sub_livros(livros)
        
    if opção == "3":
        sub_empréstimos(usuários, livros, empréstimos)
        
    if opção == "4":
        sub_relatórios(usuários, livros, empréstimos)
        
    if opção == "5":
        print("\n  ---  ENCERRANDO  ---")
     



