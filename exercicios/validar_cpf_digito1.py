cpf = "74682489070"

nove_digitos = cpf[:9]
contagem1 = 10
total1 = 0  
for digito1 in nove_digitos:
    total1 += (int(digito1) * contagem1)
    contagem1 -= 1
    
segundocalculo1 = total1* 10
restodivisao1 = segundocalculo1 % 11
restodivisao1 = restodivisao1 if restodivisao1 <= 9 else 0
print(restodivisao1)



nove_digitos = cpf[:9] + str ('7')
contagem2 = 10
total2 = 0  
for digito2 in nove_digitos:
    total2 += (int(digito2) * contagem2)
    contagem2 -= 1
    
segundocalculo2 = total2* 10
restodivisao2 = segundocalculo2 % 11
restodivisao2 = restodivisao2 if restodivisao2 <= 9 else 0
print(restodivisao2)