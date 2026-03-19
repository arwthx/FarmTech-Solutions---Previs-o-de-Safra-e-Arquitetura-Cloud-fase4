# 🌾 FarmTech Solutions - Previsão de Safra e Arquitetura Cloud

Bem-vindo ao repositório do projeto FarmTech Solutions! Este projeto foi desenvolvido para a Fase 5 (PBL) e está dividido em duas frentes principais: Ciência de Dados (Machine Learning) e Infraestrutura em Nuvem (AWS).

**Integrantes da Equipe:**
- Arthur Peixoto Souza - RM566697
- 

---

## 🤖 Entrega 1: Machine Learning (Previsão de Rendimento)

Nosso objetivo foi analisar uma base de dados de uma fazenda de 200 hectares e prever o rendimento das safras com base em dados climáticos (precipitação, umidade, temperatura).

### 📂 Estrutura da Solução
A análise completa, limpeza de dados e modelagem está contida no arquivo Jupyter Notebook:
👉 **https://jupyter.org/try-jupyter/edit/?path=ArthurPeixoto_rm566697_pbl_fase5.ipynb.py**

No notebook você encontrará:
1. **Análise Exploratória (EDA):** Entendimento das distribuições climáticas.
2. **Clusterização e Outliers:** Uso de `K-Means` e `Isolation Forest` para encontrar tendências de produtividade e isolar anomalias climáticas.
3. **Modelagem Supervisionada:** Treinamento e comparação de 5 algoritmos (Regressão Linear, Árvore de Decisão, Random Forest, Gradient Boosting e SVR).
4. **Conclusões:** Avaliação baseada nas métricas de R² Score, RMSE e MAE.

🎥 **Vídeo de Demonstração (Entrega 1):** https://www.youtube.com/watch?v=_Z_oZ6bTehw

---

## ☁️ Entrega 2: Computação em Nuvem (AWS)

Para hospedar a API que receberá os dados dos sensores e rodará nosso modelo de Machine Learning, dimensionamos uma máquina na nuvem da AWS com as seguintes especificações:
- **Compute:** 2 vCPUs e 1 GiB de memória (Instância `t3.micro` Linux)
- **Rede:** Até 5 Gigabit
- **Storage:** 50 GB de armazenamento (EBS gp3)
- **Modelo:** On-Demand

### 📊 Comparativo de Custos (Calculadora AWS)
*(Adicione aqui um print / captura de tela da calculadora da AWS)*

Realizamos o comparativo entre duas regiões:
- **N. Virginia (EUA):** ~ US$ 11,60 / mês *(Solução financeiramente mais barata)*
- **São Paulo (BR):** ~ US$ 18,20 / mês

### ⚖️ Tomada de Decisão (Cenário Real)
Apesar da região da Virgínia do Norte ser mais barata financeiramente, em um cenário onde é exigido **acesso rápido** aos sensores e existem **restrições legais para armazenamento no exterior**, a escolha obrigatória é a região de **São Paulo (sa-east-1)**. 

**Justificativa:** A hospedagem em São Paulo garante baixa latência (tempo de resposta rápido na comunicação entre os sensores na fazenda e a nuvem) e cumpre rigorosamente os requisitos de soberania de dados e leis de privacidade territoriais, mantendo os dados legais e protegidos em solo nacional.

🎥 **Vídeo de Demonstração (Entrega 2 - Calculadora):** https://www.youtube.com/watch?v=_Z_oZ6bTehw
