"""
The MIT License (MIT)

Copyright (c) 2020 Skelmis

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import logging
import sys
import unittest

from discord.ext import commands

from AntiSpam import Guild, User, AntiSpamHandler
from AntiSpam.static import Static


class TestGuild(unittest.TestCase):
    """
    Used to test the ASH object (AntiSpamHandler)
    """

    def setUp(self):
        """
        Simply setup our Guild obj before usage
        """
        self.ash = AntiSpamHandler(commands.Bot(command_prefix="!"))
        self.ash.guilds = Guild(
            None, 12, Static.DEFAULTS, logger=logging.getLogger(__name__)
        )
        self.ash.guilds = Guild(
            None, 15, Static.DEFAULTS, logger=logging.getLogger(__name__)
        )
        self.ash.guilds[0] = User(
            None, 20, 15, Static.DEFAULTS, logger=logging.getLogger(__name__)
        )

    def test_defaults(self):
        self.assertEqual(self.ash.options, Static.DEFAULTS)

    # TODO Add a ensureRaises test for each setable option...
