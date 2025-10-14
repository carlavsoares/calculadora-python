def calculadora():
    while True:
        a = float(input("\nDigite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        print("\n1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")

        opcao = (input("ESCOLHA UMA OPCAO: "))

        if opcao == '1':
            soma = a+b
            print("\nResultado da {:.2f}".format(soma))
        elif opcao == '2':
            sub = a-b
            print("\nResultado da subtracao: {:.2f}".format(sub))
        elif opcao == '3':
            mult = a*b
            print("\nResultado da multiplicacao:{:.2f}".format(mult))
        elif opcao == '4':
            div = a/b
            if b == 0:
                print("\nErro: divisao por zero")
            else:
                print("\nResultado da divisao: {:.2f}".format(div))
        else:
            print("\nOPCAO INVALIDA! TENTE NOVAMENTE")

        continuar = input("\nDeseja continuar? [S/N]").strip().upper()[0]
        if continuar != 'S':
            print ("\nEncerrando o programa...")
            break

calculadora()
