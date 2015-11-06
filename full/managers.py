from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from ripozo.resources.fields.common import StringField
from ripozo_sqlalchemy import AlchemyManager, ScopedSessionHandler

from common.models import engine, Post, Comment

session_handler = ScopedSessionHandler(engine)


class PostManager(AlchemyManager):
    model = Post
    fields = ('id', 'username', 'post_text', 'comments.id',)
    create_fields = ('username', 'post_text',)
    _field_validators = {
        'username': StringField('username', minimum=3, regex=re.compile(r'^[a-zA-Z0-9]+$'))
    }


class CommentManager(AlchemyManager):
    model = Comment
    fields = ('id', 'username', 'comment_text', 'post_id',)
    create_fields = ('username', 'post_id', 'comment_text',)
    update_fields = ('username', 'comment',)
