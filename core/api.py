import json
import logging

import requests

from core import errors, models
from core.api_types import api_types


class Api(object):
    """
    Represents MyArena Server API.

    Args:
        token: str

    Attrs:
        token: str
        api_url: str
    """

    def __init__(self, token: str) -> None:
        """
        Represents MyArena Server API.

        Args:
            token: str

        Attrs:
            token: str
            api_url: str
        """
        self.logger = logging.getLogger()
        self.token = token
        self.api_url = 'https://www.myarena.ru/api.php?query={0}&token={1}'

    def send_request(self, query: str) -> object:
        """
        Send request to API.

        Args:
            query: str

        Returns:
            response

        Raises:
            ApiErr
        """
        response = requests.get(
            self.api_url.format(query, self.token),
        )

        response.raise_for_status()
        response_data = json.loads(response.content.decode('utf-8'))

        if response_data.get('status') != 'OK':
            raise errors.ApiErr(
                api_types.get('apierr')(**response_data),
            )

        return api_types.get(query)(**response_data)

    def status(self) -> models.ServerStatus:
        """
        Get server status.

        Returns:
            ApiData
        """
        return self.send_request('status')

    def start(self) -> models.ServerStart:
        """
        Start server.

        Returns:
            ApiData
        """
        return self.send_request('start')

    def stop(self) -> models.ServerStop:
        """
        Stop server.

        Returns:
            ApiData
        """
        return self.send_request('stop')

    def restart(self) -> models.SeverRestart:
        """
        Restart server.

        Returns:
            ApiData
        """
        return self.send_request('restart')

    def changelevel(self, map_name: str) -> models.ServerChangeLevel:
        """
        Change server level.

        Args:
            map_name: str

        Returns:
            ApiData
        """
        return self.send_request(
            'changelevel&map={0}'.format(
                map_name,
            ),
        )

    def getmaps(self) -> models.GetMaps:
        """
        Get server maps.

        Returns:
            ApiData
        """
        return self.send_request('getmaps')

    def consolecmd(self, command: str) -> models.ConsoleCMD:
        """
        Execute command.

        Args:
            command: str

        Returns:
            ApiData
        """
        return self.send_request(
            'consolecmd&cmd={0}'.format(
                command,
            ),
        )

    def getresources(self) -> models.GetResources:
        """
        Get server resources.

        Returns:
            ApiData
        """
        return self.send_request('getresources')
