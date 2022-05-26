print("-----------------------------------------------")
print("Converta um número decimal para outras bases!  ")
print("-----------------------------------------------")
print()

while True:
    numero= int(input( 'Digite um número decimal:'))
    binario=""
    octal=""
    inteiro = numero
    hexadecimal= ""
    conv_hex = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

    resposta='s'


    while resposta == 's': 


     print("-------------------------------------")
     print('''escolha uma das bases para conversão:
     [1] converter para binario
     [2] converter para hexadecimal
     [3] converter para octadecimal
     [0] cancelar''')
     opção = int(input('escolha sua opção:'))
     print("----------------------------------------------")

     if opção == 1:
      while numero!=0: 
       r = numero % 2
       binario = str(r) + binario
       numero = numero//2
      print("O decimal digitado equivale a %s na base 2." %binario)
      break
      

     elif opção == 2:
       while numero!=0:
        r = numero % 16
        hexadecimal = conv_hex[r] + hexadecimal
        numero = numero//16
       print("O decimal digitado equivale a %s na base 16." %hexadecimal)
       break
       

     elif opção == 3:
      while numero!=0: 
       r = numero % 8
       octal = str(r) + octal
       numero = numero//8
      print("O decimal digitado equivale a %s na base 8." %octal)
      break

     elif opção == 0:
      print ('Fim da operação!')
      break

     else:
      print ('opção inválida tente novamente!')  

    print("----------------------------------------------")
    print("deseja converter outros valores? ")
    print()
    resposta= input("digite 's' para sim ou 'n' para não: ")
    print("--------------------------------------")

    if resposta =='n':
     print("________________")
     print("fim da operação!")
     print("________________")
     break