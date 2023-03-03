planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string 
distance_to_alpha_centauri = 4.367 # looks like a float
type(distance_to_alpha_centauri) ## <class 'float'>
from datetime import date
date.today()
print(date.today())
print("Today's date is: " + str(date.today()))
moon_facts = ["The Moon is drifting away from the Earth," " On average, the Moon is moving about 4cm every year"]
c='\n'.join(moon_facts)
print(moon_facts,c)
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))