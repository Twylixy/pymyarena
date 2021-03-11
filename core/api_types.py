from core import models

api_types = {
    'status': models.ServerStatus,
    'start': models.ServerStart,
    'stop': models.ServerStop,
    'restart': models.SeverRestart,
    'changelevel': models.ServerChangeLevel,
    'getmaps': models.GetMaps,
    'consolecmd': models.ConsoleCMD,
    'getresources': models.GetResources,
    'apierr': models.ApiError,
}
