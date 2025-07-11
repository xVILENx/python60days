#threads

import threading
import time

def tarefa(nome, tempo_execucao):
    print(f"Tarefa {nome} iniciada...")
    time.sleep(tempo_execucao)
    print(f"Tarefa {nome} finalizada.")
    
thread1 = threading.Thread(target = tarefa, args=("Download tarefa 1", 3))
thread2 = threading.Thread(target = tarefa, args=("Download tarefa 2", 6))

# iniciando threads
thread1.start()
thread2.start()

# aguardando as tarefas finalizarem
thread1.join()
thread2.join()

print("Todas as tarefas foram finalizadas.")

# Sem ser multi tarefas ao mesmo tempo:
# print(tarefa("Download 1", 3))
# print(tarefa("Download 2", 6))
