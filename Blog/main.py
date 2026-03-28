from fastapi import FastAPI,Depends,status,Response,HTTPException
from Blog import schemas,models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def Home():
    return {'message':'lets build'}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create (requests:schemas.Blog, db:Session=Depends(get_db)):
   new_blog = models.Blog(title=requests.title,body = requests.body)
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)
   return new_blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
  
  blog.delete(synchronize_session=False)
  db.commit()
  return {'detail':f'{id} id is deleted successfully'}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

@app.get('/blog')
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200)
def show(id:int,response:Response,db:Session=Depends(get_db)):
    blog  =  db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not avilable")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with id {id} is not avilable"}
    return blog