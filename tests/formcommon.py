#
#   The contents of this file are subject to the HACOS License Version 1.2
#   (the "License"); you may not use this file except in compliance with
#   the License.  Software distributed under the License is distributed
#   on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or
#   implied. See the LICENSE file for the specific language governing
#   rights and limitations under the License.  The Original Software
#   is "NetEpi Collection". The Initial Developer of the Original
#   Software is the Health Administration Corporation, incorporated in
#   the State of New South Wales, Australia.
#
#   Copyright (C) 2004-2011 Health Administration Corporation, Australian
#   Government Department of Health and Ageing, and others.
#   All Rights Reserved.
#
#   Contributors: See the CONTRIBUTORS file for details of contributions.
#
from cocklebur import form_ui

def get_testform():
    form = form_ui.Form(name='testform', text='Test Form', form_type='testform')
    section = form_ui.Section('Section 1')
    section.question(text='First Question',
        input = form_ui.YesNo('input_a', required=True,
                              summary='Input A'))
    section.question(text='Second Question',
        inputs = [
            form_ui.TextInput('q2a', pre_text='Part A'),
            form_ui.TextInput('q2b', pre_text='Part B'),
            form_ui.TextInput('q2c', pre_text='Part C'),
        ])
    form.append(section)
    form.question(text='Third Question',
        input = form_ui.RadioList('q3', required=True, direction='horizontal',
            choices=[
                ('a', 'A'),
                ('b', 'B'),
                ('c', 'C'),
            ]))
    return form
