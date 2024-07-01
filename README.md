# Git clone

Este script Python é uma ferramenta simples para clonar todos os repositórios públicos de um usuário do GitHub para um diretório local.

## Requisitos

Certifique-se de ter instalado os seguintes pacotes Python:

- requests: para fazer solicitações HTTP.
subprocess: para executar comandos do sistema operacional.
os: para interagir com o sistema de arquivos.
Você pode instalar esses pacotes usando o pip:

```cmd
pip install requests
```

## Uso

1. Especifique o caminho do diretório local onde deseja clonar os repositórios.

2. Execute o script main.py.

3. Digite o nome de usuário do GitHub quando solicitado.

O script então obterá os repositórios do usuário fornecido, clonará cada um deles no diretório especificado e exibirá uma mensagem indicando o sucesso ou falha da operação.

### Exemplo de Uso

```cmd
python clone_repos.py
```

```cmd
Digite o nome de usuário do Github: user_exemplo
```

### Observações

Certifique-se de ter permissões adequadas para clonar os repositórios.
Os repositórios clonados serão armazenados em um diretório com o nome do usuário do GitHub fornecido.
