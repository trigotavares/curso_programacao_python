# 1.19 & 1.20
IVA = 0.23

leite_preco = 0.95
leite_quantidade = 6

leite_iva = leite_preco * IVA
print(f"IVA 1 leite: {leite_iva}")
leite_unico = leite_preco + leite_iva
print(f"1 leite: {leite_unico}")
print(f"6 leite: {6 * leite_unico}")


granola_preco = 2.23
granola_quantidade = 2

granola_iva = granola_preco * IVA
print(f"IVA 1 granola: {granola_iva}")
granola_unico = granola_preco + granola_iva
print(f"1 granola: {granola_unico}")
print(f"2 granola: {2 * granola_unico}")

preco_final = (leite_preco + leite_preco * IVA) * leite_quantidade + (granola_preco + granola_preco * IVA) * granola_quantidade
print(preco_final)