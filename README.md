# Terminal Simulando um Sistema de Banco

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Uma interface via linha de comando para um sistema de banco apresentado para a disciplina de Linguagens de Programação, apresentado para fins avaliativos na disciplina de Linguagens de Programação no IFAL campus Arapiraca durante o ano de 2023

## Ferramentas Utilizadas

<div>
  <table>
    <tr>
      <th style="text-align:center">Python</th>
      <th style="text-align:center">Git</th>
      <th style="text-align:center">Pre-Commit</th>
    </tr>
    <tr>
      <td><a href="https://www.python.org"><img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" height="90" alt="Python" /></a></td>
      <td><a href="https://git-scm.com"><img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg" height="90" alt="Git" /></a></td>
      <td><a href="https://pre-commit.com"><img src="https://pre-commit.com/logo.svg" height="90" alt="Pre-Commit" /></a></td>
    </tr>
  </table>
</div>

### Pacotes Utilizados

<div>
  <table>
    <tr>
      <th style="text-align:center"><a href="https://pypi.org/project/bcrypt/">bcrypt</th>
      <th style="text-align:center"><a href="https://pypi.org/project/validate-docbr/">validate-docbr</th>
    </tr>
  </table>
</div>

## Como Rodar

1. Clone esse repositório na pasta desejada:

```bash
git clone https://github.com/Maheshivara/sistema-bancario-tela.git
```

2. Crie um ambiente virtual de python dentro da pasta 'sistema-bancario-tela' que foi criada:

```bash
cd sistema-bancario-tela
python -m venv .env
```

3. Inicie o ambiente virtual:

- Linux _(bash)_:

```bash
source ./.env/bin/activate
```

- Windows _(cmd)_:

```cmd
.env\Scripts\activate.bat
```

4. Instale as dependências usando o pip:

```bash
pip install -r requirements.txt
```

5. Prepare o pre-commit para o projeto:

```bash
pre-commit install
```

6. Execute o módulo main:

```bash
python -m src.main
```
