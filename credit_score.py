{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Passo a Passo \n",
    "\n",
    "#### 0.Entender o desafio da empresa\n",
    "#### 1.Importar a base de dados\n",
    "#### 2.Preparar a base de dados para a IA\n",
    "#### 3.Criar um modelo de IA\n",
    "#### 4.Escolher o melhor modelo\n",
    "#### 5.Usar o modelo em um cenário real "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 100000 entries, 0 to 99999\n",
      "Data columns (total 25 columns):\n",
      " #   Column                    Non-Null Count   Dtype  \n",
      "---  ------                    --------------   -----  \n",
      " 0   id_cliente                100000 non-null  int64  \n",
      " 1   mes                       100000 non-null  int64  \n",
      " 2   idade                     100000 non-null  float64\n",
      " 3   profissao                 100000 non-null  object \n",
      " 4   salario_anual             100000 non-null  float64\n",
      " 5   num_contas                100000 non-null  float64\n",
      " 6   num_cartoes               100000 non-null  float64\n",
      " 7   juros_emprestimo          100000 non-null  float64\n",
      " 8   num_emprestimos           100000 non-null  float64\n",
      " 9   dias_atraso               100000 non-null  float64\n",
      " 10  num_pagamentos_atrasados  100000 non-null  float64\n",
      " 11  num_verificacoes_credito  100000 non-null  float64\n",
      " 12  mix_credito               100000 non-null  object \n",
      " 13  divida_total              100000 non-null  float64\n",
      " 14  taxa_uso_credito          100000 non-null  float64\n",
      " 15  idade_historico_credito   100000 non-null  float64\n",
      " 16  investimento_mensal       100000 non-null  float64\n",
      " 17  comportamento_pagamento   100000 non-null  object \n",
      " 18  saldo_final_mes           100000 non-null  float64\n",
      " 19  score_credito             100000 non-null  object \n",
      " 20  emprestimo_carro          100000 non-null  int64  \n",
      " 21  emprestimo_casa           100000 non-null  int64  \n",
      " 22  emprestimo_pessoal        100000 non-null  int64  \n",
      " 23  emprestimo_credito        100000 non-null  int64  \n",
      " 24  emprestimo_estudantil     100000 non-null  int64  \n",
      "dtypes: float64(14), int64(7), object(4)\n",
      "memory usage: 19.1+ MB\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "None"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#IMPORTAR BASE DE DADOS \n",
    "import pandas as pd\n",
    "\n",
    "tabela = pd.read_csv('clientes.csv')\n",
    "display(tabela.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 100000 entries, 0 to 99999\n",
      "Data columns (total 25 columns):\n",
      " #   Column                    Non-Null Count   Dtype  \n",
      "---  ------                    --------------   -----  \n",
      " 0   id_cliente                100000 non-null  int64  \n",
      " 1   mes                       100000 non-null  int64  \n",
      " 2   idade                     100000 non-null  float64\n",
      " 3   profissao                 100000 non-null  int32  \n",
      " 4   salario_anual             100000 non-null  float64\n",
      " 5   num_contas                100000 non-null  float64\n",
      " 6   num_cartoes               100000 non-null  float64\n",
      " 7   juros_emprestimo          100000 non-null  float64\n",
      " 8   num_emprestimos           100000 non-null  float64\n",
      " 9   dias_atraso               100000 non-null  float64\n",
      " 10  num_pagamentos_atrasados  100000 non-null  float64\n",
      " 11  num_verificacoes_credito  100000 non-null  float64\n",
      " 12  mix_credito               100000 non-null  int32  \n",
      " 13  divida_total              100000 non-null  float64\n",
      " 14  taxa_uso_credito          100000 non-null  float64\n",
      " 15  idade_historico_credito   100000 non-null  float64\n",
      " 16  investimento_mensal       100000 non-null  float64\n",
      " 17  comportamento_pagamento   100000 non-null  int32  \n",
      " 18  saldo_final_mes           100000 non-null  float64\n",
      " 19  score_credito             100000 non-null  int32  \n",
      " 20  emprestimo_carro          100000 non-null  int64  \n",
      " 21  emprestimo_casa           100000 non-null  int64  \n",
      " 22  emprestimo_pessoal        100000 non-null  int64  \n",
      " 23  emprestimo_credito        100000 non-null  int64  \n",
      " 24  emprestimo_estudantil     100000 non-null  int64  \n",
      "dtypes: float64(14), int32(4), int64(7)\n",
      "memory usage: 17.5 MB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#Passo 2: Preparar a base de dados para a IA\n",
    "# 2.1 Transformar as colunas de texto em numero (colunas: Profissao,Mix credito, comportamento Pagamento e score credito) - usar labelencoder, esta dentro do sklearn\n",
    "\n",
    "import sklearn\n",
    "from sklearn.preprocessing import LabelEncoder \n",
    "codificador = LabelEncoder()\n",
    "tabela[\"profissao\"] = codificador.fit_transform(tabela[\"profissao\"])\n",
    "tabela[\"mix_credito\"] = codificador.fit_transform(tabela[\"mix_credito\"])\n",
    "tabela[\"comportamento_pagamento\"] = codificador.fit_transform(tabela[\"comportamento_pagamento\"])\n",
    "tabela[\"score_credito\"] = codificador.fit_transform(tabela[\"score_credito\"])\n",
    "print(tabela.info())\n",
    "\n",
    "# 2.2 Separar info em treino e teste, y é o que eu quero prever e x são as colunas que eu vou usar para prever\n",
    "y = tabela[\"score_credito\"]\n",
    "x = tabela.drop([\"score_credito\", \"id_cliente\"], axis=1)\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x_treino,x_teste,y_treino,y_teste = train_test_split(x,y, test_size=0.3, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Passo 3: Criar um modelo de IA - score ruim medio bom\n",
    "# 3.1 arvore de decisao e KNN, importar modelo de IA\n",
    "from sklearn.ensemble import RandomForestClassifier \n",
    "from sklearn.neighbors import KNeighborsClassifier \n",
    "#Criar modelo de IA\n",
    "modelo_arvoredecisao = RandomForestClassifier()\n",
    "modelo_knn = KNeighborsClassifier()\n",
    "\n",
    "#treinar modelo (fit e pra treinar)\n",
    "modelo_arvoredecisao.fit(x_treino, y_treino)\n",
    "modelo_knn.fit(x_treino, y_treino)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8263\n",
      "0.7324\n"
     ]
    }
   ],
   "source": [
    "#Passo 4: Escolher o melhor modelo (acuracia do modelo)\n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)\n",
    "previsao_knn = modelo_knn.predict(x_teste.to_numpy())\n",
    "\n",
    "print(accuracy_score(y_teste, previsao_arvoredecisao))\n",
    "print(accuracy_score(y_teste, previsao_knn))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# o melhor modelo é o modelo_arvoredecisao = 83% acuracia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mes</th>\n",
       "      <th>idade</th>\n",
       "      <th>profissao</th>\n",
       "      <th>salario_anual</th>\n",
       "      <th>num_contas</th>\n",
       "      <th>num_cartoes</th>\n",
       "      <th>juros_emprestimo</th>\n",
       "      <th>num_emprestimos</th>\n",
       "      <th>dias_atraso</th>\n",
       "      <th>num_pagamentos_atrasados</th>\n",
       "      <th>...</th>\n",
       "      <th>taxa_uso_credito</th>\n",
       "      <th>idade_historico_credito</th>\n",
       "      <th>investimento_mensal</th>\n",
       "      <th>comportamento_pagamento</th>\n",
       "      <th>saldo_final_mes</th>\n",
       "      <th>emprestimo_carro</th>\n",
       "      <th>emprestimo_casa</th>\n",
       "      <th>emprestimo_pessoal</th>\n",
       "      <th>emprestimo_credito</th>\n",
       "      <th>emprestimo_estudantil</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>31.0</td>\n",
       "      <td>1</td>\n",
       "      <td>19300.340</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>17.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>52.0</td>\n",
       "      <td>19.0</td>\n",
       "      <td>...</td>\n",
       "      <td>29.934186</td>\n",
       "      <td>218.0</td>\n",
       "      <td>44.50951</td>\n",
       "      <td>1</td>\n",
       "      <td>312.487689</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>12600.445</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>18.0</td>\n",
       "      <td>...</td>\n",
       "      <td>28.819407</td>\n",
       "      <td>12.0</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>2</td>\n",
       "      <td>300.994163</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>48.0</td>\n",
       "      <td>1</td>\n",
       "      <td>20787.690</td>\n",
       "      <td>8.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>24.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>...</td>\n",
       "      <td>34.235853</td>\n",
       "      <td>215.0</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0</td>\n",
       "      <td>345.081577</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   mes  idade  profissao  salario_anual  num_contas  num_cartoes  \\\n",
       "0    1   31.0          1      19300.340         6.0          7.0   \n",
       "1    4   32.0          0      12600.445         5.0          5.0   \n",
       "2    2   48.0          1      20787.690         8.0          6.0   \n",
       "\n",
       "   juros_emprestimo  num_emprestimos  dias_atraso  num_pagamentos_atrasados  \\\n",
       "0              17.0              5.0         52.0                      19.0   \n",
       "1              10.0              3.0         25.0                      18.0   \n",
       "2              14.0              7.0         24.0                      14.0   \n",
       "\n",
       "   ...  taxa_uso_credito  idade_historico_credito  investimento_mensal  \\\n",
       "0  ...         29.934186                    218.0             44.50951   \n",
       "1  ...         28.819407                     12.0              0.00000   \n",
       "2  ...         34.235853                    215.0              0.00000   \n",
       "\n",
       "   comportamento_pagamento  saldo_final_mes  emprestimo_carro  \\\n",
       "0                        1       312.487689                 1   \n",
       "1                        2       300.994163                 0   \n",
       "2                        0       345.081577                 0   \n",
       "\n",
       "   emprestimo_casa  emprestimo_pessoal  emprestimo_credito  \\\n",
       "0                1                   0                   0   \n",
       "1                0                   0                   0   \n",
       "2                1                   0                   1   \n",
       "\n",
       "   emprestimo_estudantil  \n",
       "0                      0  \n",
       "1                      1  \n",
       "2                      0  \n",
       "\n",
       "[3 rows x 23 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O Score de crédito do cliente 1 é Ruim\n",
      "O Score de crédito do cliente 3 é Bom\n",
      "O Score de crédito do cliente 2 é Ok\n"
     ]
    }
   ],
   "source": [
    "#Qual é o processo de previsao?\n",
    "\n",
    "novos_clientes = pd.read_csv(\"novos_clientes.csv\")\n",
    "novos_clientes[\"profissao\"] = codificador.fit_transform(novos_clientes[\"profissao\"])\n",
    "novos_clientes[\"mix_credito\"] = codificador.fit_transform(novos_clientes[\"mix_credito\"])\n",
    "novos_clientes[\"comportamento_pagamento\"] = codificador.fit_transform(novos_clientes[\"comportamento_pagamento\"])\n",
    "display(novos_clientes)\n",
    "\n",
    "previsao = modelo_arvoredecisao.predict(novos_clientes)\n",
    "\n",
    "for item in previsao:\n",
    "    if item == 0:\n",
    "        print(f'O Score de crédito do cliente 3 é Bom')\n",
    "    elif item == 1:\n",
    "        print(f'O Score de crédito do cliente 1 é Ruim')\n",
    "    else:\n",
    "        print(f'O Score de crédito do cliente 2 é Ok')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
