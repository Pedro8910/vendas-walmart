# Análise de Vendas do Walmart

Limpeza e análise exploratória de dados semanais de vendas de lojas Walmart, relacionando vendas com feriados, inflação (CPI), desemprego, temperatura e preço do combustível. O projeto combina **análise estatística em Python** com um **dashboard interativo em Power BI** para exploração visual dos dados.

## Fonte dos dados

Dataset **Walmart Sales** (Kaggle), com vendas semanais (`Weekly_Sales`) por loja (`Store`), incluindo indicador de semana de feriado (`Holiday_Flag`), temperatura, preço do combustível, CPI e taxa de desemprego.

## O que o script faz

1. Carrega `Walmart_Sales.csv` e inspeciona tipos de dados e valores ausentes.
2. **Limpeza**:
   - Converte `Date` para datetime e depois padroniza no formato `MM-DD-AAAA`.
   - Arredonda `Weekly_Sales` (2 casas), `Temperature` (inteiro), `Fuel_Price` (2 casas), `CPI` (3 casas) e `Unemployment` (3 casas).
   - Ordena os dados por `Store` e `Date`.
   - Exporta o resultado limpo para `Walmart_Sales_clean.csv`.
3. **Análises**:
   - Vendas médias em semanas de feriado, agrupadas por mês.
   - Desemprego médio por loja, ordenado do menor para o maior.
   - Correlação entre CPI e vendas — geral, e separada entre semanas com e sem feriado.
   - Matriz de correlação entre vendas, temperatura, preço do combustível, CPI e desemprego.

## Como executar

```bash
pip install -r requirements.txt
python analise_vendas_walmart.py
```

## Estrutura do repositório

```
├── analise_vendas_walmart.py     # script principal da análise
├── Walmart_Sales.csv             # dataset original
├── Walmart_Sales_clean.csv       # dataset após limpeza (gerado pelo script)
├── Relatorio_Walmart_Sales.docx  # relatório formatado com os resultados
├── requirements.txt
└── README.md
```

## Relatório

O arquivo `Relatorio_Walmart_Sales.docx` traz a interpretação dos resultados, incluindo o efeito dos feriados nas vendas e a relação entre indicadores econômicos e o desempenho de vendas.

## Dashboard (Power BI)

Além da análise em Python, o projeto inclui um dashboard interativo em Power BI com 4 páginas:

| Página | Conteúdo |
|---|---|
| **Visão Geral** | Cards de KPI (vendas totais, média semanal, impacto de feriado), evolução das vendas no tempo, filtro por loja |
| **Feriado vs Normal** | Comparação de vendas médias entre semanas de feriado e normais, e volume total por loja |
| **Desemprego x Vendas** | Dispersão da relação entre taxa de desemprego e vendas médias por loja |
| **CPI e Combustível x Vendas** | Dispersão da relação entre inflação (CPI), preço do combustível e vendas médias por loja |

**Principais insights do dashboard:**
- Semanas de feriado vendem, em média, **+7,84%** a mais que semanas normais.
- O impacto do feriado não é uniforme entre lojas — algumas têm um salto bem mais expressivo que outras.
- A relação entre desemprego/CPI/combustível e vendas é fraca a moderada, sem um padrão linear forte — reforçando que o porte da loja pesa mais no volume de vendas do que esses indicadores macroeconômicos isolados.

### Como visualizar
O arquivo `.pbix` requer o [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (gratuito) para ser aberto e explorado interativamente. Prints de cada página estão disponíveis na pasta `dashboard/` para quem quiser visualizar sem instalar o programa.

```
├── dashboard/
│   ├── Dashboard_Vendas_Walmart.pbix   # arquivo do Power BI
│   └── imagens/                        # prints de cada página do dashboard
```
