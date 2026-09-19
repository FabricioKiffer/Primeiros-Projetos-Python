# CARDÁPIO DE LANCHONETE

# ITEM:                      VALOR:            CÓDIGO:
# Hamburguer Tradicional     25,90             1001
# CheeseBurger               26,90             1002
# Batata Frita               15,80             1003
# Bauru Simples              22,00             1004
# Bauru Completo             28,00             1005
# Refrigerante               8,90              1006
# Suco                       13,90             1007

# BOAS VINDAS

print ('** FAÇA SEU PEDIDO! ')

# CARDÁPIO DE LANCHONETE

print("** FAÇA SEU PEDIDO! **")

cardapio = {
    1001: ("Hambúrguer Tradicional", 25.90),
    1002: ("Cheeseburger", 26.90),
    1003: ("Batata Frita", 15.80),
    1004: ("Bauru Simples", 22.00),
    1005: ("Bauru Completo", 28.00),
    1006: ("Refrigerante", 8.90),
    1007: ("Suco", 13.90),
}

carrinho = []
total = 0

while True:
    print("\n===== CARDÁPIO =====")

    for codigo, (produto, preco) in cardapio.items():
        print(f"{codigo} - {produto}: R$ {preco:.2f}")

    print("0 - Finalizar pedido")

    escolha = int(input("\nDigite o número do produto: "))

    if escolha == 0:
        break

    if escolha in cardapio:
        produto, preco = cardapio[escolha]

        carrinho.append(produto)
        total += preco

        print(f"{produto} adicionado ao pedido!")
    else:
        print("Opção inválida!")

print("\n===== PEDIDO FINAL =====")

print("Itens selecionados:")

for item in carrinho:
    print(f"- {item}")

print(f"\nTotal: R$ {total:.2f}")