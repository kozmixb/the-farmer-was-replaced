plantables = [
	Entities.Pumpkin,
	Entities.Bush,
	Entities.Tree,
	Entities.Grass,
	Entities.Carrots,
]

while True:
	current = get_plant()
	do_harvest(current)
	do_plant(current)
	do_move()

def get_plant():
	for i in range(len(plantables)):
		if get_pos_y() % len(plantables) == i:
			current = plantables[i]
			if current == Entities.Bush:
				current = Entities.Pumpkin
			if current == Entities.Tree and get_pos_x() % 2 == 1:
				current = Entities.Grass
			return current
	
def do_plant(current):
	buy_seeds()
	if get_ground_type() == Grounds.Turf and current == Entities.Carrots:
		till()
	if get_ground_type() == Grounds.Turf and current == Entities.Pumpkin:
		till()
	if get_ground_type() == Grounds.Soil and current == Entities.Bush:
		till()
	if get_ground_type() == Grounds.Soil and current == Entities.Tree:
		till()
	if get_ground_type() == Grounds.Soil and current == Entities.Grass:
		till()
	if get_entity_type() != current:
		plant(current)
	if num_items(Items.Water_Tank) > 1:
		use_item(Items.Water_Tank)

def do_harvest(current):
	if can_harvest() and current == Entities.Pumpkin:
		if check_pumpkins():
			harvest()
		return
	if can_harvest():
		harvest()

def do_move():
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)