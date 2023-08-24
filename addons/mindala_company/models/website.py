# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _
from odoo.addons.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = "website"

    def get_suggested_controllers(self):
        suggested_controllers = super(Website, self).get_suggested_controllers()
        suggested_controllers.append((_('Company'), url_for('/company'), 'mindala_company'))
        return suggested_controllers

    def configurator_set_menu_links(self, menu_company, module_data):
        companies = module_data.get('#m4pcompany', [])
        for idx, company in enumerate(companies):
            new_company = self.env['mindala.m4pcompany'].create({
                'name': company['name'],
                'website_id': self.id,
            })
            company_menu_values = {
                'name': company['name'],
                'url': '/company/%s' % new_company.id,
                'sequence': company['sequence'],
                'parent_id': menu_company.id if menu_company else self.menu_id.id,
                'website_id': self.id,
            }
            if idx == 0:
                company_menu = self.env['website.menu'].search([('url', '=', '/company'), ('website_id', '=', self.id)])
                company_menu.write(company_menu_values)
            else:
                self.env['website.menu'].create(company_menu_values)
        super().configurator_set_menu_links(menu_company, module_data)

    def _search_get_details(self, search_type, order, options):
        result = super()._search_get_details(search_type, order, options)
        if search_type in ['companies', 'companies_only', 'all']:
            result.append(self.env['mindala.m4pcompany']._search_get_detail(self, order, options))
        return result
