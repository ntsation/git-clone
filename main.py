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
        os.chdir(path)
        for repo_url in repos:
            repo_nome = repo_url.split('/')[-1].split('.')[0]
            repo_caminho = os.path.join(path, repo_nome)
            if not os.path.exists(repo_caminho):
                subprocess.run(['git', 'clone', repo_url])
                print("Repositório", repo_nome, "clonado com sucesso em", path)
            else:
                print("O repositório", repo_nome, "já existe em", path)
    else:
        print("Nenhum repositório encontrado para o usuário", user)

if __name__  == "__main__":
    user = 'SEU USUARIO'
    path = r'CAMINHO DA PASTA'
    clona_repos(user, path)
