from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import adapters

from full.resources import PostResource, CommentResource

app = Flask('fullexample')

dispatcher = FlaskDispatcher(app, url_prefix='/api')
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)
dispatcher.register_resources(PostResource, CommentResource)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
