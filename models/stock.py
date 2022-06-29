# -*- encoding: utf-8 -*-
# Coded by German Ponce Dominguez 
#     ▬▬▬▬▬.◙.▬▬▬▬▬  
#       ▂▄▄▓▄▄▂  
#    ◢◤█▀▀████▄▄▄▄▄▄ ◢◤  
#    █▄ █ █▄ ███▀▀▀▀▀▀▀ ╬  
#    ◥ █████ ◤  
#     ══╩══╩═  
#       ╬═╬  
#       ╬═╬ Dream big and start with something small!!!  
#       ╬═╬  
#       ╬═╬ You can do it!  
#       ╬═╬   Let's go...
#    ☻/ ╬═╬   
#   /▌  ╬═╬   
#   / \
# Cherman Seingalt - german.ponce@outlook.com

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import re

class StockPicking(models.Model):
    _inherit ='stock.picking'

    def get_stock_move_lines_info_sorted(self, move_line_ids_without_package):
        list_locations_names_srted = []
        dict_locations_names_srted = {}
        dict_locations_names_moves_final = {}
        list_sorted = []
        #.with_context({'lang':'es'})
        for mv_line in move_line_ids_without_package:
            mv_line = mv_line.with_context({'lang':'es'})
            complete_name = mv_line.location_id.complete_name
            if not complete_name in list_locations_names_srted:
                list_locations_names_srted.append(complete_name)
                dict_locations_names_srted[complete_name] = mv_line.location_id.id
                dict_locations_names_moves_final[mv_line.location_id.id] = []
        # move_line_ids_without_package.sorted(key=lambda ml: ml.location_id.id)
        list_locations_names_srted = list(sorted(list_locations_names_srted))
        for location_sortd_name in list_locations_names_srted:
            location_sortd_id = dict_locations_names_srted[location_sortd_name]
            for mv_line in move_line_ids_without_package:
                mv_location_id = mv_line.location_id.id
                if location_sortd_id == mv_location_id:
                    prev_list = dict_locations_names_moves_final[mv_location_id]
                    prev_list.append(mv_line)

        list_sorted = []
        for location_sortd_name in list_locations_names_srted:
            location_sortd_id = dict_locations_names_srted[location_sortd_name]
            list_for_location = dict_locations_names_moves_final[location_sortd_id]
            list_sorted = list_sorted + list_for_location
        return list_sorted