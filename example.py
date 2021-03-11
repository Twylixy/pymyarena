from pymyarena.api import Api

api = Api('token_here')
response = api.status()

print(response)  # noqa:WPS421
# ServerStatus(status='OK', online=1, ...)
