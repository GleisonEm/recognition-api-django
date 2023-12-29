# Use a imagem oficial do Python 3.9 como base
FROM python:3.12-slim-buster

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instale as dependências do sistema necessárias para o Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências Python usando pip
RUN pip install -r requirements.txt

# Copie o código fonte para o diretório de trabalho
COPY . .
