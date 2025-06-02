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


class ProjectSingleSelectFieldOption(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the ProjectV2SingleSelectFieldOption from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2singleselectfieldoption

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        self._color: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._description_html: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._name_html: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "color": self._color.value,
            "description": self._description.value,
            "description_html": self._description_html.value,
            "name": self._name.value,
            "name_html": self._name_html.value
        })

    @property
    def color(self) -> str:
        return self._color.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def description_html(self) -> str:
        return self._description_html.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def name_html(self) -> str:
        return self._name_html.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "color" in attributes:  # pragma: no branch
            self._color = self._makeStringAttribute(value=attributes["color"])
        if "description" in attributes:  # pragma: no branch
            self._description = self._makeStringAttribute(value=attributes["description"])
        if "descriptionHTML" in attributes:  # pragma: no branch
            self._description_html = self._makeStringAttribute(value=attributes["descriptionHTML"])
        if "name" in attributes:  # pragma: no branch
            self._name = self._makeStringAttribute(value=attributes["name"])
        if "nameHTML" in attributes:  # pragma: no branch
            self._name_html = self._makeStringAttribute(value=attributes["nameHTML"])
