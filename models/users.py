from sqlalchemy.orm import Mapped, mapped_column


from base.orm import Base


class User(Base): 
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
