import ckan.plugins.toolkit as toolkit

from ckan.plugins.toolkit import BaseController
from ckan.plugins.toolkit import c
from ckan.plugins.toolkit import _

class MainController(BaseController):
    def config(self):
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
