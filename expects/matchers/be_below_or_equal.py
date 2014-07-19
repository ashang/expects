# -*- coding: utf-8 -*

from . import Matcher


class BeBelowOrEqual(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject <= self._expected

    @property
    def _description(self):
        return 'be below or equal {expected!r}'.format(expected=self._expected)
