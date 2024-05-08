import random as rd
pontos1=0.0
pontos2=0.0
while pontos1<3 and pontos2<3:
  A=int(input("Escolha um número de 1 a 6: "))
  B=rd.randint(1,6)
  D=rd.randint(1,6)
  if A!=B:
    if A==D:
     pontos1=pontos1+1
     print("Valor escolhido pelo jogador 1: ",A)
     print("Valor escolhido pelo jogador 2: ",B) 
     print("Valor sorteado no dado: ",D)
     print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
    elif B==D:
     pontos2=pontos2+1
     print("Valor escolhido pelo jogador 1: ",A)
     print("Valor escolhido pelo jogador 2: ",B) 
     print("Valor sorteado no dado: ",D)
     print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
    elif A!=D and B!=D:
      if D==1 or D==2 or D==3:
        pontos1=pontos1+1
        print("Valor escolhido pelo jogador 1: ",A)
        print("Valor escolhido pelo jogador 2: ",B) 
        print("Valor sorteado no dado: ",D)
        print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
      elif D==4 or D==5 or D==6:
        pontos2=pontos2+1
        print("Valor escolhido pelo jogador 1: ",A)
        print("Valor escolhido pelo jogador 2: ",B) 
        print("Valor sorteado no dado: ",D)
        print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
  elif A==B:
    if D==1 or D==2 or D==3:
      pontos1=pontos1+1
      print("Valor escolhido pelo jogador 1: ",A)
      print("Valor escolhido pelo jogador 2: ",B) 
      print("Valor sorteado no dado: ",D)
      print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
    elif D==4 or D==5 or D==6:
      pontos2=pontos2+1
      print("Valor escolhido pelo jogador 1: ",A)
      print("Valor escolhido pelo jogador 2: ",B) 
      print("Valor sorteado no dado: ",D)
      print("Jogador 1 tem ",pontos1," ponto(s) e o jogador 2 tem ",pontos2," ponto(s).")
if pontos1==3:
  print("Parabéns, jogador 1!")
elif pontos2==3:  
  print("Parabéns, jogador 2!")