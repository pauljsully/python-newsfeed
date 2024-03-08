from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User')
    comments = relationship('Comment', cascade='all, delete') # if post is deleted, all associated comments will be too
    votes = relationship('Vote', cascade='all, delete')

    vote_count = column_property(
        # eg: SELECT COUNT(votes.id) AS vote_count FROM votes WHERE votes.post_id = 1;
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )