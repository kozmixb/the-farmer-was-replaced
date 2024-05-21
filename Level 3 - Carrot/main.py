#clear()
while True:
	current = get_entity_type()
	if can_harvest():
		harvest()
	
	if current == Entities.Grass:
		plant(Entities.Bush)
	elif current == Entities.Bush:
		if get_ground_type() == Grounds.Turf:
			till()
		if num_items(Items.Carrot_Seed) == 0:
			trade(Items.Carrot_Seed)
		plant(Entities.Carrots)
	else:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Grass)

	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
