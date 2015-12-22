import asyncio
from apiox.core.db import API

__version__ = '0.1'

api_id = 'hello-world'
url_prefix = '/{}/'.format(api_id)


@asyncio.coroutine
def setup(app):
    from . import handlers

    app.router.add_route('*', url_prefix,
                         handlers.IndexHandler(),
                         name='hello-world:index')


def declare_api(session):
    session.merge(API.from_json({
        'id': api_id,
        'title': 'Hello World',
        'version': __version__,
        'scopes': [{
            'id': '/hello-world',
            'title': 'Hello World!',
            'description': 'Provides access to POST to the "Hello World!" API',
            'grantToUser': True,
            'requestableByAllClients': True,
        }],
    }))
