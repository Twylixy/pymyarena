from dataclasses import dataclass

from pymyarena.models.abc import ApiResponseABC


@dataclass
class ServerStatus(ApiResponseABC):
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
    data: dict  # noqa:WPS110
    server_id: str
    server_name: str
    server_address: str
    server_maxslots: str
    server_location: str
    server_type: str
    server_dateblock: str
    server_daystoblock: int


@dataclass
class GetMaps(ApiResponseABC):
    """
    Represents server maps.

    Attrs:
        status: str
        maps: list
    """

    status: str
    maps: list


@dataclass
class GetResources(ApiResponseABC):
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
