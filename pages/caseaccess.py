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
from cocklebur import dbobj
from casemgr import globals
from pages import page_common
import config

class PageOps(page_common.PageOpsBase):
    def unsaved_check(self, ctx):
        if ctx.locals.case.acl.db_has_changed():
            raise page_common.ConfirmSave

    def commit(self, ctx):
        log = ctx.locals.case.acl.db_desc()
        ctx.locals.case.user_log(log)
        ctx.locals.case.acl.db_update()
        globals.db.commit()
        if log:
            ctx.add_message('Case access controls updated')

    def revert(self, ctx):
        ctx.locals.case.acl.db_revert()

    def do_update(self, ctx, ignore):
        self.commit(ctx)
        ctx.pop_page()

    def do_pt_search(self, ctx, op, *args):
        if op == 'info':
            unit_id = ctx.locals.pt_search.pt_available[int(args[0])].unit_id
            ctx.push_page('unitview', unit_id)
        else:
            ctx.locals.case.acl.do(op, *args)

pageops = PageOps()

def page_enter(ctx):
    ctx.locals.case.load_acl()
    ctx.locals.pt_search = ctx.locals.case.acl
    ctx.add_session_vars('pt_search')

def page_leave(ctx):
    if hasattr(ctx.locals, 'case'):
        ctx.locals.case.unload_acl()
    ctx.del_session_vars('pt_search')

def page_display(ctx):
    ctx.run_template('caseaccess.html')

def page_process(ctx):
    if pageops.page_process(ctx):
        return
