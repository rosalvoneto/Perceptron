from Pattern import Pattern
from DadosAnd import DadosAnd
from DadosOr import DadosOr
from Mcp import Mcp
from DadosImpl import DadosImpl

# Primeiro commit

print("Escolha a funcao booleana")
print("1- And")
print("2- Or")
print("3- Imp")

op = int(input("Digite sua opcao:"))

if (op==1):
    And = DadosAnd()
    dados = And.getDados()
elif(op==2):
    Or = DadosOr()
    dados = Or.getDados()
else:
    Im = DadosImpl()
    dados = Im.getDados()
    
mcp = Mcp(0,0,0,0.4)


acerto = 0
while (acerto < 4):    
    acerto = 0
    for p in dados:
        out = mcp.output(p)
        if (out == p.y):
            acerto = acerto +1
        else:
            mcp.delta(p, out) 

print("Mcp Treinado!")
print("*"*50)        
print("W1: ", mcp.w1)
print("W2: ", mcp.w2)
print("Bias: ", mcp.w3)

print("*"*50)
print("Teste")
print("*"*50)
teste = 1
while (teste ==1):
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))
    p = Pattern(x1, x2, 0)    
    resp = mcp.output(p)
    print("Resposta: ", resp)
    teste = int(input("Para continuar testando digite 1"))