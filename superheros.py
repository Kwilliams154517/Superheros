import random

class Ability:
	def __init__(self, name, attack_strength):
		'''Create Instance Variables:
		name:String
		max_damage: Integer
		'''
		self.name = name
		self.attack_strength = attack_strength

	def attack(self):
		''' Return a value between 0 and the value set by self.max_damage.'''
		return random.randint(0, self.attack_strength)
class Armor:
	def __init__(self, name, max_block):
		'''Instantiate instance properties.
			name: String
			max_block: Integer
		'''
		self.name = name
		self.max_block = max_block

	def block(self):
		return random.randint(0, self.max_block)

class Hero:
	def __init__(self, name, starting_health=100):
		'''Instance properties:
			abilities: List
			armors: List
			name: String
			starting_health: Integer
			current_health: Integer
		'''
		self.name = name
		self.starting_health = starting_health
		self.abilities = []
		self.armors = []

	def add_ability(self, ability):
		''' Add ability to abilities list '''
		self.abilities.append(ability)

	def attack(self):
		'''Calculate the total damage from all ability attacks.
			return: total:Int
		'''
		total = 0
		for ability in self.abilities:
			total += ability.attack()
		return total
	def add_armor(self, armor):
		'''Add armor to self.armors
		Armor: Armor Object
		'''
		self.armors.append(armor)

	def defend(self, damage_amt):
		'''Runs `block` method on each armor.
		Returns sum of all blocks
		'''
# TODO: This method should run the block method on each armor in self.armors
		sum = 0 
		for damage_amt in self.armors:
			sum += damage_amt
		return sum 


