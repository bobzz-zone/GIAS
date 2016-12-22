# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ros@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TTDocument(Document):
	
        def validate(self):
                pass
        def on_submit(self):
                self.update_si()

        def update_si(self):
                table = self.outstanding_invoices or []
                for item in table:
                        voucher_no = item.against_voucher_no
                        name = self.name
                        #frappe.msgprint(_("name = {0}").format(name))
                        if voucher_no:
                                frappe.db.sql(""" UPDATE `tabSales Invoice` SET tt_reference_number=%(number)s
                                                        WHERE name=%(tt_name)s""" , {"number":name, "tt_name":voucher_no})
