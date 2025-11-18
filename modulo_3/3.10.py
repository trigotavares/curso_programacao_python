set1 = set(input("primeiro conjunto: ").split(","))
set2 = set(input("segundo conjunto: ").split(","))

# elementos comuns

elementosComuns = set1.intersection(set2)

print(elementosComuns)

# elementos apenas da primeira lista

elementosApenasPrimeiraLista = set1.difference(set2)

print(elementosApenasPrimeiraLista)

# união dos dois conjuntos

juncaoDasDuas = set1.union(set2)

print(juncaoDasDuas)