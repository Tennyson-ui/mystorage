# Relatorio de preparacao do workspace SWOT - Atividade 3

## 1. O que foi criado?

Foi criada a estrutura limpa da atividade em `atividade3_swot/`, com pastas para notebooks, codigo auxiliar, pontos, dados, resultados e documentacao.

Arquivos novos criados:

- `atividade3_swot/.gitignore`
- `atividade3_swot/requirements.txt`
- `atividade3_swot/README.md`
- `atividade3_swot/pontos/README.md`
- `atividade3_swot/src/check_environment.py`
- `atividade3_swot/notebooks/trabalho/00_verificar_ambiente.ipynb`
- `atividade3_swot/docs/RELATORIO_PREPARACAO_WORKSPACE_SWOT.md`

## 2. O que foi copiado?

Foram copiadas para `atividade3_swot/notebooks/originais/` as seis fontes principais da atividade SWOT:

- `swot_download_earthdata_draw_inmap_training_EN.ipynb`
- `swot_download_earthdata_rectangle_vietnam_training_EN.ipynb`
- `swot_courses_tile_visualizer_training_EN.ipynb`
- `open_swot_PIXC_training_EN.ipynb`
- `curso_swot_reaches_timeseries_training_EN.ipynb`
- `curso_swot_lake_timeseries_training_EN.ipynb`

As copias foram comparadas por SHA-256 com os arquivos em `alunos/alunos/scripts` e todos os hashes bateram.

## 3. O que foi preservado?

Foram preservados sem modificacao:

- `alunos/`
- `alunos.rar`
- `aulas/`
- `docs/`
- `geo2/`
- materiais das atividades 1 e 2
- notebooks originais em `alunos/alunos/scripts`

Nao houve download de dados SWOT, autenticacao Earthdata, execucao de notebooks de analise nem alteracao de historico Git.

## 4. Como ficou a estrutura?

```text
atividade3_swot/
├── notebooks/
│   ├── originais/
│   └── trabalho/
├── src/
├── pontos/
├── dados/
│   ├── raw/
│   ├── intermediarios/
│   └── referencias/
├── outputs/
│   ├── tabelas/
│   ├── figuras/
│   ├── vetores/
│   └── logs/
├── docs/
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Quais dependencias foram identificadas?

O `requirements.txt` foi montado com base na lista solicitada e nos imports reais dos notebooks SWOT:

- `earthaccess`
- `xarray`
- `netCDF4`
- `h5netcdf`
- `pandas`
- `geopandas`
- `shapely`
- `pyproj`
- `matplotlib`
- `ipyleaflet`
- `ipywidgets`
- `fiona`
- `pyogrio`
- `numpy`
- `requests`
- `pyarrow`

O teste local em Windows/Anaconda executou o script `python src/check_environment.py`. O script funcionou, mas apontou pendencias locais:

- ausente: `netCDF4`
- ausente: `h5netcdf`
- ausente: `ipyleaflet`
- ausente: `fiona`

No mesmo teste local, foram importados com sucesso: `earthaccess`, `xarray`, `pandas`, `geopandas`, `shapely`, `pyproj`, `matplotlib`, `ipywidgets`, `pyogrio`, `numpy`, `requests` e `pyarrow`.

## 6. Como configurar o JupyterLab Copernicus?

No JupyterLab do Copernicus Data Space, acessar:

```text
https://jupyterhub.dataspace.copernicus.eu/
```

Depois, no Terminal do JupyterLab:

```bash
cd ~/mystorage

git clone <URL_DO_REPOSITORIO>

cd <REPOSITORIO>/atividade3_swot

python -m pip install --upgrade pip
pip install -r requirements.txt

python src/check_environment.py
```

Usar `~/mystorage/` porque arquivos fora dessa area nao tem garantia de persistencia entre sessoes.

## 7. Como sincronizar com VS Code via Git?

O workspace principal foi verificado e nao e um repositorio Git local neste momento.

Quando houver repositorio Git configurado, o fluxo recomendado e:

```bash
git pull
git status
git add atividade3_swot
git commit -m "Prepare workspace da atividade SWOT"
git push
```

No VS Code local, editar e versionar codigo, notebooks e documentacao. No JupyterLab Copernicus, fazer `git pull`, executar o processamento remoto e usar `git push` apenas para codigo/documentacao/notebooks e derivados leves apropriados.

## 8. O que fica fora do Git?

O `.gitignore` de `atividade3_swot` exclui:

- `dados/raw/`
- `dados/intermediarios/`
- arquivos `*.nc`
- arquivos `*.zip`
- arquivos `*.h5`
- arquivos `*.hdf`
- arquivos `*.tif`
- arquivos `*.tiff`
- checkpoints Jupyter
- caches Python
- ambientes virtuais
- temporarios de logs

Nao foram excluidos notebooks, scripts, README, documentacao, CSVs pequenos derivados, GeoPackages pequenos derivados ou figuras relevantes.

## 9. Onde ficam os produtos SWOT brutos?

Os produtos SWOT brutos devem ficar em:

```text
atividade3_swot/dados/raw/
```

No Copernicus, essa pasta deve estar dentro de `~/mystorage/`, por exemplo:

```text
~/mystorage/PPGGAG1889/<REPOSITORIO>/atividade3_swot/dados/raw/
```

Esses dados sao pesados, descartaveis e nao versionados.

## 10. Onde ficam os resultados?

Os derivados finais devem ficar em:

- `atividade3_swot/outputs/tabelas/`
- `atividade3_swot/outputs/figuras/`
- `atividade3_swot/outputs/vetores/`
- `atividade3_swot/outputs/logs/`

Resultados leves e relevantes podem ser versionados quando fizer sentido. Produtos brutos devem permanecer fora do Git.

## 11. Qual e o proximo teste recomendado?

O proximo teste recomendado e executar, no JupyterLab Copernicus, primeiro:

```bash
python src/check_environment.py
```

Depois abrir:

```text
notebooks/trabalho/00_verificar_ambiente.ipynb
```

Esse teste verifica imports, versao do Python, diretorio atual, escrita em `outputs/logs`, `earthaccess`, `xarray`, `geopandas`, `ipywidgets` e `ipyleaflet`, sem autenticar e sem baixar dados.

Somente depois disso deve-se criar os notebooks futuros:

1. `01_testar_observabilidade_pontos.ipynb`
2. `02_baixar_passagem_teste.ipynb`
3. `03_classificar_estado_observacional.ipynb`
4. `04_serie_temporal_sazonalidade.ipynb`

## Validacao final

- Estrutura `atividade3_swot/` criada.
- Seis notebooks originais copiados e preservados por hash.
- `requirements.txt` criado com dependencias coerentes.
- `.gitignore` criado para excluir dados pesados e caches.
- `00_verificar_ambiente.ipynb` e JSON valido.
- `src/check_environment.py` executa localmente e relata dependencias ausentes.
- Nenhum produto SWOT bruto foi criado.
- Nenhum material original foi alterado.
