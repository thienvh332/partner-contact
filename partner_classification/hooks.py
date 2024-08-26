# Copyright 2024 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.upgrade import util

def pre_init_hook(env):

    required_modules = ["gts_partner_category"]
    if not env["ir.module.module"].search(
        [("name", "in", required_modules)]
    ):
        return

    # Rename table from 'partner_category' to 'partner_classification'
    util.rename_model(env.cr, "partner.category", "partner.classification")

    # Rename field `group_category_id` to `partner_classification_id` in res_partner
    if util.column_exists(env.cr, "res_partner", "group_category_id"):
        util.rename_field(env.cr, "res.partner", "group_category_id", "partner_classification_id")

def post_init_hook(env):
    if not env["ir.module.module"].search(
        [("name", "=", "gts_partner_category")]
    ):
        return
    util.remove_module(env.cr, "gts_partner_category")
