# Usa uma imagem oficial do Python com Playwright já configurado
FROM mcr.microsoft.com/playwright/python:v1.41.0-focal

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala os navegadores necessários para o Playwright
RUN playwright install --with-deps

# Define o comando padrão ao rodar o container
CMD ["python", "main.py"]