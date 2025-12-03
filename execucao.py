import os


def executar_comando(args):
    """
    Recebe uma lista de argumentos (ex: ['ls', '-l']).
    Cria um processo filho e executa o comando.
    
    Args:
        args (list): Lista de argumentos onde args[0] é o comando
                     e os demais são os argumentos do comando.
    """
    try:
        pid = os.fork()

        if pid == 0:
            try:
                # os.execvp(programa, lista_de_argumentos)
                # args[0] é o nome do comando (ex: "ls")
                # args é a lista completa (ex: ["ls", "-l"])
                os.execvp(args[0], args)
                
            except FileNotFoundError:
                print(f"Erro: Comando '{args[0]}' não encontrado.")
                os._exit(1) 
            except OSError as e:
                print(f"Erro ao executar: {e}")
                os._exit(1)

        elif pid > 0:
            # os.wait() retorna uma tupla (pid, status).
            os.wait()

        else:
            print("Erro ao criar processo (fork falhou).")

    except OSError as e:
        print(f"Erro de sistema: {e}")

