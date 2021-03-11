from dataclasses import dataclass

from pymyarena.models.abc import ApiResponseABC


@dataclass
class ApiError(ApiResponseABC):
    """
    Represents Api error.

    Attrs:
        status: str
        message: str
    """

    status: str
    message: str
