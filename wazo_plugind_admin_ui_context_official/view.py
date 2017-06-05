# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from wazo_admin_ui.helpers.classful import LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response


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
