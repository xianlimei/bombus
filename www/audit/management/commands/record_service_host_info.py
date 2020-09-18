"""
    同步主机资产信息
"""

#  Copyright (C) 2020  momosecurity
#
#  This file is part of Bombus.
#
#  Bombus is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Bombus is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Bombus.  If not, see <https://www.gnu.org/licenses/>.

import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


def sync_host():
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info('############ HOST SYNC STARTING #############')
        sync_host()
        logger.info('############## HOST SYNC END ################')
