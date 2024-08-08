l0 = []
ocorrencias = {}
total = 0
acumulada = 0
with open ("dados2.txt", 'r', encoding='utf-8') as dados:
    for i in dados:
        l0.append(i.rstrip())

for i in l0:
    if i in ocorrencias:
        ocorrencias[i] += 1
    else:
        ocorrencias[i] = 1

for i in ocorrencias.values():
    total += i

for chave,dados in ocorrencias.items():
    frequenciaRelativa = (dados / total) * 100
    ocorrencias[chave] = [dados,frequenciaRelativa]
    

ocorrenciasOrdenadas = sorted(ocorrencias.items(), key=lambda item: item[1], reverse=True)

for chave,dados in ocorrenciasOrdenadas:
    acumulada += dados[1] 
    print(f"{chave} || número de ocorrência: {dados[0]} || Frequência relativa: {dados[1]:.2f}% || frequência acumulada: {acumulada:.2f}")


    
    
# for chave,dados in l1.items():
#     print(f"{chave}: número de ocorrência: {dados}")

