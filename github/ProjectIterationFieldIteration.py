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

from typing import TYPE_CHECKING, Any

from github.GithubObject import NonCompletableGithubObject, GraphQlObject, Attribute, NotSet

if TYPE_CHECKING:
    import datetime


class ProjectIterationFieldIteration(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the ProjectV2IterationFieldIteration from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2iterationfielditeration

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._duration: Attribute[int] = NotSet
        self._start_date: Attribute[datetime.datetime] = NotSet
        self._title: Attribute[str] = NotSet
        self._title_html: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "duration": self._duration.value,
            "start_date": self._start_date.value,
            "title": self._title.value,
            "title_html": self._title_html.value
        })

    @property
    def duration(self) -> int:
        return self._duration.value

    @property
    def start_date(self) -> datetime.datetime:
        return self._start_date.value

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def title_html(self) -> str:
        return self._title_html.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)

        if "duration" in attributes:
            self._duration = self._makeIntAttribute(attributes["duration"])
        if "startDate" in attributes:
            self._start_date = self._makeDatetimeAttribute(attributes["startDate"])
        if "title" in attributes:
            self._title = self._makeStringAttribute(attributes["title"])
        if "titleHTML" in attributes:
            self._title_html = self._makeStringAttribute(attributes["titleHTML"])
