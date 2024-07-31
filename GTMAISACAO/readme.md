# MVP GT Mais Ação (Django Edition)

Essa é a branch relativa à versão em Django do MVP, onde testamos na prática em segundo plano os conceitos modelados e testados no protótipo inicial — vulgo WP.

## FAQ

### Como acessar essa branch?

```sh
git switch mvp-django
```

### Repositório local desatualizado?

1. Puxar commits

```sh
git pull
```

2. Acessar ambiente virtual (venv)

```sh
.\myenv\Scripts\Activate.ps1 (powershell)
.\myenv\Scripts\activate.bat (cmd)
```

3. Baixar módulos

```sh
pip install -r GTMais\requirements.txt
```

### Repositório remoto sem módulos

Inclua eles manualmente no requirements.txt ou:

```sh
python3 -m pip freeze > requirements.txt
```
