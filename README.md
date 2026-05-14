# Data_Process_Pandas
# 🌿 Análise de Incêndios na Amazonas com Python (Pandas)

## 📊 Descrição do Projeto

Este projeto realiza uma análise exploratória de dados sobre incêndios florestais no estado do Amazonas, utilizando Python e a biblioteca Pandas.
O objetivo é explorar padrões temporais e geográficos, identificar tendências e responder a perguntas como:

* Qual o total de incêndios por estado?
* Qual o ano com mais ocorrências?
* Quais estados registaram mais incêndios em determinados meses?
* Qual a média geral de incêndios?

---

## 📁 Dataset

O dataset utilizado é o **Amazonas.csv**, que contém informações como:

* `year` → Ano da ocorrência
* `month` → Mês
* `state` → Estado brasileiro
* `number` → Número de incêndios

---

## 🛠️ Tecnologias Utilizadas

* Python 🐍
* Pandas 📊
* NumPy 🔢
* Matplotlib 📈 (opcional para visualização)
* Seaborn 🎨 (opcional para gráficos)

---

## 📌 Funcionalidades Implementadas

O script realiza:

### 🔹 Leitura de dados

* Importação do ficheiro CSV com Pandas

### 🔹 Análise exploratória

* Visualização das primeiras e últimas linhas (`head`, `tail`)
* Identificação do ano mínimo e máximo
* Cálculo da média de incêndios

### 🔹 Agrupamento de dados

* Total de incêndios por estado
* Total de incêndios por ano (ex: estado do Acre)

### 🔹 Filtragem de dados

* Uso de máscaras (`mask`) para filtrar meses e condições específicas
* Identificação de estados com mais incêndios em determinados períodos

### 🔹 Ordenação

* Estados ordenados por número total de incêndios
* Listagem alfabética de estados com ocorrência de incêndios

---

## 📈 Exemplo de Análise

```python
df.groupby('state')['number'].sum().sort_values(ascending=False)
```

---

## ▶️ Como Executar o Projeto

1. Instalar as dependências:

```bash
pip install pandas numpy matplotlib seaborn
```

2. Executar o script Python:

```bash
python Data_visualization.py
```

3. Garantir que o ficheiro `Amazonas.csv` está no caminho correto.

---

## ⚠️ Notas Importantes

* Em alguns sistemas, o separador do CSV pode ser `;` em vez de `,`
* Os meses podem estar em inglês (`Jan`, `Feb`, `Dec`) em vez de português
* Em Windows, use caminhos com `r'...'` ou `/` para evitar erros de `unicodeescape`

---

## 📌 Conclusão

Este projeto demonstra técnicas fundamentais de análise de dados com Pandas, incluindo leitura de dados, filtragem, agregação e exploração estatística.

---

## 👨‍💻 Autor

Projeto desenvolvido no âmbito de aprendizagem de Data Analysis com Python.
