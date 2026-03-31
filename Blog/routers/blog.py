from fastapi import APIRouter, Depends,HTTPException,status
from Blog import schemas,models, oauth2
from Blog.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix= "/blog",
    tags=["Blogs"]
)

@router.get('/',response_model=list[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs



@router.post('/',status_code=status.HTTP_201_CREATED)
def create (requests:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   new_blog = models.Blog(title=requests.title,body = requests.body,User_id=requests.User_id)
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)
   return new_blog


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def destroy(id,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
  blog = db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
  
  blog.delete(synchronize_session=False)
  db.commit()
  return {'detail':f'{id} id is deleted successfully'}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog,)
def show(id:int,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog  =  db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not avilable")
       
    return blog 