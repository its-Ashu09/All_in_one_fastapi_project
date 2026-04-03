from fastapi import FastAPI
from Blog import models
from .database import engine
from Blog.routers import blog, user, authentication

app = FastAPI()


#models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



@app.get('/',tags=["Home"])
def Home():
    return {'message':'lets build'}










