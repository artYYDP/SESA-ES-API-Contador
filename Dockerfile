# Usa imagem base enxuta com Python 3.13
FROM python:3.13-slim

# Cria diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo o restante do código para dentro do container
COPY . .

# Expõe a porta padrão usada pelo Flask (ajuste se mudar no app.py)
EXPOSE 5000

# Comando que inicia sua aplicação
CMD ["python", "app.py"]