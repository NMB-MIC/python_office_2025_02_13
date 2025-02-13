# Setup program

##  miniconda
#### setup
```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```
#### command
- create env
```
conda create -n python_office python

conda create -n python_office python==3.11
```
- activate
```
conda activate python_office
```
- deactivate
```
conda deactivate 
```
- check env
```
conda env list
```
- remove env
```
conda remove --name python_office --all
```

- list
```
conda list
```

- install pandas 
```
pip install pandas
```

- uninstall pandas 
```
pip uninstall pandas
```
## vscode extension
```
Python Extension Pack
Jupyter
Dracula theme Official
```
