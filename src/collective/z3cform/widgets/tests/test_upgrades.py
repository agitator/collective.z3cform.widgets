# -*- coding: utf-8 -*-

from collective.z3cform.widgets.testing import INTEGRATION_TESTING
from collective.z3cform.widgets.upgrades import to3

import unittest


class Upgrade2to3TestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_update_dependencies(self):
        """Test plone.formwidget.contenttree resources were installed.
        """
        portal_js = self.portal.portal_javascripts
        portal_css = self.portal.portal_css
        js = '++resource++plone.formwidget.contenttree/contenttree.js'
        css = '++resource++plone.formwidget.contenttree/contenttree.css'

        # manually unistall resources to simulate previous profile
        portal_js.unregisterResource(js)
        portal_css.unregisterResource(css)
        self.assertNotIn(js, portal_js.getResourceIds())
        self.assertNotIn(css, portal_css.getResourceIds())

        # run the upgrade step and test resources are installed
        to3(self.portal)
        self.assertIn(js, portal_js.getResourceIds())
        self.assertIn(css, portal_css.getResourceIds())