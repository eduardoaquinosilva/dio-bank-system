def leave():
    print("Obrigado e volte sempre!")
    exit()


def list_accounts(accounts):
    print("\n--------------- CONTAS ---------------")
    if accounts:
        for a in accounts:
            print(f"\nAgência:\t\t{a['agency']}")
            print(f"C/C:\t\t\t{a['account_number']}")
            print(f"Titular:\t\t{a['user']['name']}\n")
    else:
        print("Não há contas cadastradas.")
    print("-" * 38, "\n")


def new_account(agency, users, accounts):
    cpf = input("Informe o CPF do usuário: ")
    user = filter_user(cpf, users)

    account_number = len(accounts) + 1
    if user:
        print("Conta corrente criada com sucesso!\n")
        accounts.append({"agency": agency, "account_number": account_number, "user": user})
    else:
        print("Operação inválida! Usuário não encontrado.\n")


def filter_user(cpf, users):
    filtering = [user for user in users if cpf == user["cpf"]]
    return filtering[0] if filtering else None


def new_user(users):
    cpf = input("Informe CPF (Ex.: 11111111111): ")
    user_exists = filter_user(cpf, users)

    if user_exists:
        print("Operação inválida! Usuário já cadastrado com esse CPF.\n")
    else:
        name = input("Nome completo: ")
        birth_date = input("Data de nascimento (dd-mm-aaaa): ")
        state = input("Estado (sigla): ")
        city = input("Cidade: ")
        neighbourhood = input("Bairro: ")
        patio = input("Logradouro: ")
        number = input("Número: ")

        users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": f"{patio}, {number} - "
                                                                                     f"{neighbourhood} - {city}/{state}"
                                                                                     f""})
        print("Usuário cadastrado com sucesso!\n")


def statements(balance, /, *, statement):
    print("\n--------------- EXTRATO ---------------")
    if statement:
        for a in statement:
            print(a)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("-" * 39, "\n")


def withdrawals(*, balance, value, statement, limit, withdrawals_done, withdrawals_limit):
    withdrawals_available = withdrawals_done + 1 <= withdrawals_limit
    if withdrawals_available:
        value_available = 0 <= value <= limit

        if value_available:
            value_in_balance = balance >= value

            if value_in_balance:
                balance -= value
                statement.append(f"Saque:\t\tR$ {value:.2f}")
                withdrawals_done += 1
                print("Saque realizado com sucesso!\n")
            else:
                print("Operação inválida! Não é possível realizar saque pois não há valor suficinte de saldo.\n")
        else:
            print(f"Operação inválida! Não é possível realizar saque com valor fora do intervalo de R$ 0,00 e "
                  f"R$ {limit:.2f}\n")
    else:
        print(f"Operação inválida! Não é possível realizar mais de {withdrawals_limit} saque(s) por dia.\n")

    return balance, statement, withdrawals_done


def deposits(balance, value, statement, /):
    if value >= 0:
        balance += value
        statement.append(f"Depósito:\tR$ {value:.2f}")
        print("Depósito realizado com sucesso!\n")
    else:
        print("Operação inválida! Para retirar valores da conta utilize a função de saque.\n")

    return balance, statement


def menu():
    print("===== MENU =====")
    print("[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[4] - Nova Conta\n[5] - Listar Contas\n[6] - Novo Usuário\n"
          "[0] - Sair")
    print("================")

    try:
        return int(input("Operação: "))
    except ValueError:
        print("Operação Inválida!\n")
        main()


def main():
    balance, statement, withdrawals_done, users, accounts = 0, list(), 0, list(), list()
    MAXIMUM_DAILY_WITHDRAWALS = 3
    MAXIMUM_WITHDRAWAL_VALUE = 500
    AGENCY = "0001"

    while True:
        operation = menu()
        if operation == 1:
            try:
                value = float(input("Valor do depósito: R$ "))
                balance, statement = deposits(balance, value, statement)
            except ValueError:
                print("Operação inválida!\n")
                continue
        elif operation == 2:
            try:
                value = float(input("Valor do saque: R$ "))
                balance, statement, withdrawals_done = withdrawals(balance=balance, value=value, statement=statement,
                                                 limit=MAXIMUM_WITHDRAWAL_VALUE, withdrawals_done=withdrawals_done,
                                                 withdrawals_limit=MAXIMUM_DAILY_WITHDRAWALS)
            except ValueError:
                print("Operação inválida!\n")
                continue
        elif operation == 3:
            statements(balance, statement=statement)
        elif operation == 4:
            new_account(AGENCY, users, accounts)
        elif operation == 5:
            list_accounts(accounts)
        elif operation == 6:
            new_user(users)
        elif operation == 0:
            leave()
        else:
            print("Operação Inválida!\n")


main()
