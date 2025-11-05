# PROJETO 13 — Relatório de Vendas

# Criar uma lista para armazenar as vendas
vendas = []

# Loop para receber dados
while True:
    print("\n--- Cadastro de Venda ---")
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))
    preco = float(input("Preço unitário (R$): "))

    # Armazena cada venda como um dicionário
    venda = {
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco,
        "total": quantidade * preco
    }
    vendas.append(venda)

    continuar = input("Deseja cadastrar outra venda? (s/n): ").lower()
    if continuar == 'n':
        break

# --- Cálculos ---
total_vendido = sum(v["total"] for v in vendas)
media_faturamento = total_vendido / len(vendas)

# Encontrar o produto mais vendido (maior quantidade)
mais_vendido = max(vendas, key=lambda v: v["quantidade"])

# --- Relatório Final ---
print("\n========== RELATÓRIO DE VENDAS ==========")
print(f"Total de vendas registradas: {len(vendas)}")
print(f"Faturamento total: R$ {total_vendido:.2f}")
print(f"Média de faturamento por venda: R$ {media_faturamento:.2f}")
print(f"Produto mais vendido: {mais_vendido['produto']} ({mais_vendido['quantidade']} unidades)")
print("==========================================")
