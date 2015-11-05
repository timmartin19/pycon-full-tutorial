from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import ResourceBase, adapters, apimethod, translate, fields, Relationship

app = Flask('helloworld')


class HelloResource(ResourceBase):
    append_slash = True
    resource_name = 'hello'
    _relationships = (
        Relationship('related', relation='RelatedResource', property_map=dict(name='name')),
    )

    @translate(fields=[fields.StringField('name', minimum=3, required=True)], validate=True)
    @apimethod(methods=['GET'], no_pks=True)
    def hello_world(cls, request):
        return cls(properties=dict(content='Hello World!', name=request.get('name')))


class RelatedResource(ResourceBase):
    append_slash = True
    resource_name = 'related'
    pks = ('name',)

    @translate(fields=[fields.StringField('name', minimum=3, required=True)], validate=True)
    @apimethod(methods=['GET'])
    def hello_name(cls, request):
        name = request.get('name')
        content = 'Your name is {}'.format(name)
        return cls(properties=dict(content=content, name=name))


dispatcher = FlaskDispatcher(app)
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)
dispatcher.register_resources(HelloResource, RelatedResource)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
