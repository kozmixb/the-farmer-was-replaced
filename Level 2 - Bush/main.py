clear()
while True:
	if get_entity_type() == Entities.Grass and can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_entity_type() == Entities.Bush and can_harvest():
		harvest()
		plant(Entities.Grass)		

	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
