#!/bin/false

# Copyright (c) 2022 Vít Labuda. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#     disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#     products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from typing import Final, Type
from spideriment_ng_search.databases.drivers.DatabaseDriverIface import DatabaseDriverIface
from spideriment_ng_search.databases.drivers.mysql.MySQLDatabaseDriver import MySQLDatabaseDriver
from spideriment_ng_search.databases.registry.exc.DatabaseDriverNotFoundExc import DatabaseDriverNotFoundExc


class DatabaseDriverRegistry:
    _DATABASE_DRIVERS: Final[tuple[Type[DatabaseDriverIface], ...]] = (
        MySQLDatabaseDriver,
    )

    @classmethod
    def get_all_database_drivers(cls) -> dict[str, Type[DatabaseDriverIface]]:
        return {database_driver.get_database_driver_info().name: database_driver for database_driver in cls._DATABASE_DRIVERS}

    @classmethod
    def get_database_driver_by_name(cls, db_driver_name: str) -> Type[DatabaseDriverIface]:
        """
        :raises DatabaseDriverNotFoundExc
        """

        try:
            return cls.get_all_database_drivers()[db_driver_name]
        except KeyError:
            raise DatabaseDriverNotFoundExc(db_driver_name)
