# FarmTech Solutions - Análise e Previsão de Rendimento de Safra
**Equipe:Arthur Peixoto 566697 ** 

Neste notebook, realizamos a análise exploratória, clusterização para descoberta de tendências/outliers e a construção de 5 modelos de Machine Learning (Regressão) para prever o rendimento das safras com base em dados climáticos.

    import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Pré-processamento e Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

# Modelos de Regressão
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

# Métricas
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('crop_yield.csv')

display(df.head())
display(df.info())
display(df.describe())

plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Cultura', y='Rendimento', data=df)
plt.title("Distribuição do Rendimento por Cultura")
plt.show()

X_cluster = df.select_dtypes(include=[np.number])
scaler_cluster = StandardScaler()
X_cluster_scaled = scaler_cluster.fit_transform(X_cluster)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_cluster_scaled)

iso = IsolationForest(contamination=0.05, random_state=42)
df['Outlier'] = iso.fit_predict(X_cluster_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperatura a 2 metros (ºC)', y='Rendimento', hue='Cluster', style='Outlier', palette='viridis', data=df)
plt.title("Clusters de Safra e Outliers (Temperatura vs Rendimento)")
plt.show()

print(f"Total de Outliers detectados: {len(df[df['Outlier'] == -1])}")

X = df.drop(columns=['Rendimento', 'Cluster', 'Outlier'])
y = df['Rendimento']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = ['Cultura']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

modelos = {
    "Regressão Linear": LinearRegression(),
    "Árvore de Decisão": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    "SVR (Support Vector Regressor)": SVR()
}

resultados = []

for nome, modelo in modelos.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', modelo)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    resultados.append({'Modelo': nome, 'MAE': mae, 'RMSE': rmse, 'R2 Score': r2})

df_resultados = pd.DataFrame(resultados).sort_values(by='R2 Score', ascending=False)
display(df_resultados)

   