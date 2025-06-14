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

from github.Actor import Actor
from github.ProjectItemContent import ProjectItemContent

if TYPE_CHECKING:
    import datetime


class ProjectItem(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the ProjectItem from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2item

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._content: Attribute[ProjectItemContent | None] = NotSet
        self._createdAt: Attribute[datetime.datetime] = NotSet
        self._creator: Attribute[Actor | None] = NotSet
        self._fieldValueByName: Attribute[ProjectItemFieldValue | None] = NotSet
        self._fieldValues: Attribute[list[ProjectItemFieldValueConnection]] = NotSet
        self._isArchived: Attribute[bool] = NotSet
        self._project: Attribute[Project] = NotSet
        self._type: Attribute[str] = NotSet
        self._updatedAt: Attribute[datetime.DateTime] = NotSet
