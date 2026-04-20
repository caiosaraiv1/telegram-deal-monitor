# 1. Imagem base oficial do Python (versão slim = mais leve)
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências primeiro (boa prática para cache do Docker)
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do código para dentro do container
COPY . .

# 6. Comando que será executado quando o container iniciar
CMD ["python", "-u", "main.py"]
