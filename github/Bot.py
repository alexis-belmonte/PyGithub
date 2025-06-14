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

from github.GithubObject import Attribute, NotSet
from github.Actor import Actor

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import datetime


class Bot(Actor):
    """
    This class represents the Bot from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#bot

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._createdAt: Attribute[datetime.datetime] = NotSet
        self._updatedAt: Attribute[datetime.datetime] = NotSet

    @property
    def createdAt(self) -> datetime.datetime:
        return self._createdAt.value

    @property
    def updatedAt(self) -> datetime.datetime:
        return self._updatedAt.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "createdAt" in attributes:
            self._createdAt = self._makeDatetimeAttribute(attributes["createdAt"])
        if "updatedAt" in attributes:
            self._updatedAt = self._makeDatetimeAttribute(attributes["updatedAt"])
