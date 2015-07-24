import asyncio

from apiox.core.handlers import BaseHandler
from apiox.core.response import JSONResponse

class IndexHandler(BaseHandler):
    def get(self, request):
        return JSONResponse(body={'title': 'Hello, World!',
                                  'instructions': "This is a test API. POST to it with the /hello-world scope to see something interesting happen after a few seconds."})

    def post(self, request):
        yield from self.require_authentication(request)

        yield from asyncio.sleep(5)

        return JSONResponse(body={'title': 'Hello, World!',
                                  'actually': 'Nothing happens.',
                                  'token': {'user': request.token.user,
                                            'client': request.token.client_id,
                                            'account': request.token.account_id,
                                            'scopes': request.token.scopes}})
