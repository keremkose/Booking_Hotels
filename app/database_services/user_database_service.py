from app.schemas.user_schema import UserSchema
from app.models.models import UserModel
from sqlalchemy.orm.session import Session
from app.database_services.hash import Hash



def create_user(user_schema:UserSchema,db:Session):
    db_user=UserModel(
        name=user_schema.name,
        surname=user_schema.surname,
        username=user_schema.username,
        email=user_schema.email,
        password= Hash.bcrypt(user_schema.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return 1