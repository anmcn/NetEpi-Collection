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

import sys
import os
from cocklebur.form_ui.pyload import pyload
from cocklebur.form_ui.xmlsave import xmlsave

def form_to_xml(filename):
    f = open(filename)
    try:
        form = pyload(f)
    finally:
        f.close()
    form.update_columns()
    form.name = os.path.basename(filename)[:-3]
    xmlsave(sys.stdout, form)

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        sys.exit('Usage: %s <form.py>' % sys.argv[0])
    form_to_xml(sys.argv[1])
