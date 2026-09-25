def gerar_instrucoes(expressao):
    pilha = []
    temp = 1
    instrucoes = []

    for caractere in expressao:

        # Se for operando, coloca na pilha
        if caractere.isalpha():
            pilha.append(caractere)

        # Se for operador
        elif caractere in "+-*/":

            # Segundo operando
            op2 = pilha.pop()

            # Primeiro operando
            op1 = pilha.pop()

            # Carrega o primeiro operando no registrador
            instrucoes.append(f"LD {op1}")

            # Realiza a operação com o segundo operando
            if caractere == "+":
                instrucoes.append(f"AD {op2}")

            elif caractere == "-":
                instrucoes.append(f"SB {op2}")

            elif caractere == "*":
                instrucoes.append(f"ML {op2}")

            elif caractere == "/":
                instrucoes.append(f"DV {op2}")

            # Guarda o resultado em uma variável temporária
            temporario = f"TEMP{temp}"
            instrucoes.append(f"ST {temporario}")

            # Coloca o temporário de volta na pilha
            pilha.append(temporario)

            temp += 1

    # O resultado final deve ficar no registrador
    resultado = pilha.pop()
    instrucoes.append(f"LD {resultado}")

    return instrucoes
