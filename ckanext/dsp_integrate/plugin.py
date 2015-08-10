# -*- coding: utf8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Dsp_IntegratePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    '''
        IRoutes為增加路由所使用的Interface
        詳見：
            1. 教學文： http://rossjones.github.io/ckan-plugins-iroutes/
            2. Plugin interfaces reference： http://docs.ckan.org/en/latest/extensions/plugin-interfaces.html
    '''
    plugins.implements(plugins.IRoutes)

    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'dsp_integrate')
        
        '''
            在Ckan的後台（/ckan-admin）加入DSP Integrate的設定頁
            dsp-integrate-config為route_name（詳見before_map）
        '''
        toolkit.add_ckan_admin_tab(config, 'dsp-integrate-config', 'DSP Integrate') 

    # IRoutes

    def before_map(self, map):
        controller = 'ckanext.dsp_integrate.controllers:MainController'
        
        '''
            map.connect()是pylons的Named Routes
            詳見：
                1.http://pylonsbook.com/en/1.0/urls-routing-and-dispatch.html
        '''
        map.connect('dsp-integrate-config', '/ckan-admin/dsp-integrate',
            controller=controller, action='config')
        map.connect('dsp-integrate-view', '/dsp-integrate',
            controller=controller, action='view')
            
        return map

    def after_map(self, map):
        return map
