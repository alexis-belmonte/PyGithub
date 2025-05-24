############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Benoit Latinier <benoit@latinier.fr>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Lars Kellogg-Stedman <lars@oddbit.com>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Alexis Belmonte <alexbelm48@gmail.com>                        #
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

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.GithubObject
import github.NamedUser
import github.Organization
import github.Repository
from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, GraphQlObject, NotSet, Opt
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.NamedUser import NamedUser


class Project(CompletableGithubObject, GraphQlObject):
    """
    This class represents GraphQL-based Project V2.

    The reference can be found here
    https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2

    """

    def _initAttributes(self) -> None:
        self._closed: Attribute[bool] = NotSet
        self._closed_at: Attribute[datetime] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[NamedUser] = NotSet
        self._fields: Attribute[PaginatedList[ProjectFieldConfiguration]] = NotSet
        self._full_database_id: Attribute[str] = NotSet
        self._items: Attribute[PaginatedList[ProjectItemConnection]] = NotSet
        self._number: Attribute[int] = NotSet
        self._owner: Attribute[NamedUser] = NotSet
        self._public: Attribute[bool] = NotSet
        self._readme: Attribute[str] = NotSet
        self._repositories: Attribute[PaginatedList[Repository]] = NotSet
        self._resource_path: Attribute[str] = NotSet
        self._short_description: Attribute[str] = NotSet
        self._status_updates: Attribute[PaginatedList[ProjectStatusUpdate]] = NotSet
        self._teams: Attribute[PaginatedList[Team]] = NotSet
        self._template: Attribute[bool] = NotSet
        self._title: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._viewer_can_reopen: Attribute[bool] = NotSet
        self._viewer_can_close: Attribute[bool] = NotSet
        self._viewer_can_update: Attribute[bool] = NotSet
        self._views: Attribute[PaginatedList[ProjectView]] = NotSet
        self._workflows: Attribute[ProjectWorkflows] = NotSet

    @property
    def closed(self) -> bool:
        return self._closed.value

    @property
    def closed_at(self) -> datetime:
        return self._closed_at.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def creator(self) -> github.NamedUser.NamedUser:
        return self._creator.value

    @property
    def fields(self) -> PaginatedList[github.ProjectFieldConfiguration.ProjectFieldConfiguration]:
        return self._fields.value

    @property
    def full_database_id(self) -> str:
        return self._full_database_id.value

    @property
    def items(self) -> PaginatedList[github.ProjectItemConnection.ProjectItemConnection]:
        return self._items.value

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def owner(self) -> github.NamedUser.NamedUser:
        return self._owner.value

    @property
    def public(self) -> bool:
        return self._public.value

    @property
    def readme(self) -> str:
        return self._readme.value

    @property
    def repositories(self) -> PaginatedList[github.Repository.Repository]:
        return self._repositories.value

    @property
    def resource_path(self) -> str:
        return self._resource_path.value

    @property
    def short_description(self) -> str:
        return self._short_description.value

    @property
    def status_updates(self) -> PaginatedList[github.ProjectStatusUpdate.ProjectStatusUpdate]:
        return self._status_updates.value

    @property
    def teams(self) -> PaginatedList[github.Team.Team]:
        return self._teams.value

    @property
    def template(self) -> bool:
        return self._template.value

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def viewer_can_reopen(self) -> bool:
        return self._viewer_can_reopen.value

    @property
    def viewer_can_close(self) -> bool:
        return self._viewer_can_close.value

    @property
    def viewer_can_update(self) -> bool:
        return self._viewer_can_update.value

    @property
    def views(self) -> PaginatedList[github.ProjectView.ProjectView]:
        return self._views.value

    @property
    def workflows(self) -> github.ProjectWorkflow.ProjectWorkflows:
        return self._workflows.value

    def delete(self) -> None:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql/reference/mutations>`_ with a mutation to delete a project
        <https://docs.github.com/en/graphql/reference/mutations#deleteprojectv2>
        """
        variables = {
            "projectId": self._id.value
        }
        self._requester.graphql_named_mutation(
            mutation_name="deleteProjectV2",
            mutation_input=variables,
            output_schema="deleteProjectV2"
        )

    def edit(
        self,
        name: Opt[str] = NotSet,
        body: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        organization_permission: Opt[str] = NotSet,
        private: Opt[bool] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /projects/{project_id} <https://docs.github.com/en/rest/reference/projects#update-a-project>`_
        """
        assert name is NotSet or isinstance(name, str), name
        assert body is NotSet or isinstance(body, str), body
        assert state is NotSet or isinstance(state, str), state
        assert organization_permission is NotSet or isinstance(organization_permission, str), organization_permission
        assert private is NotSet or isinstance(private, bool), private
        patch_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "body": body,
                "state": state,
                "organization_permission": organization_permission,
                "private": private,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        self._useAttributes(data)

    def get_columns(self) -> PaginatedList[github.ProjectColumn.ProjectColumn]:
        """
        :calls: `GET /projects/{project_id}/columns <https://docs.github.com/en/rest/reference/projects#list-project-columns>`_
        """

        return PaginatedList(
            github.ProjectColumn.ProjectColumn,
            self._requester,
            self.columns_url,
            None,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )

    def create_column(self, name: str) -> github.ProjectColumn.ProjectColumn:
        """
        calls: `POST /projects/{project_id}/columns <https://docs.github.com/en/rest/reference/projects#create-a-project-column>`_
        """
        assert isinstance(name, str), name
        post_parameters = {"name": name}
        import_header = {"Accept": Consts.mediaTypeProjectsPreview}
        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.url}/columns", headers=import_header, input=post_parameters
        )
        return github.ProjectColumn.ProjectColumn(self._requester, headers, data)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "columns_url" in attributes:  # pragma no branch
            self._columns_url = self._makeStringAttribute(attributes["columns_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "organization_permission" in attributes:  # pragma no branch
            self._organization_permission = self._makeStringAttribute(attributes["organization_permission"])
        if "owner_url" in attributes:  # pragma no branch
            self._owner_url = self._makeStringAttribute(attributes["owner_url"])
        if "private" in attributes:  # pragma no branch
            self._private = self._makeBoolAttribute(attributes["private"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
