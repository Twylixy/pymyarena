from dataclasses import dataclass


@dataclass
class ServerStatus(object):
    """
    Represents server status.

    Attrs:
        status: str
        online: int
        data: dict
        server_id: str
        server_name: str
        server_address: str
        server_maxslots: str
        server_location: str
        server_type: str
        server_dateblock: str
        server_daystoblock: int
    """

    status: str
    online: int
    data: dict
    server_id: str
    server_name: str
    server_address: str
    server_maxslots: str
    server_location: str
    server_type: str
    server_dateblock: str
    server_daystoblock: int


@dataclass
class ServerStart(object):
    """
    Represents server start data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class ServerStop(object):
    """
    Represents server stop data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class SeverRestart(object):
    """
    Represents server restart data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class ServerChangeLevel(object):
    """
    Represents server changelevel.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class GetMaps(object):
    """
    Represents server maps.

    Attrs:
        status: str
        maps: list
    """

    status: str
    maps: list


@dataclass
class ConsoleCMD(object):
    """
    Represents server execute cmd.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class GetResources(object):
    """
    Represents server resources.

    Attrs:
        status: str
        cpu_proc: str
        mem_used: str
        mem_quota: str
        mem_proc: str
        players: str
        players_max: str
        players_proc: str
        disk_used: str
        disk_quota: str
        disk_proc: str
    """

    status: str
    cpu_proc: str
    mem_used: str
    mem_quota: str
    mem_proc: str
    players: str
    players_max: str
    players_proc: str
    disk_used: str
    disk_quota: str
    disk_proc: str


@dataclass
class ApiError(object):
    """
    Represents Api error.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str
