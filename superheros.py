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
		self.current_health = starting_health
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
		try:
			for armor in self.armors:
				damage_amt -= armor.block()
		except:
			pass
		return damage_amt 

	def take_damage(self, damage):
		'''Updates self.current_health to reflect the damage minus the defense.
		'''
		self.current_health -= self.defend(damage)
  
	def is_alive(self):
		'''Return True or False depending on whether the hero is alive or not.
		'''

		if self.current_health >= 0:
			return True
		else:
			return False

	def fight(self, opponent):
		# loop while self and opponent are fighting
			# self takes damage, where damage = opponent.attack()
			# opponent takes damage, where damage = self.attack()
			# check if either of them died
				# if they did end the while loop
		# print ______ wins!
		while opponent.is_alive() and self.is_alive():
			damage = self.attack()
			opponent.take_damage(damage)
			damage = opponent.attack()
			self.take_damage(damage)
		if opponent.is_alive():
			print(f"{opponent.name} knocked {self.name} the fuck out")
		else:
			print(f"{self.name} knocked {opponent.name} the fuck out")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Coco Roco")
    hero2 = Hero("Kye")
    ability1 = Ability("Super Speed", 30)
    ability2 = Ability("Super Eyes", 60)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
