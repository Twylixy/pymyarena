from core import Api

api = Api('token_here')
response = api.status()

print(response)
# ServerStatus(status='OK', online=1, ...)
