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
