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

from github.GithubObject import Attribute, NotSet
from github.Actor import Actor
from github.AnnouncementBanner import AnnouncementBanner

if TYPE_CHECKING:
    import datetime


class OrganizationActor(Actor):
    """
    This class represents the Organization from Project V2.

    The reference can be found here:
    https://docs.github.com/en/graphql/reference/objects#organization

    The OpenAPI schema can be found at
    - /components/schemas/projects-v2
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._annoucementBanner: Attribute[AnnouncementBanner | None] = NotSet
        self._anyPinnableItems: Attribute[bool] = NotSet
        self._archivedAt: Attribute[datetime.datetime | None] = NotSet
        self._auditLog: Attribute[OrganizationAuditEntryConnection] = NotSet
        self._description: Attribute[str | None] = NotSet
        self._descriptionHTML: Attribute[str | None] = NotSet
        self._domains: Attribute[VerifiableDomainConnection] = NotSet
        self._email: Attribute[str | None] = NotSet
        self._enterpriseOwners: Attribute[OrganizationEnterpriseOwnerConnection] = NotSet
        self._estimatedNextSponsorsPayoutInCents: Attribute[int] = NotSet
        self._hasSponsorsListing: Attribute[bool] = NotSet
        self._interactionAbility: Attribute[RepositoryInteractionAbility | None] = NotSet
        self._ipAllowListEnabledSetting: Attribute[IpAllowListEnabledSetting] = NotSet
        self._ipAllowListEntries: Attribute[IpAllowListEntryConnection] = NotSet
        self._ipAllowListForInstalledAppsEnabledSetting: Attribute[IpAllowListEnabledSetting] = NotSet
        self._isSponsoredBy: Attribute[bool] = NotSet
        self._isSponsoringViewer: Attribute[bool] = NotSet
        self._isVerified: Attribute[bool] = NotSet
        self._issueTypes: Attribute[IssueTypeConnection] = NotSet
        self._itemShowcase: Attribute[ProfileItemShowcase] = NotSet
        self._lifetimeReceivedSponsorshipValues: Attribute[SponsorAndLifetimeValueConnection] = NotSet
        self._location: Attribute[str | None] = NotSet
        self._mannequins: Attribute[MannequinConnection] = NotSet
        self._memberStatuses: Attribute[OrganizationMemberStatusConnection] = NotSet
        self._membersCanForkPrivateRepositories: Attribute[bool] = NotSet
        self._membersWithRole: Attribute[OrganizationMemberConnection] = NotSet
        self._monthlyEstimatedSponsorsIncomeInCents: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._newTeamResourcePath: Attribute[str] = NotSet
        self._newTeamUrl: Attribute[str] = NotSet
        self._notificationDeliveryRestrictionEnabledSetting: Attribute[NotificationRestrictionSettingValue] = NotSet
        self._organizationBillingEmail: Attribute[str | None] = NotSet
        self._packages: Attribute[PackageConnection] = NotSet
        self._pendingMembers: Attribute[OrganizationPendingMemberConnection] = NotSet
        self._pinnableItems: Attribute[PinnableItemConnection] = NotSet
        self._pinnedItems: Attribute[PinnableItemConnection] = NotSet
        self._pinnedItemsRemaining: Attribute[int] = NotSet
        self._projects: Attribute[ProjectConnection] = NotSet
        self._projectsResourcePath: Attribute[str] = NotSet
        self._
