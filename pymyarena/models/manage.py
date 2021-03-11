from dataclasses import dataclass

from pymyarena.models.abc import ApiResponseABC


@dataclass
class ServerStart(ApiResponseABC):
    """
    Represents server start data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class ServerStop(ApiResponseABC):
    """
    Represents server stop data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class SeverRestart(ApiResponseABC):
    """
    Represents server restart data.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class ConsoleCMD(ApiResponseABC):
    """
    Represents server execute cmd.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str


@dataclass
class ServerChangeLevel(ApiResponseABC):
    """
    Represents server changelevel.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str
