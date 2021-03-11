# PyMyArena API (Core)

This is a API Core for MyArena Server API ([myarena.ru](https://www.myarena.ru/))

## Download

```
git clone https://github.com/Twylixy/pymyarena.git
```

## How to use?

Place core in the same directory of our project

```
from pymyarena.api import Api

api = Api('token_here')
response = api.status()

print(response)
# ServerStatus(status='OK', online=1, ...)
```

## Documentation

dev...
