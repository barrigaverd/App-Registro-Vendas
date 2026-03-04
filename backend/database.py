# Configuração da conexão com o banco de dados SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Defina uma variável com a URL do banco de dados (será um arquivo sqlite local chamado 'vendas.db')
DATABASE_URL = "sqlite:///vendas.db"

# Crie o motor (engine) do banco de dados usando a URL definida acima
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crie uma classe de sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crie uma classe base para nossos modelos de banco de dados
Base = declarative_base()
