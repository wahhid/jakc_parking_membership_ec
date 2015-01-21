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

class park_membership_payment(osv.osv_memory):
    _name = "park.membership.payment"
    _description = "Parking Membership Payment"

    def onchange_partner(self, cr, uid, ids, partner_id):
        membership_line_obj = self.pool.get('park.membership.line')        
        membership_line_ids = membership_line_obj.search(cr,uid, [('partner_id','=', partner_id)])
        return {'domain':{'membership_line_id':[('id','in',membership_line_ids)]}}
                    
    _columns = {
        'partner_id': fields.many2one('res.partner','Member'),
        'membership_line_id': fields.many2one('park.membership.line','Line'),
        'membership_duration': fields.integer('Duration (in month)'),
        'state': fields.selection(AVAILABLE_STATES,'Status', size=16, required=True, readonly=True),
    }
    
    _defaults = {
        'state': lambda *a: 'open',
    }

park_membership_payment()