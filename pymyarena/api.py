import logging

import requests

from pymyarena.api_types import api_types
from pymyarena.models import abc, info, manage


class Api(object):
    """Represents MyArena Server API."""

    def __init__(self, token: str) -> None:
        """
        Initialize API object.

        Args:
            token: str

        Attrs:
            token: str
            api_url: str
        """
        self.logger = logging.getLogger()
        self.token = token
        self.api_url = 'https://www.myarena.ru/api.php?query={0}&token={1}'

    def status(self) -> info.ServerStatus:
        """
        Get server status.

        Returns:
            ApiData
        """
        return self._send_request('status')

    def start(self) -> manage.ServerStart:
        """
        Start server.

        Returns:
            ApiData
        """
        return self._send_request('start')

    def stop(self) -> manage.ServerStop:
        """
        Stop server.

        Returns:
            ApiData
        """
        return self._send_request('stop')

    def restart(self) -> manage.SeverRestart:
        """
        Restart server.

        Returns:
            ApiData
        """
        return self._send_request('restart')

    def changelevel(self, map_name: str) -> manage.ServerChangeLevel:
        """
        Change server level.

        Args:
            map_name: str

        Returns:
            ApiData
        """
        return self._send_request(
            'changelevel&map={0}'.format(
                map_name,
            ),
        )

    def getmaps(self) -> info.GetMaps:
        """
        Get server maps.

        Returns:
            ApiData
        """
        return self._send_request('getmaps')

    def consolecmd(self, command: str) -> manage.ConsoleCMD:
        """
        Execute command.

        Args:
            command: str

        Returns:
            ApiData
        """
        return self._send_request(
            'consolecmd&cmd={0}'.format(
                command,
            ),
        )

    def getresources(self) -> info.GetResources:
        """
        Get server resources.

        Returns:
            ApiData
        """
        return self._send_request('getresources')

    def _send_request(self, query: str) -> abc.ApiResponseABC:
        """
        Send request to API.

        Args:
            query: str

        Returns:
            response

        Raises:
            ApiErr : unsuccessful request
        """
        response = requests.get(
            self.api_url.format(query, self.token),
        )

        response.raise_for_status()
        response_data = response.json()

        if response_data.get('status') != 'OK':
            return api_types['apierr'](**response_data)

        if 'consolecmd' in query:
            query = 'consolecmd'
        elif 'changelevel':
            query = 'changelevel'

        return api_types[query](**response_data)
