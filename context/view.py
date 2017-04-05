# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from wazo_admin_ui.helpers.classful import BaseDestinationView


class ContextDestinationView(BaseDestinationView):

    def list_json(self):
        params = self._extract_params()
        ivrs = self.service.list(**params)
        results = [{'id': ivr['id'], 'text': ivr['name']} for ivr in ivrs['items']]
        return self._select2_response(results, ivr['total'], params)
