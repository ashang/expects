# -*- coding: utf-8 -*

from mamba import describe, context

from expects import *
from expects.testing import failure


with describe('equal'):
    def it_should_pass_if_number_equals_expected():
        expect(1).to(equal(1))

    def it_should_fail_if_number_does_not_equal_expected():
        with failure('Expected 1 to equal 2'):
            expect(1).to(equal(2))

    with context('#negated'):
        def it_should_pass_if_number_does_not_equal_expected():
            expect(1).not_to(equal(2))

        def it_should_fail_if_number_equals_expected():
            with failure('Expected 1 not to equal 1'):
                expect(1).not_to(equal(1))
