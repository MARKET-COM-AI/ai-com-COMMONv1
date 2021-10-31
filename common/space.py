#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from .base import *

#
# markets are managed as spaces where a combination of what and where.
#

class Space(ObjectBase):

    """

    """

    id: str = ""

    acl: str = ""
    name: str = ""
    tags: str = ""

    genre_id: str = ""
    where_id: str = ""

    program: str = ""
    storage: str = ""

    def verify(self, tables):

        results = []

        if not self.genre_id == "":
            if not self.genre_id in tables.genres:
                results.append([self, "genre_id key not able to be resolved"])

        if not self.where_id == "":
            if not self.where_id in tables.wheres:
                results.append([self, "where_id key not able to be resolved"])

        return results






