#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GuessIt - A library for guessing information from filenames
# Copyright (c) 2013 Nicolas Wack <wackou@gmail.com>
#
# GuessIt is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# GuessIt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function, unicode_literals

from guessit.test.guessittest import *
from guessit.fileutils import split_path

from guessit import PY2


class TestHashes(TestGuessit):
    def test_hashes(self):
        hashes = (
                  ('hash_mpc', u'8542ad406c15c8bd'),  # TODO: Check if this value is valid
                  ('hash_ed2k', u'ed2k://|file|1MB|1048576|AA3CC5552A9931A76B61A41D306735F7|/'),  # TODO: Check if this value is valid
                  ('hash_md5', u'5d8dcbca8d8ac21766f28797d6c3954c'),
                  )
        filename = '1MB'

        for hash_type, expected_value in hashes:
            guess = guess_file_info(file_in_same_dir(__file__, filename), None, hash_type)
            self.assertEquals(expected_value, guess.get(hash_type))


suite = allTests(TestHashes)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
