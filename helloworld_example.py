from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import ResourceBase, adapters, apimethod, translate, fields

app = Flask('helloworld')


class HelloResource(ResourceBase):
    resource_name = 'hello'
    pks = ('name',)

    @apimethod(methods=['GET'], no_pks=True)
    def hello_world(cls, request):
        return cls(properties=dict(content='Hello World!'))

    @translate(fields=[fields.StringField('name', minimum=3, required=True)], validate=True)
    @apimethod(methods=['GET'])
    def hello_name(cls, request):
        content = 'Hello {}'.format(request.get('name'))
        return cls(properties=dict(content=content))


dispatcher = FlaskDispatcher(app)
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)
dispatcher.register_resources(HelloResource)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()



