# Relatorio de fechamento Git - Atividade 3 SWOT

## 1. Git foi inicializado?

Sim. O Git foi inicializado localmente apenas dentro da pasta da atividade 3.

## 2. Qual pasta virou repositorio?

A pasta transformada em repositorio Git independente foi:

```text
D:\unb\Mestrado\TÓPICOS EM GEOPROCESSAMENTO E ANÁLISE AMBIENTAL 2\atividade3_swot
```

O workspace principal da disciplina nao foi inicializado como repositorio Git.

## 3. Quais arquivos ficaram versionados?

Foram preparados para versionamento:

- `.gitignore`
- `README.md`
- `requirements.txt`
- `src/check_environment.py`
- `pontos/README.md`
- `docs/RELATORIO_PREPARACAO_WORKSPACE_SWOT.md`
- `docs/RELATORIO_FECHAMENTO_GIT_SWOT.md`
- `notebooks/trabalho/00_verificar_ambiente.ipynb`
- os seis notebooks preservados em `notebooks/originais/`

Notebooks originais versionados:

- `notebooks/originais/swot_download_earthdata_draw_inmap_training_EN.ipynb`
- `notebooks/originais/swot_download_earthdata_rectangle_vietnam_training_EN.ipynb`
- `notebooks/originais/swot_courses_tile_visualizer_training_EN.ipynb`
- `notebooks/originais/open_swot_PIXC_training_EN.ipynb`
- `notebooks/originais/curso_swot_reaches_timeseries_training_EN.ipynb`
- `notebooks/originais/curso_swot_lake_timeseries_training_EN.ipynb`

## 4. Quais ficaram fora?

O `.gitignore` deixa fora:

- `dados/raw/`
- `dados/intermediarios/`
- arquivos `*.nc`
- arquivos `*.zip`
- arquivos `*.h5`
- arquivos `*.hdf`
- arquivos `*.tif`
- arquivos `*.tiff`
- `.ipynb_checkpoints/`
- `__pycache__/`
- `*.pyc`
- `.venv/`
- `venv/`
- `env/`
- temporarios em `outputs/logs/*.tmp`
- logs em `outputs/logs/*.log`

## 5. O `.gitignore` esta funcionando?

Sim. Antes do commit foi verificado que nao havia arquivos brutos com extensoes `.nc`, `.zip`, `.h5`, `.hdf`, `.tif` ou `.tiff` dentro do repositorio.

Tambem foi verificado, com `git ls-files`, que nenhum arquivo pesado ou ignorado estava staged.

## 6. O primeiro commit foi criado?

Sim. O commit inicial local foi criado com a mensagem:

```text
Prepare workspace SWOT activity 3
```

## 7. O remoto foi configurado?

Nao. Conforme solicitado, nenhum remoto foi configurado automaticamente.

## 8. Se nao, o que falta?

Falta criar ou escolher o repositorio remoto e informar a URL. Quando a URL estiver disponivel, usar:

```bash
git remote add origin <URL_DO_REPOSITORIO>
git branch -M main
git push -u origin main
```

## 9. Qual comando deve ser usado no Copernicus?

No Terminal do JupyterLab Copernicus:

```bash
cd ~/mystorage
mkdir -p PPGGAG1889
cd PPGGAG1889

git clone <URL_DO_REPOSITORIO> atividade3_swot

cd atividade3_swot

python -m pip install --upgrade pip
pip install -r requirements.txt

python src/check_environment.py
```

Depois abrir:

```text
notebooks/trabalho/00_verificar_ambiente.ipynb
```

## 10. Qual e o proximo passo depois do clone remoto?

O proximo passo e testar o ambiente no Copernicus, sem baixar dados:

1. Rodar `python src/check_environment.py`.
2. Abrir `notebooks/trabalho/00_verificar_ambiente.ipynb`.
3. Confirmar imports, escrita em `outputs/logs` e funcionamento de `ipywidgets`/`ipyleaflet`.
4. Somente depois iniciar a preparacao dos notebooks futuros.

Ainda nao devem ser executados nesta etapa:

- autenticacao Earthdata;
- `earthaccess.download`;
- download de produtos SWOT;
- processamento PIXC;
- processamento RiverSP;
- processamento LakeSP;
- analise sazonal.

## Comandos finais de sincronizacao

No VS Code local:

```bash
git pull
git status
git add .
git commit -m "Mensagem objetiva da alteracao"
git push
```

No JupyterLab Copernicus:

```bash
cd ~/mystorage/PPGGAG1889/atividade3_swot

git pull

# executar notebooks / editar codigo

git status
git add notebooks src docs outputs
git commit -m "Mensagem objetiva da alteracao"
git push
```

Regra operacional: Git guarda codigo, notebooks, documentacao e derivados leves. `mystorage` guarda dados SWOT brutos, intermediarios e outputs. Windows local guarda a copia do repositorio e resultados finais necessarios.
