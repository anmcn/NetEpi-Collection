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

import inspect

def getclassattr(cls, attr):
    for c in inspect.getmro(cls):
        if hasattr(c, attr):
            return getattr(c, attr)

def callall(inst, methname, *args, **kwargs):
    """
    Call the named method (if it exists) on all base cases in the MRO

    super() for new-style classes does something somewhat equivalent,
    but not all our classes are new-style, and there are other caveats.
    """
    for cls in inspect.getmro(inst.__class__):
        cls_meth = cls.__dict__.get(methname)
        if cls_meth is not None:
            cls_meth(inst, *args, **kwargs)
