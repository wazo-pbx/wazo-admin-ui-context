# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_listing_url

from .service import ContextService
from .view import ContextView, ContextListingView

context = create_blueprint('context', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        ContextView.service = ContextService()
        ContextView.register(context, route_base='/contexts')
        register_flaskview(context, ContextView)

        ContextListingView.service = ContextService()
        ContextListingView.register(context, route_base='/contexts_listing')

        register_listing_url('context_by_type', 'context.ContextListingView:list_json_by_type')
        register_listing_url('context', 'context.ContextListingView:list_json')

        core.register_blueprint(context)
