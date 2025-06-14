############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Alexis Belmonte <alexbelm48@gmail.com>                        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from github.GithubObject import NonCompletableGithubObject, GraphQlObject, Attribute, NotSet

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import datetime


class Actor(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the Actor from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/interfaces#actor

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._avatarUrl: Attribute[str] = NotSet
        self._createdAt: Attribute[datetime.datetime] = NotSet
        self._login: Attribute[str] = NotSet
        self._resourcePath: Attribute[str] = NotSet
        self._updatedAt: Attribute[datetime.datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "avatarUrl": self._avatarUrl.value,
            "login": self._login.value,
            "resourcePath": self._resourcePath.value,
            "url": self._url.value
        })

    @property
    def avatarUrl(self) -> str:
        return self._avatarUrl.value

    @property
    def login(self) -> str:
        return self._login.value

    @property
    def resourcePath(self) -> str:
        return self._resourcePath.value

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "avatarUrl" in attributes:
            self._avatarUrl = self._makeStringAttribute(attributes["avatarUrl"])
        if "login" in attributes:
            self._login = self._makeStringAttribute(attributes["login"])
        if "resourcePath" in attributes:
            self._resourcePath = self._makeStringAttribute(attributes["resourcePath"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
