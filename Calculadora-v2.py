def calculadora():

    while(True):
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        print("\n1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")

        operacao = (input("ESCOLHA UMA OPCAO: "))

        match operacao:
            case '1':
                print("\nResultado da multiplicacao: {:.2f}".format(a+b))
            case '2':
                print("\nResultado da multiplicacao: {:.2f}".format(a-b))
            case '3':
                print("\nResultado da multiplicacao: {:.2f}".format(a*b))
            case '4':
                if b != 0:
                    print("\nResultado da multiplicacao: {:.2f}".format(a/b))
                else:
                    print("\nErro: divisao por zero")
            case _:
                print("\nOPCAO INVALIDA! TENTE NOVAMENTE")

        continuar = input("\nDeseja continuar? [S/N]").strip().upper()[0]
        if continuar != 'S':
            print ("\nEncerrando o programa...")
            break

calculadora()