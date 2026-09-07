# Atividade 3 SWOT - PPGGAG1889

## Objetivo

Preparar um ambiente limpo e versionavel para analise SWOT de aguas superficiais, com processamento remoto no JupyterLab do Copernicus Data Space e acesso aos dados por NASA Earthdata / PO.DAAC usando `earthaccess`.

## Arquitetura

```text
VS Code local
<-> Git
JupyterLab Copernicus
↓
earthaccess
↓
NASA Earthdata / PO.DAAC
↓
SWOT bruto remoto
↓
processamento Python
↓
derivados
```

## Principio

- codigo, notebooks e documentacao versionados;
- dados brutos nao versionados;
- processamento pesado remoto;
- resultados derivados persistidos;
- apenas derivados necessarios baixados localmente.

## Estrutura das pastas

- `notebooks/originais/`: copias preservadas dos notebooks SWOT recebidos.
- `notebooks/trabalho/`: notebooks adaptados para execucao da atividade.
- `src/`: scripts auxiliares reutilizaveis.
- `pontos/`: futura entrada de pontos de exutorio ou locais de interesse.
- `dados/raw/`: produtos SWOT brutos, pesados e descartaveis.
- `dados/intermediarios/`: arquivos reprocessaveis gerados durante o fluxo.
- `dados/referencias/`: bases auxiliares leves ou documentadas.
- `outputs/tabelas/`: CSVs e tabelas finais derivadas.
- `outputs/figuras/`: graficos e figuras finais.
- `outputs/vetores/`: GeoPackages e outros vetores derivados.
- `outputs/logs/`: logs de execucao.
- `docs/`: relatorios e notas tecnicas da atividade.

## Ambiente remoto

O ambiente remoto previsto e o JupyterLab do Copernicus Data Space:

```text
https://jupyterhub.dataspace.copernicus.eu/
```

No Copernicus, trabalhe dentro de:

```bash
~/mystorage/
```

Arquivos fora de `mystorage` nao tem garantia de persistencia. A area persistente tem aproximadamente 10 GB e e preservada por 30 dias a partir do ultimo login. Downloads SWOT devem ir para uma pasta dentro de `mystorage`, e os resultados devem ser salvos em `outputs`.

## Comandos no JupyterLab Copernicus

Use o Terminal do JupyterLab:

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

Depois abra:

```text
notebooks/trabalho/00_verificar_ambiente.ipynb
```

Nao foi definida uma URL Git nesta preparacao. Substitua `<URL_DO_REPOSITORIO>` pela URL real quando o repositorio remoto existir.

## Configuracao do remoto Git

Quando a URL do repositorio remoto estiver disponivel, configure a partir da raiz de `atividade3_swot`:

```bash
git remote add origin <URL_DO_REPOSITORIO>
git branch -M main
git push -u origin main
```

Nao use Git como armazenamento de dados cientificos pesados.

## Fluxo recomendado de dados

```text
Copernicus JupyterLab
↓
earthaccess
↓
NASA Earthdata / PO.DAAC
↓
produto SWOT bruto em mystorage/dados/raw
↓
processamento Python
↓
derivados em outputs
↓
download local apenas do resultado
```

## Principio de dados

RAW = descartavel / pesado / nao versionado

INTERMEDIARIO = reprocessavel / preferencialmente nao versionado

OUTPUT = derivado leve / persistente / versionavel quando apropriado

Dados brutos podem ser removidos apos a geracao dos derivados se houver necessidade de espaco.

## Sequencia planejada

A analise sazonal ainda nao foi iniciada. A sequencia futura planejada e:

1. `00_verificar_ambiente.ipynb`
2. `01_testar_observabilidade_pontos.ipynb`
3. `02_baixar_passagem_teste.ipynb`
4. `03_classificar_estado_observacional.ipynb`
5. `04_serie_temporal_sazonalidade.ipynb`

Nesta etapa foi criado apenas o notebook `00_verificar_ambiente.ipynb`.

## Sincronizacao com VS Code e Git

Edite codigo, notebooks e documentacao localmente no VS Code. Sincronize com o JupyterLab Copernicus por Git:

### No VS Code local

```bash
git pull
git status
git add .
git commit -m "Mensagem objetiva da alteracao"
git push
```

### No JupyterLab Copernicus

```bash
cd ~/mystorage/PPGGAG1889/atividade3_swot

git pull

# executar notebooks / editar codigo

git status
git add notebooks src docs outputs
git commit -m "Mensagem objetiva da alteracao"
git push
```

Antes de qualquer commit, confira `git status`. Nao adicione `dados/raw/`, `dados/intermediarios/`, NetCDF, ZIP, HDF ou GeoTIFF pesado.

## Regra de dados

Git:

- codigo;
- notebooks;
- documentacao;
- derivados leves.

`mystorage`:

- dados SWOT brutos;
- intermediarios;
- outputs.

Windows local:

- copia do repositorio;
- resultados finais necessarios.

No Copernicus, os produtos SWOT brutos devem ficar em:

```text
~/mystorage/PPGGAG1889/atividade3_swot/dados/raw/
```

Os resultados devem ir para:

```text
~/mystorage/PPGGAG1889/atividade3_swot/outputs/
```

Nao grave resultados importantes fora de `mystorage`.
