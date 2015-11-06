from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from common import settings


engine = create_engine(settings.SQLALCHEMY_URI, echo=True)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=50), nullable=True)
    post_text = Column(Text, nullable=False)
    comments = relationship('Comment', backref='post')


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=50), nullable=True)
    comment_text = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


Base.metadata.create_all(engine)
