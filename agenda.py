def exibir_menu():
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Visualizar Lista de Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar como Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    } 

    agenda.append(contato)
    print(f"\n Contato '{nome}' adicionado com sucesso!")

def visualizar_contato(agenda):
    if not agenda: 
       print("\n Sua agenda está vazia. Adicione um contato na opção 1.")
       return

    print("\n---  LISTA DE CONTATOS ---")
    for indice, contato in enumerate(agenda,start=1):
        print(f"{indice}. {contato['nome']} | {contato['telefone']} | {contato['email']}")

def editar_contato(agenda):
    if not agenda: 
       print("\n Nenhum contato cadastrado. Adicione um contato primeiro")
       return

    print("\n--- SEUS CONTATOS ---")
    for indice, contato in enumerate(agenda, start=1):
        print(f"{indice}. {contato['nome']} {contato['telefone']} {contato['email']}")

    entrada = input("\n Digite o número do contato que deseja editar (ou 0 para cancelar): ")

    if entrada == "0":
       print("\n Edição cancelada. Voltada ao Menu Principal.")
       return

    if entrada.isdigit():
        posição = int(entrada) - 1

        if 0 <= posição < len(agenda):
            contato_atual = agenda[posição]

            while True:
                print(f"\n--- EDITANDO: {contato_atual ['nome']} ---")
                print("1. Alterar apenas o Nome")
                print("2. Alterar apenas o Telefone")
                print("3. Alterar apenas o E-mail")
                print("4. Alterar todos os campos")
                print("5. Cancelar e Voltar ao Menu Principal")

                campo = input("\n O que você deseja editar? (1-5 ou 0): ")

                if campo in ["5", "0"]:
                    print("\n Edição cancelada. Voltando ao Menu Principal")
                    break

                elif campo == "1":
                    print(f"\n Nome atual: {contato_atual['nome']} ")
                    print(" -> Digite o novo nome")
                    print("-> Digite 'V' para VOLTAR às opções de edição")
                    print("-> Digite 'C' para CANCELAR e ir ao Menu Principal")

                    novo_nome = input("\n Sua opção: ")

                    if novo_nome.upper() == "C":
                        print("\n  Edição cancelada. ")
                        break
                    elif novo_nome.upper() == "V" or novo_nome == "":
                        print("\n Operação voltada. Nenhuma alteração feita no nome.")
                        continue
                    else:
                        agenda[posição] ['nome'] = novo_nome
                        print("\n Nome atualizado com sucesso!")

                elif campo == "2":
                    print(f"\n Telefone atual: {contato_atual['telefone']}")
                    print(" -> Digite o novo telefone")
                    print(" -> Digite 'V' para VOLTAR às opções de edição")
                    print(" -> Digite 'C' para CANCELAR e ir ao Menu Principal")

                    novo_tel = input("\n Sua Opção: ")

                    if novo_tel.upper() == "C":
                        print("\n Edição Cancelada. ")
                        break
                    elif novo_tel.upper() == "V" or novo_tel == "":
                        print("\n Operação voltada. Nenhum telefone alterado.")
                        continue
                    else:
                        agenda[posição]["telefone"] = novo_tel 
                        print("\n Telefone atualizado com sucesso!")

                elif campo == "3":
                    print(f"\n E-mail atual {contato_atual['email']}")
                    print(" -> Digite o novo e-mail")
                    print(" -> Digite 'V' para VOLTAR às opções de edição")
                    print(" -> Digite 'C'para CANCELAR e ir ao Menu Principal")

                    novo_email = input("\n Sua opção: ")

                    if novo_email.upper() == "C":
                        print("\n Edição cancelada.")
                        break
                    elif novo_email.upper() == "V" or novo_email == "":
                        print("\n Operação voltada. Nenhum e-mail alterado.")
                        continue
                    else:
                        agenda[posição]["email"] = novo_email
                        print("\n E-mail alterado com sucesso!")

                elif campo == "4":
                    print("\n[Alteração Completa - Digite 'V' em qualquer campo para VOLTAR]")
                    novo_nome = input(f"Novo nome(Atual: {contato_atual['nome']})")
                    if novo_nome.upper() == "V":
                        continue

                    novo_tel = input(f"Novo telefone(Atual: {contato_atual['telefone']})")
                    if novo_tel.upper() == "V":
                        continue

                    novo_email = input(f"Novo E-mail(Atual: {contato_atual['email']})")
                    if novo_email.upper() == "V":
                        continue

                    if novo_nome:
                        agenda[posição]['nome'] = novo_nome
                    if novo_tel:
                        agenda[posição]['telefone'] = novo_tel
                    if novo_email:
                        agenda[posição]['email'] = novo_email

                    print("\n Todos os campos atualizados com sucesso!")


                else:
                    print("\n Número fora da lista.")

        else:
            print("\n Digite apenas números.")

def favoritar_contato(agenda):
    if not agenda:
        print("\n Nenhum contato cadastrado. Adicione um contato primeiro.")
        return
    
    print("\n --- SEUS CONTATOS ---")
    for indice, contato in enumerate(agenda,start=1):
        print(f"{indice}. {contato['nome']}")

    entrada = input("\n Digite o número do contato para favoritar/desfavoritar (ou 0) para cancelar): ")

    if entrada == "0":
        print("\n Ação cancelada")
        return

    if entrada.isdigit():
        posicao = int(entrada) - 1

        if 0 <= posicao < len(agenda):
            agenda[posicao] ["favorito"] = not agenda[posicao] ["favorito"]

            if agenda[posicao] ["favorito"]:
                status = "marcado como FAVORITO"
            else:
                status = "removido dos favoritos" 

            print(f"\n Contato '{agenda[posicao]['nome']} '{status}!")
        else:
            print(f"\n Número fora da lista.")
    else:
        print(f"\n Digite apenas números.")

def visualizar_favoritos(agenda):
    if not agenda:
        print("\n Sua agenda está vazia. Nenhum favorito cadastrado.")
        return

    favoritos = [contato for contato in agenda if contato["favorito"]]

    if not favoritos:
        print("\n Você possui contatos, mas nenhum foi marcado como favorito ainda.")
    else:
        print("\n --- CONTATOS FAVORITOS ---")
        for indice, contato in enumerate(favoritos, start=1):
            print(f"\n {indice} {contato['nome']} | {contato['telefone']} | {contato['email']} ")

def deletar_contato(agenda):
    if not agenda:
        print("\n Nenhum contato para deletar. Sua agenda está vazia.")
        return

    print("\n --- SEUS CONTATOS ---")
    for indice, contato in enumerate(agenda, start=1):
        print(f"\n {indice} {contato['nome']}")

    entrada = input("\n Digite o contato que deseja deletar (ou 0 para cancelar): ")

    if entrada == "0":
        print("\n Remoção cancelada.")
        return

    if entrada.isdigit():
        posicao = int(entrada) - 1

        if 0 <= posicao < len(agenda):
            removido = agenda.pop(posicao)
            print(f"\n Contato '{removido['nome']}' Deletado com sucesso!")
        else:
            print("\n Número fora da lista.")
    else:
        print("\n Digite apenas números.")


def main():
    agenda_de_contatos = []

    while True:
        exibir_menu()

        opcao = input("\n Escolha uma opção (1-7): ")

        if opcao == "7":
            print("\n Saindo da agenda... Até mais! ")
            break
        elif opcao == "1":
            adicionar_contato(agenda_de_contatos)
        elif opcao == "2":
            visualizar_contato(agenda_de_contatos)
        elif opcao == "3":
            editar_contato(agenda_de_contatos)
        elif opcao == "4":
            favoritar_contato(agenda_de_contatos)
        elif opcao == "5":
            visualizar_favoritos(agenda_de_contatos)
        elif opcao == "6":
            deletar_contato(agenda_de_contatos)
        else:
            print("\n Opção Inválida. escolha um número entre 1 e 7.")

if __name__ == "__main__":
    main()