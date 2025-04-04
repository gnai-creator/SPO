def generate_spo_levels():
    levels = []

    for i in range(1, 97):
        if i <= 10:
            # Lógica binária simples
            levels.append(lambda x, i=i: int(sum(x[:i % len(x)]) % 2 == 0))
        
        elif i <= 20:
            # Paridade sobre janelas múltiplas
            levels.append(lambda x, i=i: int(
                sum([sum(x[j:j+2]) for j in range(0, len(x), 2)]) % (i % 5 + 2) == 0
            ))
        
        elif i <= 30:
            # Paridade com dependência simbólica entre posições
            levels.append(lambda x, i=i: int(
                all((x[j] ^ x[-(j+1)]) == (i % 2) for j in range(len(x)//2))
            ))

        elif i <= 40:
            # Simulação de agente com memória simbólica
            levels.append(lambda x, i=i: int(
                sum(x) % (i % 7 + 3) == sum([j % 2 for j in x])
            ))

        elif i <= 50:
            # Consistência entre múltiplos contextos (simulação de tempo)
            levels.append(lambda x, i=i: int(
                (sum(x[:len(x)//2]) - sum(x[len(x)//2:])) % (i % 4 + 2) == 0
            ))

        elif i <= 60:
            # Inferência reversa de causa (abdução simbólica)
            levels.append(lambda x, i=i: int(
                x[0] ^ (sum(x[1:]) % 2) == i % 2
            ))

        elif i <= 70:
            # Teoria da mente simulada (metarrepresentações)
            levels.append(lambda x, i=i: int(
                x[i % len(x)] == ((sum(x) + i) % 2)
            ))

        elif i <= 80:
            # Paradoxo temporal e autoengano
            levels.append(lambda x, i=i: int(
                (x[0] + x[-1] + i) % 3 == (x[len(x)//2] ^ 1)
            ))

        elif i <= 90:
            # Estrutura ontológica com loops cruzados
            levels.append(lambda x, i=i: int(
                all((x[j] ^ x[(j + i) % len(x)]) == (j % 2) for j in range(len(x)))
            ))

        elif i <= 97:
            # Auto negação simbolica
            levels.append(lambda x: int(
                not ((sum(x) % 2) == (sum([1 - i for i in x]) % 2))
            ))
        
        elif i <= 98:
            # Teoria da Mente com espelhamento recursivo
            levels.append(lambda x: int(
                ((x[0] ^ x[-1]) + x[len(x)//2]) % 2 == (x[1] ^ x[-2])
            ))
        
        elif i <= 99:
            # MEta- paridade temporo causal
            levels.append(lambda x: int(
                sum(x[:len(x)//2]) % 2 == sum(x[len(x)//2:][::-1]) % 2
            ))
        elif i <= 100:
            # Descontinuidade ontologica
            levels.append(lambda x: int(
                all(x[i] != x[i+1] for i in range(len(x)-1))  # rejeita padrões contínuos
            ))
        elif i <= 101:
            # Paradoxo do obersvador
            levels.append(lambda x: int(
                (sum(x) + x[0]) % 3 != x[-1]
            ))
        elif i <= 102:
            # agfente simulado em consciencia incompleta
            levels.append(lambda x: int(
                x[0] != x[len(x)//2] and x[-1] != (sum(x) % 2)
            ))
        elif i <= 103:
            #simulação subjetiva paradoxal
            levels.append(lambda x: int(
                (x[0] ^ x[-1]) != ((sum(x) + 1) % 2)
            ))
        elif i <= 104:
            # Reversao de consistencia em multiagente
            levels.append(lambda x: int(
                sum(x) == len(x) or sum(x) == 0  # todo mundo igual => inconsistente
            ))
        elif i <= 105:
            # Paradoxo da escolha
            levels.append(lambda x: int(
                x[len(x)//2] == (sum([i * x[i] for i in range(len(x))]) % 2)
            ))
        else:
            # Meta-paridade com raciocínio simbólico contínuo
            levels.append(lambda x, i=i: int(
                (sum([(a ^ b) for a, b in zip(x, x[::-1])]) + i) % 5 == 0
            ))

    return levels
