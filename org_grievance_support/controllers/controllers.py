# -*- coding: utf-8 -*-
from odoo import http,_
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager

class OrgGrievanceSupport(http.Controller):

    @http.route('/grievance/portal', type='http', auth='public', website=True)
    def document_upload(self, **kw):
        return request.render("org_grievance_support.my_controller_form")

    @http.route('/submit_data', type='http', auth="public", website=True)
    def submit_grievance_data(self, **post):
        print("\n\n\n\n\n\n post=========>>",post)
        name = post.get('name')
        email = post.get('email')
        print("\n\n\n-----name",name)
        print("\n\n\n-----email",email)
        return request.render("org_grievance_support.RegisterMessage")

    @http.route(['/my/grievance', '/my/grievance/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_grievances(self, **kwargs):
        values = self._prepare_grievance_portal_rendering_values(quotation_page=False, **kwargs)
        request.session['my_orders_history'] = values['orders'].ids[:100]
        return request.render("org_grievance_support.portal_my_grievances",values)
        # return request.render("sale.portal_my_orders", values)

    def _prepare_portal_gra_layout_values(self):
        """Values for /my/* templates rendering.

        Does not include the record counts.
        """
        # get customer sales rep
        sales_user_sudo = request.env['res.users']
        partner_sudo = request.env.user.partner_id
        if partner_sudo.user_id and not partner_sudo.user_id._is_public():
            sales_user_sudo = partner_sudo.user_id
        else:
            fallback_sales_user = partner_sudo.commercial_partner_id.user_id
            if fallback_sales_user and not fallback_sales_user._is_public():
                sales_user_sudo = fallback_sales_user

        return {
            'sales_user': sales_user_sudo,
            'page_name': 'home',
        }

    def grievance_domain(self, partner):
        return [
            ('employee_id', 'in', [partner.id]),
        ]

    def _get_gra_searchbar_sortings(self):
        return {
            'date': {'label': _('Order Date'), 'order': 'create_date desc'},
            # 'name': {'label': _('Reference'), 'order': 'name'},
            # 'stage': {'label': _('Stage'), 'order': 'state'},
        }

    def _prepare_grievance_portal_rendering_values(
        self, page=1, date_begin=None, date_end=None, sortby=None, quotation_page=False, **kwargs
    ):
        SaleOrder = request.env['employee.grievance']

        if not sortby:
            sortby = 'date'

        partner = request.env.user.partner_id
        print("\n\n\n\n------------partner",partner)
        values = self._prepare_portal_gra_layout_values()

        url = "/my/grievance"
        domain = self.grievance_domain(partner)
        domain=[]
        print("\n\n\n\n-------domain",domain)

        searchbar_sortings = self._get_gra_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        _items_per_page = 100

        pager_values = portal_pager(
            url=url,
            total=SaleOrder.search_count(domain),
            page=page,
            step=100,
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
        )
        orders = SaleOrder.search(domain, order=sort_order, limit=100, offset=pager_values['offset'])

        values.update({
            'date': date_begin,
            'quotations': orders.sudo() if quotation_page else SaleOrder,
            'orders': orders.sudo() if not quotation_page else SaleOrder,
            'page_name': 'quote' if quotation_page else 'order',
            'pager': pager_values,
            'default_url': url,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })

        return values
