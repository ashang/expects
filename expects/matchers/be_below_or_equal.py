# -*- coding: utf-8 -*

from .matcher import Matcher


class BeBelowOrEqual(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject <= self._expected

    def _description(self, subject):
        return 'be below or equal {expected!r}'.format(expected=self._expected)
