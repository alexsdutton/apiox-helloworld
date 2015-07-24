from . import __version__, handlers

prefix = 'hello-world'
url_prefix = '/{}/'.format(prefix)


def hook_in(app):
    app['definitions'][prefix] = {'title': 'Hello World',
                                  'version': __version__}
    
    app.router.add_route('GET', url_prefix,
                         handlers.IndexHandler().get,
                         name='hello-world:index')
    app.router.add_route('POST', url_prefix,
                         handlers.IndexHandler().post)

    app['scopes'].add(name='/hello-world',
                      title='Hello World!',
                      description='Provides access to POST to the "Hello World!" API',
                      available_to_client=True,
                      available_to_user=True,
                      requestable_by_all_clients=True)
