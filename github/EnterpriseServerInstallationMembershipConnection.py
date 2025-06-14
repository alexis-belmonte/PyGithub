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

from github.EnterpriseServerInstallationMembershipEdge import EnterpriseServerInstallationMembershipEdge
from github.EnterpriseServerInstallation import EnterpriseServerInstallation
from github.PageInfo import PageInfo


class EnterpriseServerInstallationMembershipConnection(NonCompletableGithubObject, GraphQlObject):
    """
    This class represents the EnterpriseServerInstallationMembershipConnection from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#enterpriseserverinstallationmembershipconnection

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()

        self._edges: Attribute[list[EnterpriseServerInstallationMembershipEdge | None] = NotSet
        self._nodes: Attribute[list[EnterpriseServerInstallation] | None] = NotSet
        self._pageInfo: Attribute[PageInfo] = NotSet
        self._totalCount: Attribute[int] = NotSet

    @property
    def edges(self) -> list[EnterpriseServerInstallationMembershipEdge | None]:
        return self._edges.value

    @property
    def nodes(self) -> list[EnterpriseServerInstallation | None]:
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
            self._edges = self._makeListAttribute(
                klass=EnterpriseServerInstallationMembershipEdge,
                value=attributes["edges"]
            )
        if "nodes" in attributes:
            self._nodes = self._makeListAttribute(
                klass=EnterpriseServerInstallation,
                value=attributes["nodes"]
            )
        if "pageInfo" in attributes:
            self._pageInfo = self._makeClassAttribute(
                klass=PageInfo,
                value=attributes["pageInfo"]
            )
        if "totalCount" in attributes:
            self._totalCount = self._makeIntAttribute(attributes["totalCount"])
