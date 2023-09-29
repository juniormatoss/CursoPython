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