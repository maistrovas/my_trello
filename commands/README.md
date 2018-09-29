#BOARD INTERFACE
"""
print dir(wekkly_planning_board)
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
 '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'add_label', 'add_list', 
'add_member', 'admin_members', 'all_cards', 'all_lists', 'all_members', 
'client', 'close', 'closed', 'closed_cards', 'closed_lists', 
'date_last_activity', 'description', 'fetch', 'fetch_actions', 
'from_json', 'get_cards', 'get_checklists', 'get_labels', 'get_last_activity', 
'get_list', 'get_lists', 'get_members', 'id', 'list_lists', 'name', 
'normal_members', 'open', 'open_cards', 'open_lists', 'owner_members', 
'remove_member', 'save', 'set_description', 'set_name', 'url']
"""

#LIST INTERFACE
"""
weekly_planning_lists = wekkly_planning_board.all_lists() # List of List objects
print dir(weekly_planning_lists[0])
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', 
'__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', '_set_remote_attribute', 'add_card', 
'archive_all_cards', 'board', 'cardsCnt', 'client', 'close', 'closed', 'fetch', 
'fetch_actions', 'from_json', 'id', 'list_cards', 'move', 'move_all_cards', 
'name', 'open', 'pos', 'set_name', 'set_pos']
"""




#CARD INETERFACE
"""
print dir(thursday_cards[0])
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', 
'__getattribute__', '__hash__', '__init__', '__module__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', '_list_movements', '_movement_as_dict', 
'_movement_as_triplet', '_post_remote_data', '_set_due_complete', 
'_set_remote_attribute', 'add_checklist', 'add_label', 'add_member', 
'assign', 'attach', 'attachments', 'attriExp', 'board', 'board_id', 
'card_created_date', 'change_board', 'change_list', 'change_pos', 'checklists', 
'client', 'closed', 'comment', 'comments', 'create_label', 'created_date', 
'dateLastActivity', 'date_last_activity', 'delete', 'delete_comment', 'desc', 
'description', 'due', 'due_date', 'fetch', 'fetch_actions', 'fetch_attachments', 
'fetch_checklists', 'fetch_comments', 'fetch_plugin_data', 'from_json', 
'get_attachments', 'get_comments', 'get_list', 'get_stats_by_list', 'id', 
'idBoard', 'idLabels', 'idList', 'idMembers', 'idShort', 'is_due_complete', 
'label_ids', 'labels', 'latestCardMove_date', 'listCardMove_date', 'list_id', 
'list_labels', 'list_movements', 'member_id', 'member_ids', 'name', 'plugin_data', 
'pos', 'remove_attachment', 'remove_due', 'remove_due_complete', 'remove_label', 
'remove_member', 'set_closed', 'set_description', 'set_due', 'set_due_complete', 
'set_name', 'set_pos', 'shortUrl', 'short_id', 'short_url', 'subscribe', 'trello_list', 
'unassign', 'update_comment', 'url']
"""