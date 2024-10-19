print ("Bem vindo a Madeleira do Lenhador André Pereira!")

def escolha_tipo():
    while True:
        print("\nEntre com o Tipo de Madeira desejado:")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        tipo = input(">>")
        if tipo =="PIN":
          return 150.40
        elif tipo == "PER":
          return 170.20
        elif tipo == "MOG":
          return 190.90
        elif tipo == "IPE":
          return 210.10
        elif tipo == "IMB":
          return 220.70
        else:
            print  ("Escolha errada, entre novamente com o modelo!")
def qtd_toras():
    while True:
        try:
            qtd = int(input("Entre com a quantidade de toras (m³): "))
            if qtd>2000:
               print ("Não aceitamos pedidos com essa quantidade de toras")
            elif qtd < 100:
                return qtd, 0
            elif 100 <= qtd < 500:
                return qtd, 0.04 
            elif 500 <=qtd <1000:
              return qtd, 0.09 
            elif 1000 <= qtd <= 2000:
                return qtd, 0.16
        except ValueError:
            print ("Por favor, insira um valor numérico válido")

def transporte():
    while True:
       print("\nEscolha o tipo de transporte: ")
       print("1 - Transporte Rodoviário - R$1000.00")
       print("2 - Transporte Ferroviário - R$2000.00")
       print("3 - Transporte Hidroviário - R$2500.00")

       opcao = input(">>")
       if opcao == "1":
         return 1000.00
       elif opcao == "2":
         return 2000.00
       elif opcao =="3":
         return 2500.00

if __name__ == "__main__":
    valor_madeira = escolha_tipo()

qtd, desconto = qtd_toras()

valor_transporte = transporte()

total = ((valor_madeira * qtd) * (1 - desconto)) + valor_transporte

print("Total: R$ {:.2f}".format(total))
