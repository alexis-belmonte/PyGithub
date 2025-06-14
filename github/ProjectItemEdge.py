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

from github.ProjectItem import ProjectItem

from typing import Any


class ProjectItemEdge(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the ProjectItemEdge from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2itemedge

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._cursor: Attribute[str] = NotSet
        self._node: Attribute[ProjectItem] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "node": self._node.value,
            "cursor": self._cursor.value
        })

    @property
    def cursor(self) -> str:
        return self._cursor.value

    @property
    def node(self) -> ProjectItem:
        return self._node.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)

        if "cursor" in attributes:
            self._cursor = self._makeStringAttribute(attributes["cursor"])
        if "node" in attributes:
            self._node = self._makeClassAttribute(ProjectItem, attributes["node"])
