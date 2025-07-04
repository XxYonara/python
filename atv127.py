import atv127fc
cargo = str(input("Qual seu cargo ?"))

a = atv127fc.Analisar(cargo)
print(f"O cargo é {cargo} e seu sálario é {a}")

soma = int(a * 12)
print(f"A renda anual é {soma}")