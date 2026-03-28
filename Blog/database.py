from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
# sqlite_file_name = "blog.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
mysql_url = "mysql+pymysql://root:Querry4437%40@localhost:3306/blogdb"

# connect_args = {"check_same_thread": False}
engine = create_engine(mysql_url)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)



Base = declarative_base()