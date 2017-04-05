# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from wazo_admin_ui.helpers.classful import BaseDestinationView


class ContextDestinationView(BaseDestinationView):

    def list_json_by_type(self, type_):
        params = self._extract_params()
        params['type'] = type_
        contexts = self.service.list(**params)
        results = [{'id': context['id'], 'text': context['name']} for context in contexts['items']]
        return self._select2_response(results, contexts['total'], params)
