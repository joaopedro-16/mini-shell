# Mini-Shell

Este é um projeto de uma shell simples implementada em Python.

## Como compilar e rodar

Como o projeto é desenvolvido em Python, não é necessário compilação prévia. Para executar o shell, certifique-se de ter o Python 3 instalado e execute o seguinte comando no terminal:

```bash
python3 shell.py
```

## Chamadas ao sistema utilizadas

O código faz uso direto de chamadas de sistema (system calls) através da biblioteca `os` do Python para gerenciar processos e entrada/saída:

*   `os.fork()`: Utilizada para criar um processo filho. O shell (processo pai) cria uma cópia de si mesmo para executar comandos sem ser substituído.
*   `os.execvp(file, args)`: Utilizada no processo filho para substituir a imagem do processo atual pelo programa especificado no comando.
*   `os.wait()`: Utilizada pelo processo pai para aguardar a conclusão da execução do processo filho antes de exibir o prompt novamente.
*   `os.read(fd, n)`: Utilizada para ler a entrada do usuário diretamente do descritor de arquivo 0 (stdin).
*   `os.write(fd, str)`: Utilizada para escrever o prompt e mensagens de saída no descritor de arquivo 1 (stdout).
*   `os._exit(n)`: Utilizada para encerrar o processo filho imediatamente em caso de erro, sem acionar manipuladores de limpeza do Python (que poderiam afetar o pai).

## Exemplos de comandos testados e suas saídas

Abaixo estão alguns exemplos de como o shell se comporta:

1.  **Listagem de arquivos simples:**
    ```text
    myshell> ls
    README.md  shell.py
    ```

2.  **Listagem com argumentos:**
    ```text
    myshell> ls -l
    total 8
    -rw-r--r-- 1 user user 123 Nov 30 10:00 README.md
    -rw-r--r-- 1 user user 456 Nov 30 10:00 shell.py
    ```

3.  **Comando echo:**
    ```text
    myshell> echo Olá Mundo
    Olá Mundo
    ```

4.  **Comando inexistente:**
    ```text
    myshell> xyz
    Erro: Comando 'xyz' não encontrado.
    ```

5.  **Sair do shell:**
    ```text
    myshell> exit
    Saindo...
    ```

## Limitações conhecidas

Esta implementação é um shell básico e possui as seguintes limitações em comparação com shells completos (como bash ou zsh):

*   **Navegação de Diretórios (`cd`):** O comando `cd` não está implementado internamente (built-in). Tentar executar `cd` falhará ou não terá efeito persistente, pois o comando seria executado em um processo filho.
*   **Pipes e Redirecionamento:** Não há suporte para pipes (`|`) ou redirecionamento de entrada/saída (`>`, `<`).
*   **Execução em Background:** Não suporta o operador `&` para rodar processos em segundo plano.
*   **Histórico e Autocomplete:** Não possui histórico de comandos (setas para cima/baixo) nem autocompletar com Tab.
*   **Variáveis de Ambiente:** Não permite definir ou exportar variáveis de ambiente diretamente.
