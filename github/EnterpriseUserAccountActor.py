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

from github.Enterprise import Enterprise
from github.EnterpriseServerInstallationMembershipConnection import EnterpriseServerInstallationMembershipConnection
from github.EnterpriseOrganizationMembershipConnection import EnterpriseOrganizationMembershipConnection
from github.User import User

from typing import Any


class EnterpriseUserAccountActor(Actor):
    """
    This class represents the EnterpriseUserAccount from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#enterpriseuseraccount

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._enterprise: Attribute[Enterprise] = NotSet
        self._enterpriseInstallations: Attribute[EnterpriseServerInstallationMembershipConnection] = NotSet
        self._name: Attribute[str | None] = NotSet
        self._organizations: Attribute[list[EnterpriseOrganizationMembershipConnection]] = NotSet
        self._user: Attribute[User] = NotSet

    @property
    def enterprise(self) -> Enterprise:
        return self._enterprise.value

    @property
    def enterpriseInstallations(self) -> EnterpriseServerInstallationMembershipConnection:
        return self._enterpriseInstallations.value

    @property
    def name(self) -> str | None:
        return self._name.value

    @property
    def organizations(self) -> list[EnterpriseOrganizationMembershipConnection]:
        return self._organizations.value

    @property
    def user(self) -> User:
        return self._user.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "enterprise" in attributes:
            self._enterprise = self._makeClassAttribute(
                klass=Enterprise,
                value=attributes["enterprise"]
            )
        if "enterpriseInstallations" in attributes:
            self._enterpriseInstallations = self._makeClassAttribute(
                klass=EnterpriseServerInstallationMembershipConnection,
                value=attributes["enterpriseInstallations"]
            )
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "organizations" in attributes:
            self._organizations = self._makeListOfClassesAttribute(
                klass=EnterpriseOrganizationMembershipConnection,
                value=attributes["organizations"]
            )
        if "user" in attributes:
            self._user = self._makeClassAttribute(
                klass=User,
                value=attributes["user"]
            )
