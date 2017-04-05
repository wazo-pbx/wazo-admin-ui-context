# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_listing_url

from .service import ContextService
from .view import ContextDestinationView

context = create_blueprint('context', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        ContextDestinationView.service = ContextService(config['confd'])
        ContextDestinationView.register(context, route_base='/context_list')

        register_listing_url('contexts', 'context.ContextDestinationView:list_json')

        core.register_blueprint(context)
