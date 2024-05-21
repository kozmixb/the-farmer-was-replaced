def check_pumpkins():
	is_pumpkin_ready = True
	if get_world_size() -1 == get_pos_y():
		return True	
	if get_pos_y() % 2 == 1:
		return False
	elif get_pos_x() % 2 == 1:
		for i in range(4):
			if get_entity_type() != Entities.Pumpkin or not can_harvest():
				is_pumpkin_ready = False
			if i == 0:
				move(North)
			elif i == 1:
				move(West)
			elif i == 2:
				move(South)
			else:
				move(East)
	else:
		for i in range(4):
			if get_entity_type() != Entities.Pumpkin or not can_harvest():
				is_pumpkin_ready = False
			if i == 0:
				move(North)
			elif i == 1:
				move(East)
			elif i == 2:
				move(South)
			else:
				move(West)
	return is_pumpkin_ready