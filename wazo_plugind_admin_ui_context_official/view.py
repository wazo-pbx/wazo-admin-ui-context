# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import ContextForm


class ContextView(BaseView):
    resource_name = 'context'
    form = ContextForm
    resource = l_('Context')

    @classy_menu_item('.advanced.contexts', l_('Contexts'), order=3, icon="random")
    def index(self):
        return super().index()


class ContextListingView(LoginRequiredView):

    def list_json_by_type(self, type_):
        return self._list_json(type_)

    def list_json(self):
        return self._list_json()

    def _list_json(self, type_=None):
        params = extract_select2_params(request.args)
        if type_:
            params['type'] = type_
        contexts = self.service.list(**params)
        results = [{'id': context['name'], 'text': context['label']} for context in contexts['items']]
        return jsonify(build_select2_response(results, contexts['total'], params))
