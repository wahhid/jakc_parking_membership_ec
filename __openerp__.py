{
    'name' : 'Parking Management System - Membership Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Parking Membership Module',
    'depends' : ['base_setup','base','jakc_parking',],
    'init_xml' : [],
    'data' : [			        
        'security/ir.model.access.csv',             
        'jakc_parking_membership_view.xml',
        'jakc_parking_membership_menu.xml',        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}