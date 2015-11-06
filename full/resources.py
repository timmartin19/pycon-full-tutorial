from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ripozo import restmixins, apimethod, translate, ListRelationship, Relationship
from ripozo.resources.fields.common import IntegerField

from full.managers import CommentManager, PostManager, session_handler


class PostResource(restmixins.CRUDL):
    append_slash = True
    pks = ('id',)
    manager = PostManager(session_handler)
    resource_name = 'post'
    _relationships = (
        ListRelationship('comments', relation='CommentResource'),
    )

    @translate(fields=[IntegerField('id', required=True)], validate=True)
    @apimethod(route='/create_comment/', methods=['POST'])
    def create_comment(cls, request):
        args = request.body_args
        args['post_id'] = request.get('id')
        request.body_args = args
        CommentResource.create(request)
        return cls.retrieve(request)


class CommentResource(restmixins.CRUDL):
    append_slash = True
    pks = ('id',)
    manager = CommentManager(session_handler)
    resource_name = 'comment'
    _relationships = (
        Relationship('post', property_map=dict(post_id='id'), relation='PostResource'),
    )
