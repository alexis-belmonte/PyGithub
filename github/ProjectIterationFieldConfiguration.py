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

from typing import TYPE_CHECKING

from github.GithubObject import NonCompletableGithubObject, GraphQlObject, Attribute, NotSet
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.ProjectIterationFieldIteration import ProjectIterationFieldIteration


class ProjectIterationFieldConfiguration(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the base ProjectV2FieldConfiguration from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2iterationfieldconfiguration

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        self._completed_iterations: Attribute[PaginatedList[ProjectIterationFieldIteration]] = NotSet
        self._duration: Attribute[int] = NotSet
        self._iterations: Attribute[PaginatedList[ProjectIterationFieldIteration]] = NotSet
        self._startDay: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "duration": self._duration.value,
            "startDay": self._startDay.value
        })

    @property
    def completed_iterations(self) -> PaginatedList[ProjectIterationFieldIteration]:
        return self._completed_iterations.value

    @property
    def duration(self) -> int:
        return self._duration.value

    @property
    def iterations(self) -> PaginatedList[ProjectIterationFieldIteration]:
        return self._iterations.value

    @property
    def start_day(self) -> int:
        return self._startDay.value
