# Alerth Backend

Bem-vindo à configuração do backend do projeto Alerth. Este guia irá orientá-lo pelos passos necessários para configurar o ambiente de desenvolvimento.

⚠️ Este projeto está em fase inicial de desenvolvimento, por isso, é normal encontrar bugs ou funcionalidades incompletas. ⚠️

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu sistema:

- Git
- Python 3.8+
- Redis (necessário para WebSockets e Django Channels)
- Virtualenv (opcional, mas recomendável para isolamento do ambiente)

### 1. Clonar o Repositório

O primeiro passo é clonar o repositório do projeto para o seu ambiente local. Utilize o seguinte comando no terminal:

```
git clone https://github.com/JonathasSC/alerth-backend.git
```

Após a clonagem, navegue até o diretório do projeto:

```
cd alerth-backend
```

### 2. Criar e Ativar o Ambiente Virtual

A utilização de um ambiente virtual é recomendada para garantir que as dependências do projeto sejam instaladas de maneira isolada.

#### No Windows:

Crie o ambiente virtual:

```
python -m venv venv
```

Ative o ambiente virtual:

```
.\venv\Scripts\Activate
```

#### No Linux/MacOS:

Crie o ambiente virtual:

```
python3 -m venv venv
```

Ative o ambiente virtual:

```
python3 -m venv venv
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

```
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

O projeto depende de algumas variáveis de ambiente para funcionar corretamente. Crie um arquivo .env na raiz do projeto, baseado no arquivo .env.example fornecido, ou mantenha os valores padrão.

```
cp .env.example .env
```

### 5. Aplicar Migrações no Banco de Dados

O próximo passo é aplicar as migrações para criar as tabelas necessárias no banco de dados.

```
python manage.py migrate
```

### 6. Criar um Superusuário

Para acessar a área administrativa do Django, crie um superusuário executando o seguinte comando:

```
python manage.py createsuperuser
```

### 7. Rodar o Redis para WebSockets

Como usaremos Channels, nosso armazenamento para Websocket é o Redis. É necessário garantir que o Redis está rodando. Para iniciar o Redis localmente, execute o seguinte comando:

#### No Windows:

Baixe o Redis para Windows (se necessário) ou execute via Docker:

```
docker run --name redis -p 6379:6379 -d redis
```

#### No Linux/MacOS:

```
redis-server
```

### 8. Iniciar o Servidor de Desenvolvimento

```
python manage.py runserver
```

Agora que tudo está configurado, você pode iniciar o servidor de desenvolvimento:

```
python manage.py runserver
```

A aplicação estará rodando no endereço: http://localhost:8000/

### 9. Testar a API e WebSocket

#### Testar API:

Você pode testar os endpoints da API utilizando o Postman ou Insomnia. Acesse http://localhost:8000/api/ para verificar a documentação automática.

#### Testar WebSocket:

Verifique se o WebSocket está funcionando corretamente, conectando-se ao endpoint WebSocket em ws://localhost:8000/ws/ via navegador ou ferramentas de teste de WebSocket.
