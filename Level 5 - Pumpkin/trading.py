def buy_seeds():
	if num_items(Items.Carrot_Seed) < 2:
		trade(Items.Carrot_Seed, 20)
	if num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < get_world_size() * 100:
		trade(Items.Empty_Tank)
	if num_items(Items.Pumpkin_Seed) < 2:
		trade(Items.Pumpkin_Seed, 20)
	if num_items(Items.Fertilizer) < 2:
		trade(Items.Fertilizer, 20)