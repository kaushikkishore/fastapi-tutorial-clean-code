### Getting started

To create a virtual env
`python3 -m venv env`

### To activate the virtual env

`sudo chmod -R 755  ./.venv/bin
source .venv/bin/activate`

### To deactivate a venv

`deactivate`

### To install dependencies

pip install -r requirements.txt

## To started with conda

- Install [minikonda](https://docs.anaconda.com/free/miniconda/)
- `conda create -n <env-name> python=3.12`
- To actiavte `conda activate <experiments>`

To manage use these commands

# via environment activation

```
conda activate myenvironment
conda install matplotlib
```

# via command line option

`conda install --name myenvironment matplotlib`

# via pip

`pip install fastapi`

# specifying channels

`conda install conda-forge::numpy`

# to deactivate the environment

`conda deativate `

# to install poetry

`curl -sSL https://install.python-poetry.org | python -`

# to activate the poetry

`export PATH="$HOME/.local/bin:$PATH"`

# Creating an env file

create a .env file at root level.
Add `DATABASE_CONNECTION` and a valid db connection to connect to postgres db. Then create the table and then you are ready to go.

# Table create

```SQL
CREATE TABLE example_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

```
