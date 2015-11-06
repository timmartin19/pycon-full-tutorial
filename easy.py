from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import restmixins, apimethod, translate, ListRelationship, Relationship, adapters
from ripozo.resources.fields.common import IntegerField
from ripozo_sqlalchemy import create_resource, ScopedSessionHandler

from common.models import Post, Comment, engine


app = Flask('easyapp')

session_handler = ScopedSessionHandler(engine)


class CreateCommentMixin(object):
    @translate(fields=[IntegerField('id', required=True)], validate=True)
    @apimethod(route='/create_comment/', methods=['POST'])
    def create_comment(cls, request):
        args = request.body_args
        args['post_id'] = request.get('id')
        request.body_args = args
        CommentResource.create(request)
        return cls.retrieve(request)


PostResource = create_resource(
    Post, session_handler, resource_bases=(restmixins.CRUDL, CreateCommentMixin,),
    relationships=(ListRelationship('comments', relation='Comment'),)
)
CommentResource = create_resource(
    Comment, session_handler, resource_bases=(restmixins.CRUDL,),
    relationships=(Relationship('post', property_map=dict(post_id='id'), relation='Post'),)
)


dispatcher = FlaskDispatcher(app, url_prefix='/api')
dispatcher.register_resources(PostResource, CommentResource)
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
