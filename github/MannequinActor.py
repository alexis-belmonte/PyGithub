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
from github.User import User

from typing import Any


class MannequinActor(Actor):
    """
    This class represents the Mannequin from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#mannequin

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._claimant: Attribute[User | None] = NotSet
        self._email: Attribute[str | None] = NotSet

    @property
    def claimant(self) -> User | None:
        return self._claimant.value

    @property
    def email(self) -> str | None:
        return self._email.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "claimant" in attributes:
            self._claimant = self._makeClassAttribute(
                klass=User,
                value=attributes["claimant"]
            )
        if "email" in attributes:
            self._email = self._makeStringAttribute(attributes["email"])
