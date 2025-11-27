import os
import sys

# --- MÓDULO DE LEITURA E PARSING ---
def ler_comando():
    """
    Exibe o prompt, lê a entrada do usuário usando os.read 
    e retorna uma lista com comando e argumentos.
    """
    prompt = b"myshell> "
    
    try:
        # Requisito obrigatório: Usar write para saída
        os.write(1, prompt) 
        
        # Requisito obrigatório: Usar read para entrada
        # Lê até 1024 bytes do descritor 0 (stdin/teclado)
        entrada_bytes = os.read(0, 1024)
        
        # Se entrada_bytes for vazio, significa EOF (Ctrl+D)
        if not entrada_bytes:
            return None
            
        # Decodifica bytes para string e remove espaços/quebras de linha nas pontas
        entrada_str = entrada_bytes.decode().strip()
        
        # Se o usuário só deu Enter sem digitar nada
        if not entrada_str:
            return []
            
        # Separa a string em pedaços (tokenização)
        # Ex: "ls -l /home" vira ['ls', '-l', '/home']
        argumentos = entrada_str.split()
        
        return argumentos

    except OSError as e:
        print(f"Erro na leitura: {e}")
        return None

# --- MÓDULO PRINCIPAL (LOOP) ---
def main():
    while True:
        # 1. Leitura
        args = ler_comando()
        
        # Verifica se deve encerrar (Ctrl+D)
        if args is None:
            os.write(1, b"\nSaindo do shell...\n")
            break
            
        # Verifica se o usuário deu enter vazio
        if len(args) == 0:
            continue
            
        # Verifica comando de saída explícito
        if args[0] == "exit":
            os.write(1, b"Saindo do shell...\n")
            break
            
        # 2. Por enquanto, apenas mostramos o que foi lido (Debug)
        print(f"Comando lido: {args}")

if __name__ == "__main__":
    main()