# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document
from frappe.utils import money_in_words

class ValueUpdateTool(Document):
	pass
	
@frappe.whitelist(allow_guest=True)
def update_value(doctype = None, name = None, company = None):
	frappe.msgprint("Test")
	lcv = frappe.get_doc({
	"doctype": doctype, 
	"name": name,
	"company": company
	})
	lcv.insert(ignore_permissions=True)
	lcv.submit()

