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

from github.GithubObject import Attribute, NotSet

from github.ProjectFieldConfiguration import ProjectFieldConfiguration
from github.ProjectSingleSelectFieldOption import ProjectSingleSelectFieldOption


class ProjectSingleSelectField(ProjectFieldConfiguration):
    """
    This class represents the ProjectV2IterationField from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#projectv2iterationfield

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._options: Attribute[list[ProjectSingleSelectFieldOption]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({
            "options": self._options.value
        })

    @property
    def options(self) -> list[ProjectSingleSelectFieldOption]:
        return self._options.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "options" in attributes:  # pragma: no branch
            self._options = self._makeListOfClassesAttribute(
                klass=ProjectSingleSelectFieldOption,
                value=attributes["options"]
            )
