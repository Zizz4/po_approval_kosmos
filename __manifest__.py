{
    'name': 'Purchase Order Approval Kosmos',
    'version': '16.0',
    'summary': 'Purchase Order Approval',
    'description': 'Purchase Order Approval for Kosmos',
    'category': 'Productivity',
    'author': 'Muhamad Syahril Aziz',
    'website': 'erp.kosmoswave.com',
    'license': 'LGPL-3',
    'depends': ['base','purchase'],
    'data': ['views/purchase_order_form_view.xml',
             'views/res_users_view.xml',
             'report/report_purchase_order.xml'],
    'installable': True,
    'auto_install': False
}
