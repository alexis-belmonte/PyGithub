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

from datetime import datetime
from typing import TYPE_CHECKING, Any

from github.GithubObject import NonCompletableGithubObject, GraphQlObject, Attribute, NotSet

import github.Project

if TYPE_CHECKING:
    from github.Project import Project


class ProjectFieldConfiguration(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the base ProjectFieldConfiguration from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/unions#projectv2fieldconfiguration

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._data_type: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._project: Attribute[Project] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "name": self._name.value,
            "data_type": self._data_type.value,
            "created_at": self._created_at.value,
            "updated_at": self._updated_at.value
        })

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def data_type(self) -> str:
        return self._data_type.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def project(self) -> "Project":
        return self._project.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "createdAt" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["createdAt"])
        if "dataType" in attributes:
            self._data_type = self._makeStringAttribute(attributes["dataType"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "project" in attributes:
            self._project = self._makeClassAttribute(github.Project.Project, attributes["project"])
        if "updatedAt" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updatedAt"])
