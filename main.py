import requests
import subprocess
import os


def pega_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    r = requests.get(url)
    if r.status_code == 200:
        repos = r.json()
        return [repo['clone_url'] for repo in repos]
    else:
        print("Erro ao obter os repositórios:", r.status_code)
        return None


def clona_repos(user, path):
    repos = pega_repos(user)
    if repos:
        os.makedirs(path, exist_ok=True)
        for repo_url in repos:
            repo_nome = repo_url.split('/')[-1].split('.')[0]
            repo_caminho = os.path.join(path, repo_nome)
            if not os.path.exists(repo_caminho):
                os.chdir(path)
                subprocess.run(['git', 'clone', repo_url])
                print("Repositório", repo_nome, "clonado com sucesso.")
            else:
                print("O repositório", repo_nome, "já existe em", path)
                os.chdir(repo_caminho)
                # Check if the directory is empty
                if not os.listdir(repo_caminho):
                    subprocess.run(['git', 'pull', '--force'])
                    print("Repositório", repo_nome, "atualizado com sucesso.")
                else:
                    print("O repositório", repo_nome, "não está vazio. Não foi possível atualizar automaticamente.")
    else:
        print("Nenhum repositório encontrado para o usuário", user)


if __name__ == "__main__":
    user = 'ntsation'
    path = r'/home/ntsation/repos'
    clona_repos(user, path)
