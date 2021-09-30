# How Much App - Estimando Valores para Planos de Saúde Individuais
Projeto em Ciência de Dados do <a href="https://blog.dsacademy.com.br/programa-de-mentoria-entre-os-alunos-dsa-temporada-2021/">programa de mentoria entre alunos DSA<a/><br/><br/>
Mentor: Marcelo Wecchi<br/>
Mentorados: Rye Santana Takeda, Guilherme Coelho Neves, Eder José de Carvalho

## Links úteis para entender o projeto
- <a href="https://www.youtube.com/watch?v=RAeLRPZaTFk">Sobre o programa de mentoria</a>
- <a href="https://www.youtube.com/watch?v=_u4wxHR1qVA">Sobre o projeto em Ciência de Dados</a>
- <a href="https://mentoriaapp.herokuapp.com/">Link para a aplicação hospedada no Heroku</a>
- <a href="https://github.com/wecchi/mentoria_dsa_2021/">Arquivos dos trabalhos realizados</a>

## Como executar

- Passo 1: Certifique-se de ter o <a href="https://www.python.org/">Python</a> instalado na sua máquina (versão usada nesse projeto <a href="https://www.python.org/downloads/release/python-397/">Python 3.9.7</a>)
- - Opcional: Crie um ambiente virtual <a href="https://docs.python.org/pt-br/3/library/venv.html">venv</a>
- Passo 2: Instale os requerimentos: `pip install -r requirements.txt`
- Passo 3: Rode a aplicação: `flask run`

## Detalhes sobre a aplicação

A aplicação faz uso de arquivos gerados durante o desenvolvimento do projeto de ciência de dados

- **encoders/**
- - ***faixa_etaria_labels.bin***: rótulos para os códigos das faixa etárias
- - ***new_dataset_dummy_first_true_encoders.bin***: colunas resultantes da utilização de variáveis *Dummy*
- - ***options***: conjunto de características dos planos
- - ***sample***: registro exemplo do conjunto de dados
- **models/**
- - ***mlpregressor_v1.pickle***: modelo treinado usando <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html">MLPRegressor</a>
- **Procfile**: arquivo usado para *deploy* da aplicação no <a href="https://www.heroku.com/what">Heroku</a>
