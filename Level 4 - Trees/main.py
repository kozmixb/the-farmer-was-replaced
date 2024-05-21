while True:
	buy_seeds()
	if num_items(Items.Water_Tank) > 1:
		use_item(Items.Water_Tank)
	if can_harvest():
		harvest()
	current = get_plant()
	do_plant(current)
	do_move()

def get_plant():
	if get_pos_y() % 3 == 0 and get_pos_x() % 2 == 0:
		return Entities.Tree
	if get_pos_y() % 3 == 1 and get_pos_x() % 2 == 0:
		return Entities.Carrots
	if get_pos_y() % 3 == 2 and get_pos_x() % 2 == 0:
		return Entities.Grass	
	if get_pos_y() % 3 == 0 and get_pos_x() % 2 == 1:
		return Entities.Grass
	if get_pos_y() % 3 == 1 and get_pos_x() % 2 == 1:
		return Entities.Bush
	if get_pos_y() % 3 == 2 and get_pos_x() % 2 == 1:
		return Entities.Carrots	
	
def do_plant(current):
	if current == Entities.Carrots and get_ground_type() == Grounds.Turf:
		till()
	elif current != Entities.Carrots and get_ground_type() == Grounds.Soil:
		till()
	plant(current)

def buy_seeds():
	if num_items(Items.Carrot_Seed) < 2:
		trade(Items.Carrot_Seed, 20)
	if num_items(Items.Empty_Tank) < 300:
		trade(Items.Empty_Tank)

def do_move():
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)