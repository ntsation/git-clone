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
            subprocess.run(['git', 'clone', repo_url])
        print("Todos os repositórios foram clonados com sucesso em", path)
    else:
        print("Nenhum repositório encontrado para o usuário", user)

if __name__  == "__main__":
    user = input("Digite o nome de usuário do Github: ")
    path = r''
    clona_repos(user, path)

    