from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# vai pegar tudo q tem no database e models e vai ciar um arquivo com tudo ja montado
models.Base.metadata.create_all(bind=engine)
