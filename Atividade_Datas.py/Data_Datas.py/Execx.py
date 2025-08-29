import Datas

erro = True

while erro:
    print("\n")
    entrada = input("Digite a data (dd/mm/aaaa): ")
    print("\n")
    data_Separada = Datas.bissextoSep(entrada)
    
    if not data_Separada:
        print("Erro! Use o formato dd/mm/aaaa")
        print("\n")
        continue

    sair = "não"
    
    while sair == "não":
        opções = int(input(
            "Qual opção você deseja (digite apenas o número)?\n\n"
            "1 - Pesquisar por um índice na data (ex: dia, mês ou ano)\n"
            "2 - Saber se a data é válida\n"
            "3 - Saber se o ano é bissexto\n\n"
            "Digite aqui: "
        ))
        print("\n")

        if opções == 1:
            pesquisando = input("Digite o que você pretende encontrar (dia, mês, ano): ").lower()
            print("\n")
    
            if pesquisando == "mes":
                pesquisando = "mês"
    
            resultado = data_Separada.get(pesquisando, "Erro! tente outra vez")
            print(f"O {pesquisando} que você busca é '{resultado}'")
            print("\n")
    
        elif opções == 2:
            try:
                dia = int(data_Separada["dia"])
                mes = int(data_Separada["mes"])
                ano = int(data_Separada["ano"])

                if mes < 1 or mes > 12:
                    print("Data inválida! Mês incorreto.")

                else:
                    dias_por_mes = [31, 29 if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)) else 28, 
                                    31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    if 1 <= dia <= dias_por_mes[mes-1]:
                        print("A data é válida!")
                    else:
                        print("Data inválida! Dia incorreto.")
                print("\n")

            except:
                print("Erro ao validar a data. Tente novamente.\n")

        elif opções == 3:
            ano = int(data_Separada["ano"])

            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                print(f"O ano {ano} é bissexto!")
            else:
                print(f"O ano {ano} não é bissexto!")
            print("\n")

        else:
            print("Opção inválida. Digite 1, 2 ou 3.\n")

        continuar = input("Deseja continuar? (sim/não): ").strip().lower()
        if continuar == "sim":
            sair = "não"  
        if continuar == "não":
            sair = "sim"

        else:
            sair = "sim"
            break

print("Obrigado por usar o meu programa!")
