from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import restmixins, adapters, ListRelationship, Relationship
from ripozo_sqlalchemy import create_resource, ScopedSessionHandler

from common.models import Post, Comment, engine


app = Flask('easyapp')

# Create a session handler to manage SQLAlchemy sessions
session_handler = ScopedSessionHandler(engine)

# Create your resources.  There are plenty of other options
PostResource = create_resource(
    Post, session_handler, resource_bases=(restmixins.CRUDL,),
    relationships=(ListRelationship('comments', relation='CommentResource'),)
)
CommentResource = create_resource(
    Comment, session_handler, resource_bases=(restmixins.CRUDL,),
    relationships=(Relationship('post', property_map=dict(post_id='id'), relation='PostResource'),)
)

# Initialize the dispatcher
dispatcher = FlaskDispatcher(app)
dispatcher.register_resources(PostResource, CommentResource)
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
