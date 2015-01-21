from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('done','Close'),
]

AVAILABLE_PAYMENT_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('paid','Paid'),
    ('done','Closed'),
]

class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"    
    _columns = {
        'is_parking_member': fields.boolean('Parking Member'),            
        'membership_detail_ids': fields.one2many('park.membership.line','partner_id','Memberships'),            
    }
        
res_partner()


class park_membership_line(osv.osv):
    _name = "park.membership.line"
    _description  = "Parking Membership Line"
    _columns  = {
        'partner_id': fields.many2one('res.partner','Member', required=True),
        'plat_number': fields.char('Plat Number', size=10),         
        'state': fields.selection(AVAILABLE_STATES,'Status', size=16, required=True, readonly=True),
    }    
    _sql_constraints = [
                     ('plat_number_unique', 
                      'unique(plat_number)',
                      'Plat Number already Used!')
    ]    
    _defaults = {        
        'state': lambda *a: 'open',
    }    
park_membership_line()

class park_membership_line_payment(osv.osv):
    _name = 'park.membership.line.payment'
    _description = "Parking Membership Line Payment"
    
    def get_trans(self, cr, uid, trans_id, context=None):
        return self.browse(cr, uid, trans_id, context=context)
    
    def get_last_trans(self, cr, uid, context=None):
        pass
    
    _columns = {
        'membership_line_id': fields.many2one('park.membership.line', 'Line', required=True),
        'trans_date': fields.date('Transaction Date'),
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),
        'state': fields.selection(AVAILABLE_PAYMENT_STATES,'Status', size=16, required=True),
    }

park_membership_line_payment()
