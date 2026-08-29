# Guias de Métricas de Avaliação para Modelos de Regressão

Este documento contém a explicação detalhada das 4 principais métricas utilizadas para avaliar o desempenho de modelos de Regressão em Machine Learning, com foco prático em previsões contínuas (como ganho de força, valores financeiros, pesos, etc.).

---

## 1. $R^2$ (Coeficiente de Determinação)

O **$R^2$** mede a porcentagem da variância dos dados que é explicada pelo modelo. Em termos simples, indica o quão bem a linha de regressão se ajusta aos dados reais em comparação com uma linha reta baseada apenas na média de $y$.

* **Mede:** A qualidade e capacidade de explicação global do modelo.
* **Escala:** Varia de $0$ a $1$ (ou $0\%$ a $100\%$). Pode assumir valores negativos se o modelo performar pior do que a média simples.
* **Unidade:** Adimensional (sem unidade).
* **Interpretação:** 
  * $R^2 = 1.0$: Ajuste perfeito ($100\%$ dos dados explicados).
  * $R^2 = 0.85$: O modelo explica $85\%$ da variação dos dados.
  * $R^2 = 0.0$: O modelo não aprendeu nenhuma tendência e apenas chuta a média.
* **Vantagem:** É uma métrica relativa, facilitando a comparação entre datasets com escalas totalmente diferentes.
* **Desvantagem:** Não fornece o tamanho real do erro na unidade de medida do problema (ex: não indica o erro exato em quilos ou reais).

---

## 2. MAE (Mean Absolute Error / Erro Absoluto Médio)

O **MAE** calcula a média das distâncias absolutas entre os valores reais ($y$) e as previsões ($\hat{y}$). É a média direta e simples dos erros.

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

* **Mede:** O tamanho médio do erro de previsão.
* **Unidade:** A mesma unidade da variável alvo ($y$), como $\text{kg}$, $\text{R\$}$, metros, etc.
* **Interpretação:** Se $\text{MAE} = 2.0\text{ kg}$, significa que, em média, as previsões do modelo erram por $2\text{ kg}$ para mais ou para menos.
* **Vantagem:** Intuitivo e fácil de explicar para públicos não técnicos. Trata todos os erros proporcionalmente com o mesmo peso.
* **Desvantagem:** Por ser linear, não destaca nem penaliza com maior severidade erros pontuais muito graves (outliers).

---

## 3. MSE (Mean Squared Error / Erro Quadrático Médio)

O **MSE** eleva ao quadrado a diferença entre o valor real e a previsão para cada ponto e, em seguida, tira a média desses valores.

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

* **Mede:** A magnitude do erro com foco na penalização de grandes desvios.
* **Unidade:** Elevada ao quadrado ($\text{kg}^2$, $\text{R\$}^2$, etc.).
* **Interpretação:** Como eleva os desvios ao quadrado, ele atribui um peso muito maior a erros grandes:
  * Erro de $2 \rightarrow 2^2 = 4$
  * Erro de $10 \rightarrow 10^2 = 100$ (um erro $5$ vezes maior gera uma penalidade $25$ vezes superior).
* **Vantagem:** Útil matematicamente para algoritmos de otimização e para casos em que erros grandes são inaceitáveis.
* **Desvantagem:** A escala elevada ao quadrado dificulta a interpretação direta no mundo real.

---

## 4. RMSE (Root Mean Squared Error / Raiz do Erro Quadrático Médio)

O **RMSE** é a raiz quadrada do MSE. Ele mantém a propriedade de penalizar severamente erros grandes, mas converte o resultado final de volta para a unidade de medida original.

$$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

* **Mede:** O erro médio do modelo, dando peso desproporcional a falhas grandes.
* **Unidade:** A mesma unidade da variável alvo ($y$), como $\text{kg}$, $\text{R\$}$, etc.
* **Interpretação:** Se o $\text{RMSE} = 3.5\text{ kg}$, a margem de erro média está ajustada nessa faixa, ponderando os casos em que o modelo errou por margens maiores.
* **Vantagem:** Combina a interpretabilidade da mesma unidade do MAE com a sensibilidade a grandes erros do MSE.
* **Desvantagem:** É mais vulnerável a ruídos e pontos fora do padrão (outliers) no dataset do que o MAE.

---

## Tabela Comparativa Resumida

| Métrica | Unidade de Medida | Sensibilidade a Outliers | Foco Principal |
| :--- | :--- | :--- | :--- |
| **$R^2$** | Sem unidade ($0$ a $1$) | Moderada | Qualidade e explicação geral do ajuste |
| **MAE** | Unidade original ($y$) | Baixa | Erro médio em escala real direta |
| **MSE** | Unidade ao quadrado ($y^2$) | Muito Alta | Punição matemática a grandes desvios |
| **RMSE** | Unidade original ($y$) | Alta | Erro real penalizando grandes falhas |

---

## Recomendações Práticas

* Utilize o **RMSE** como métrica principal de treinamento/otimização em problemas nos quais errar por uma grande margem é perigoso (como carga máxima ou dosagem).
* Utilize o **MAE** se o dataset contiver muitos outliers ou se o impacto de errar pouco ou muito for estritamente proporcional.
* Apresente sempre o **$R^2$** em conjunto com a métrica de erro (MAE ou RMSE) para dar contexto sobre o percentual de acerto global do modelo.
