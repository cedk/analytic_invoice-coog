# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_teardown
from trytond.tests.test_tryton import doctest_checker


class AnalyticInvoiceTestCase(ModuleTestCase):
    'Test AnalyticInvoice module'
    module = 'analytic_invoice'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AnalyticInvoiceTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_analytic_invoice.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    # This test is commented as it requires account_asset in order to run, which
    #  we do not want. The test is required in analytic_invoice setup.py,
    # and account_asset is only in analytic_invoice extras_depend
    # suite.addTests(doctest.DocFileSuite('scenario_analytic_invoice_asset.rst',
    #         tearDown=doctest_teardown, encoding='utf-8',
    #         checker=doctest_checker,
    #         optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
