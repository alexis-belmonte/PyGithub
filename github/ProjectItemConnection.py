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

from typing import Any

from github.GithubObject import NonCompletableGithubObject, GraphQlObject, Attribute, NotSet

from github.ProjectItemEdge import ProjectItemEdge
from github.ProjectItem import ProjectItem
from github.PageInfo import PageInfo


class ProjectItemConnection(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the ProjectItemConnection from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2itemconnection

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._edges: Attribute[list[ProjectItemEdge]] = NotSet
        self._nodes: Attribute[list[ProjectItem]] = NotSet
        self._pageInfo: Attribute[PageInfo] = NotSet
        self._totalCount: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "edges": self._edges.value,
            "nodes": self._nodes.value,
            "pageInfo": self._pageInfo.value,
            "totalCount": self._totalCount.value
        })

    @property
    def edges(self) -> list[ProjectItemEdge]:
        return self._edges.value

    @property
    def nodes(self) -> list[ProjectItem]:
        return self._nodes.value

    @property
    def pageInfo(self) -> PageInfo:
        return self._pageInfo.value

    @property
    def totalCount(self) -> int:
        return self._totalCount.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)

        if "edges" in attributes:
            self._edges = self._makeListOfClassesAttribute(
                klass=ProjectItemEdge,
                value=attributes["edges"]
            )
        if "nodes" in attributes:
            self._nodes = self._makeListOfClassesAttribute(
                klass=ProjectItem,
                value=attributes["nodes"]
            )
        if "pageInfo" in attributes:
            self._pageInfo = self._makeClassAttribute(
                klass=PageInfo,
                value=attributes["pageInfo"]
            )
        if "totalCount" in attributes:
            self._totalCount = self._makeIntAttribute(attributes["totalCount"])
