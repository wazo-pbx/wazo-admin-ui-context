# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (SubmitField,
                            StringField,
                            IntegerField,
                            SelectField,
                            FormField,
                            FieldList,
                            BooleanField)
from wtforms.validators import InputRequired, Length

from wazo_admin_ui.helpers.form import BaseForm


class BaseRangesForm(BaseForm):
    start = StringField(l_('Start'), validators=[InputRequired(), Length(max=16)])
    end = StringField(l_('End'), validators=[Length(max=16)])


class IncallRangesForm(BaseRangesForm):
    did_length = IntegerField(l_('DID length'), validators=[InputRequired()])


class ContextForm(BaseForm):
    enabled = BooleanField(l_('Enabled'), default=True)
    name = StringField(l_('Name'), validators=[InputRequired(), Length(max=39)])
    label = StringField(l_('Label'), validators=[InputRequired(), Length(max=128)])
    type = SelectField(l_('Type'),
                       choices=[('internal', l_('Internal')),
                                ('incall', l_('Incall')),
                                ('outcall', l_('Outcall')),
                                ('services', l_('Services')),
                                ('others', l_('Others'))],
                       validators=[InputRequired()])
    description = StringField(l_('Description'))
    user_ranges = FieldList(FormField(BaseRangesForm))
    queue_ranges = FieldList(FormField(BaseRangesForm))
    group_ranges = FieldList(FormField(BaseRangesForm))
    conference_room_ranges = FieldList(FormField(BaseRangesForm))
    incall_ranges = FieldList(FormField(IncallRangesForm))
    submit = SubmitField(l_('Submit'))
