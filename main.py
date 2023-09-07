balance, statement, withdrawals_done = 0, list(), 0
MAXIMUM_DAILY_WITHDRAWALS = 3
MAXIMUM_WITHDRAWAL_VALUE = 500


def leave():
    print("Obrigado e volte sempre!")
    exit()


def statements():
    print("\n--------------- EXTRATO ---------------")
    if statement:
        for a in statement:
            print(a)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {balance}")
    print("-" * 39, "\n")
    menu()


def withdrawals():
    global balance, withdrawals_done
    withdrawals_available = withdrawals_done + 1 <= MAXIMUM_DAILY_WITHDRAWALS
    if withdrawals_available:
        value = float(input("Valor do saque: R$ "))
        value_available = 0 <= value <= MAXIMUM_WITHDRAWAL_VALUE

        if value_available:
            value_in_balance = balance >= value

            if value_in_balance:
                balance -= value
                statement.append(f"Saque: R$ {value:.2f}")
                withdrawals_done += 1
                print("Saque realizado com sucesso!\n")
                menu()
            else:
                print("Operação inválida! Não é possível realizar saque pois não há valor suficinte de saldo.\n")
                menu()
        else:
            print(f"Operação inválida! Não é possível realizar saque com valor fora do intervalo de R$ 0,00 e "
                  f"R$ {MAXIMUM_WITHDRAWAL_VALUE:.2f}\n")
            menu()
    else:
        print(f"Operação inválida! Não é possível realizar mais de {MAXIMUM_DAILY_WITHDRAWALS} saque(s) por dia.\n")
        menu()


def deposits():
    global balance
    value = float(input("Valor do depósito: R$ "))

    if value >= 0:
        balance += value
        statement.append(f"Depósito: R$ {value:.2f}")
        print("Depósito realizado com sucesso!\n")
        menu()
    else:
        print("Operação inválida! Para retirar valores da conta utilize a função de saque.\n")
        menu()


def menu():
    print("===== MENU =====")
    print("[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[0] - Sair")
    print("================")
    try:
        operation = int(input("Operação: "))

        if operation == 1:
            deposits()
        elif operation == 2:
            withdrawals()
        elif operation == 3:
            statements()
        elif operation == 0:
            leave()
        else:
            print("Operação Inválida!\n")
            menu()
    except ValueError:
        print("Operação Inválida!\n")
        menu()


menu()
