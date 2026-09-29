import random

random.seed(42) 
turma = []

for i in range(1, 51):
    matricula = 1000 + i
    sexo = random.choice(['M', 'F'])
    altura = random.randint(150, 195)
    status = random.choice([1, 2, 3])
    turma.append({
        'matricula': matricula,
        'sexo': sexo,
        'altura': altura,
        'status': status
    })

qtd_feminino_alto = 0
total_masculino = 0
total_masculino_bom = 0

for aluno in turma:
    if aluno['sexo'] == 'F' and aluno['altura'] > 170:
        qtd_feminino_alto += 1
        
    if aluno['sexo'] == 'M':
        total_masculino += 1
        if aluno['status'] == 1:
            total_masculino_bom += 1

if total_masculino > 0:
    percent_masculino_bom = (total_masculino_bom / total_masculino) * 100
else:
    percent_masculino_bom = 0.0


print("=== RELATÓRIO DO DEPARTAMENTO DE EDUCAÇÃO FÍSICA ===")
print(f"a) Quantidade de alunas (F) com altura > 170 cm: {qtd_feminino_alto}")
print(f"b) Alunos do sexo masculino com status bom (1): {total_masculino_bom} de {total_masculino}")
print(f"   Porcentagem: {percent_masculino_bom:.2f}%")