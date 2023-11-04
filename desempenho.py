import time
import 
# Inicia a contagem de tempo
start_time = time.time()

# Código que você quer medir o tempo de execução
# Por exemplo, vamos usar um loop simples para simular alguma operação demorada
for _ in range(1000000):
    pass

# Finaliza a contagem de tempo
end_time = time.time()

# Calcula o tempo total
elapsed_time = end_time - start_time

# Imprime o tempo total
print(f"Tempo decorrido: {elapsed_time} segundos")
