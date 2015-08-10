'''
    1. 此部分主要是從admin的controller之AdminController改寫的，詳見：
        https://github.com/ckan/ckan/blob/master/ckan/controllers/admin.py
    2. 將原本使用CKAN core library的部分替換成Plugins toolkit library
        例如：
            ckan.lib.base.BaseController -> ckan.plugins.toolkit.BaseController
            ckan.lib.base.c -> ckan.plugins.toolkit.c
            ckan.lib.base._ -> ckan.plugins.toolkit._
        等等，以利此模組向後兼容。詳見： http://docs.ckan.org/en/latest/extensions/plugins-toolkit.html
    3. toolkit.render選擇template的順序為：
        1. ./templates/*
        2. ckan/ckan/templates/*
'''

import ckan.plugins.toolkit as toolkit

from ckan.plugins.toolkit import BaseController
from ckan.plugins.toolkit import c
from ckan.plugins.toolkit import _

class MainController(BaseController):
    def config(self):
        '''
            在「/ckan-admin/dsp-integrate」頁面render之前，先確認使用者是否為sysadmin。
        '''
        context = {'model': c.model,
                   'user': c.user, 'auth_user_obj': c.userobj}
        try:
            toolkit.check_access('sysadmin', context, {})
        except toolkit.NotAuthorized:
            toolkit.abort(401, _('Need to be system administrator to administer') )
        c.revision_change_state_allowed = True
        
        return toolkit.render('admin/base.html')

    def view(self):
        return toolkit.render('page.html')
