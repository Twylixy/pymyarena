from pymyarena.models import err, info, manage

api_types = {
    'status': info.ServerStatus,
    'start': manage.ServerStart,
    'stop': manage.ServerStop,
    'restart': manage.SeverRestart,
    'changelevel': manage.ServerChangeLevel,
    'getmaps': info.GetMaps,
    'consolecmd': manage.ConsoleCMD,
    'getresources': info.GetResources,
    'apierr': err.ApiError,
}
