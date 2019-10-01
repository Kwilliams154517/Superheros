import random
from random import shuffle

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
		self.deaths = 0
		self.kills = 0

	def add_kill(self, num_kills):
		self.kills += num_kills 

	def add_deaths(self, num_deaths):
		self.deaths += num_deaths

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
			opponent.add_kill(1)
			print(f"{opponent.name} knocked {self.name} the f*** out")
		else:
			self.add_deaths(1)
			print(f"{self.name} knocked {opponent.name} the f*** out")
		
	def add_weapon(self, weapon):
		weapon.append(self.abilities)
	
	def add_armors(self, armor):
		armor.append(self.armors)
		
		
class Weapon(Ability):
    def attack(self):
        return random.randint(2/self.attack_strength, self.attack_strength)
    
class Team():
	def __init__(self, name):
		self.name = name
		self.heros = []

	def remove_hero(self, hero):
		if hero in self.heros:
			self.heros.remove(hero)
		else:
			return 0

	def veiw_all_heroes(self):
		print("heros: " + ", ".join(self.heros))

	def add_hero(self, hero):
		self.heros.append(hero)

	def is_alive(self):
		for hero in self.heros:
			if hero.is_alive():
				return True
		return False

	def attack(self, other_team):
		""" Make teams fight """
		shuffle(self.heros)
		shuffle(other_team.heros)
		for other_hero in other_team.heros:
			for hero in self.heros:
				hero.fight(other_hero)
		if self.is_alive() and other_team.is_alive():
			print(f" {self.other_team.name} Tied!")

		elif self.is_alive():
			print(f" {self.name} Won!")

		elif other_team.is_alive():
			print("You lose :-) ")



	
	def revive_heros(self, health=100):
		""" reset all heros health back to its starting health """
		for hero in self.heros:
			try:
				hero.current_health = hero.starting_health
			except:
				hero.current_health = health
	def stats(self):
		for hero in self.heros:
			print(f"{hero.name} your stats are {hero.kills / hero.deaths} ") 

class Arena:
	def __init__(self):
		self.team_one = None
		self.team_two = None
		winning_team = None
		
	def create_ability(self):
		name = input("Enter ability name: ")
		attack_strength = input("Enter Attack Strength: ")
		return Ability(name, attack_strength)
		
	def create_weapon(self):
		name = input("Create weapon name: ")
		weapon = input("Create a Weapon: ")
		return Weapon(name, weapon)
		
	def create_armor(self):
		name = input("Create armor name maybe idk dude come back later: ? ")
		armor = input("Create Hero armor: ")
		return Armor(name, armor)
	

	def create_hero(self):
		name = input("Create a hero name: ")
		Hero = input("Create a starting health: ")
		return Hero(name, starting_health = 100)
	

	def build_team_one(self):
		name = input("Create the first team name: ")
		team_len = input("how many heros would you like in this team: ")
		self.team_one = Team(name)
		for i in range(int(team_len)):
			self.team_one.add_hero(self.create_hero())


	def build_team_two(self):
		name = input("Create the second team name: ")
		team_len = input("how many heros would you like in this team: ")
		self.team_two = Team(name)
		for i in range(int(team_len)):
			self.team_one.add_hero(self.create_hero())
		

	def team_battle(self):
		self.team_one.attack(team_two)

	def show_stats(self):
		print("The winners are: " + self.winning_team)
        
		self.team_one.stats()
		self.team_two.stats()

		if self.winning_team == self.team_one.name:
			for hero in self.team_one.heroes:
				if hero.status == "Alive":
					print("Surviving Heroes: " + hero.name)
		elif self.winning_team == self.team_two.name:
			for hero in self.team_two.heroes:
				if hero.status == "Alive":
           		 	print("Surviving Heroes: " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

	
		
		
	
