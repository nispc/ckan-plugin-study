import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Dsp_IntegratePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'dsp_integrate')
        toolkit.add_ckan_admin_tab(config, 'dsp-integrate-config', 'DSP Integrate') 

    # IRoutes

    def before_map(self, map):
        controller = 'ckanext.dsp_integrate.controllers:MainController'
        map.connect('dsp-integrate-config', '/ckan-admin/dsp-integrate',
            controller=controller, action='config')
        map.connect('dsp-integrate-view', '/dsp-integrate',
            controller=controller, action='view')
        return map

    def after_map(self, map):
        return map
