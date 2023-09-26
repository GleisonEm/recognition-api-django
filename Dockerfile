# Use a imagem oficial do Python 3.9 como base
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências Python usando pip
RUN pip install -r requirements.txt

# Copie o código fonte para o diretório de trabalho
COPY . .