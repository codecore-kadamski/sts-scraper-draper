# sts-scraper-draper


poetry cache:clear --all pypi

#### Instalation
1. Use poetry for packages management.
2. Use pre-commit hooks. To install it add pre-commit package to system `sudo pip3 install pre-commit` and install hooks
`pre-commit install`. Installed hooks:
    * black - python code formater
    * mypy - python typing checker 
    * isort - python library to sort imports 
3. Each project should contain `Dockerfile` and `docker-compose.yaml` for development setup (if needed).
4. Shared settings are stored in `config.base`. Each project should import from that file and add its own settings.



Docker Registry

docker login docker.pkg.github.com -u codecore-kadamski -p 4dd929a0e888c7a3c544ca2de0581262d46fd269

docker login docker.pkg.github.com -u codecore-kadamski --password-stdin 4dd929a0e888c7a3c544ca2de0581262d46fd269


poetry cache:clear pypy --all

