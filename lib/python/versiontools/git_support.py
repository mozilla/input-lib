#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#
# Copyright (C) 2011 enn.io UG (haftungsbeschränkt)
#
# Author: Jannis Leidel <jannis@leidel.info>
#
# This file is part of versiontools.
#
# versiontools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# versiontools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with versiontools.  If not, see <http://www.gnu.org/licenses/>.

"""
git support for versiontools
"""
import logging
import sys


class GitIntegration(object):
    """
    Git integration for versiontools
    """
    def __init__(self, repo):
        head = None
        try:
            # This path is for 0.3RC from pypi
            head = repo.head
            self._branch_nick = head.name
            self._commit_id = head.commit.hexsha
        except AttributeError:
            pass
        try:
            # This is for python-git 0.1.6 (that is in debian and ubuntu)
            head = [head for head in repo.heads if head.name==repo.active_branch][0]
            self._branch_nick = head.name
            self._commit_id = head.commit.id
        except (IndexError, KeyError):
            pass
        if head is None:
            raise ValueError("Unable to lookup head in %r" % repo)

    @property
    def revno(self):
        """
        Revision number of the branch
        """
        return self.commit_id_abbrev

    @property
    def commit_id(self):
        """
        The full commit id
        """
        return self._commit_id

    @property
    def commit_id_abbrev(self):
        """
        The abbreviated, 7 character commit id
        """
        return self._commit_id[:7]

    @property
    def branch_nick(self):
        """
        Nickname of the branch

        .. versionadded:: 1.0.4
        """
        return self._branch_nick

    @classmethod
    def from_source_tree(cls, source_tree):
        """
        Initialize :class:`~versiontools.git_support.GitIntegration` by
        pointing at the source tree.  Any file or directory inside the
        source tree may be used.
        """
        repo = None
        try:
            from git import Repo
            repo = Repo(source_tree)
        except Exception:
            from versiontools import get_exception_message
            message = get_exception_message(*sys.exc_info())
            logging.debug("Unable to get branch revision because "
                          "directory %r is not a git repo. Error: %s",
                          (source_tree, message))
        if repo:
            return cls(repo)
