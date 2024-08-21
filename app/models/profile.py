from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from models.db.db_setup import Base


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    full_name: Mapped[str] = mapped_column(String, index=True)
    bio: Mapped[str] = mapped_column(String, index=True)
    photo_url: Mapped[str] = mapped_column(String)
    skills: Mapped[str] = mapped_column(String)
    experience: Mapped[str] = mapped_column(String)
    project_links: Mapped[str] = mapped_column(String)

    owner: Mapped["User"] = relationship("User", back_populates="profile")

    @classmethod
    def get_profile(cls, session: Session, user_id):

        return session.query(cls).filter(cls.user_id == user_id).first() or None