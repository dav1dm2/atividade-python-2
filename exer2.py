print("bem vindo ao consultor de descontos :)\n")
print("desconto disponivel: 15%\n")

while True:
    preço = input("digite o valor do produro para consultar o valor da promoção: ")

    try:
        preço_descoto = float(preço) * (1 - 0.15 )
        preço_descontado = float(preço) * 0.15
        print(f"\no valor atual do produto é: {preço_descoto} R$\n valor economizado: {preço_descontado} R$ ")
        break
    
    except ValueError:
        print("Error: valor não numerico")
