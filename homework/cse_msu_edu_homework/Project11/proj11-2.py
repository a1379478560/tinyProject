###########################################################
#  Programming Project 11
#   class:
#    this program contains seven class,Pet,Dog,Cat,
#       Drinkable,Water,Milk,Chocolate,CatFood, DogFood
#       Food.
#    Dog and Cat inherits from Pet,Water and Milk inherits
#       from Drinkable,Chocolate,CatFood and DogFood inherit
#       from Food.
#    function:
#    loop until user input a valid pet feature.
#    then promp user to input command
#    loop until user input a string euqal to "q".
###########################################################

from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]


class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male', color='white'):
        # Initial a pet with name,species,gender and color.
        name=name.capitalize()
        species=species.capitalize()
        gender=gender.capitalize()
        color=color.capitalize()
        self._name = name
        self._species = species
        self._gender = gender
        self._color = color
        self._edible_items = list()
        self._drinkable_items = list()
        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)
        self._reply_to_master('newborn')


    def _time_pass_by(self, t=1):
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        # Get hunger level.
        return self._hunger

    def get_thirst_level(self):
        # Get thirst level.
        return self._thirst

    def get_energy_level(self):
        #Get energy level.
        return self._energy

    def drink(self, liquid):
        # Pet drink given liquid.
        self._time_pass_by()
        if isinstance(liquid, tuple(self._drinkable_items)):
            if self.get_thirst_level()<2:
                print("Your pet is satisfied, no desire for sustenance now.")
            else:
                if liquid.get_quantity() >self.get_thirst_level():
                    self._thirst=0
                else:
                    self._thirst=self.get_thirst_level()-liquid.get_quantity()

                self._reply_to_master("drink")
        else:
            print("Not drinkable")
        self._update_status()

    def feed(self, food):
        # Pet feed given food.
        self._time_pass_by()
        if isinstance(food, tuple(self._edible_items)):
            if self.get_hunger_level()<2:
                print("Your pet is satisfied, no desire for sustenance now.")
            else:
                if self.get_hunger_level()<food.get_quantity():
                    self._hunger=0
                else:
                    self._hunger=self.get_hunger_level()-food.get_quantity()
                self._reply_to_master("feed")
        else:
            print("Not edible")
        self._update_status()

    def shower(self):
        # Pet shower.
        self._time_pass_by(4)
        self._smell=0
        if self._loneliness<4:
            self._loneliness=0
        else:
            self._loneliness=self._loneliness-4
        self._reply_to_master("shower")
        self._update_status()

    def sleep(self):
        # Pet sleep.
        self._time_pass_by(7)
        if self._energy+7>10:
            self._energy=10
        else:
            self._energy=self.get_energy_level()+7
        self._reply_to_master("sleep")
        self._update_status()

    def play_with(self):
        # Play with Pet.
        self._time_pass_by(4)
        self._energy=self.get_energy_level()-4
        if self.get_energy_level()<0:
            self._energy=0
        self._loneliness=self._loneliness-4
        if self._loneliness<0:
            self._loneliness=0
        self._smell=self._smell+4
        if self._smell>10:
            self._smell=10
        self._reply_to_master("play")
        self._update_status()

    def _reply_to_master(self, event='newborn'):
        # Print some hint.
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event]) + ": " + talks[event]
        print(s)

    def show_status(self):
        # Show pet's status in a given format.
        #s = "{:<12s}: [{:<20s}]".format() + "{:5.2f}/{:2d}".format()
        print("{:<12s}: [{:<20s}]".format("Energy","#"*
                round(self.get_energy_level())*2) + "{:5.2f}/{:2d}".format(self.get_energy_level(),10))
        print("{:<12s}: [{:<20s}]".format("Hunger","#"*
                round(self.get_hunger_level())*2)+ "{:5.2f}/{:2d}".format(self.get_hunger_level(),10))
        print("{:<12s}: [{:<20s}]".format("Loneliness","#"*
                round(self._loneliness)*2)+ "{:5.2f}/{:2d}".format(self._loneliness,10))
        print("{:<12s}: [{:<20s}]".format("Smell","#"*
                round(self._smell)*2)+ "{:5.2f}/{:2d}".format(self._smell,10))
        print("{:<12s}: [{:<20s}]".format("Thirst","#"*
                round(self._thirst)*2)+ "{:5.2f}/{:2d}".format(self._thirst,10))

    def _update_status(self):
        # Updata pet's status.
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'


class Cat(Pet):
    # Cat class inherits from Pet.
    def __init__(self,name='fluffy', gender='male', color='white'):
        Pet.__init__(self,name=name,gender=gender,color=color,species="cat")
        self._drinkable_items=cat_drinkable_items
        self._edible_items=cat_edible_items

class Dog(Pet):
    #Dog class inherits from Pet.
    def __init__(self,name='fluffy', gender='male', color='white'):
        Pet.__init__(self,species="dog",gender=gender,color=color,name=name)
        self._drinkable_items=dog_drinkable_items
        self._edible_items=dog_edible_items


def main():
    #Main function.
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
    pet_feature_str_default="dog fluffy male white"
    # error checking for user input
    while 1:
        pet_feature_str = input(prompt)
        if pet_feature_str=="":
            pet_feature_str=pet_feature_str_default
        pet_feature_str=pet_feature_str.strip()
        pet_feature_str=pet_feature_str.split()
        if len(pet_feature_str)!=4:
            continue
        if (pet_feature_str[0] =="dog" or pet_feature_str[0]=="cat") and (pet_feature_str[2]=="male" or pet_feature_str[2]=="female" ):
            break

    # create a pet object
    if pet_feature_str[0]=="dog":
        mypet_Pet=Dog(name=pet_feature_str[1],color=pet_feature_str[3],gender=pet_feature_str[2])
    if pet_feature_str[0]=="cat":
        mypet_Pet=Cat(name=pet_feature_str[1],color=pet_feature_str[3],gender=pet_feature_str[2])

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
    while 1:
        cmd_str=input(prompt)
        if cmd_str=='feed':
            while True:
                food_quantity_int = input("How much food ? 1 - 10 scale: ")
                if not food_quantity_int.isdigit():
                    print("Invalid input.")
                    continue
                if int(food_quantity_int)>10 or int(food_quantity_int)<1:
                    print("Invalid input.")
                    continue
                if mypet_Pet._species=="Dog":
                    food_edible=DogFood(int(food_quantity_int))
                else:
                    food_edible=CatFood(int(food_quantity_int))
                break
            mypet_Pet.feed(food_edible)
        elif cmd_str=='drink':
            while True:
                food_quantity_int = input("How much drink ? 1 - 10 scale: ")
                if not food_quantity_int.isdigit():
                    print("Invalid input.")
                    continue
                if int(food_quantity_int)>10 or int(food_quantity_int)<1:
                    print("Invalid input.")
                    continue
                food_edible=Water(int(food_quantity_int))
                break
            mypet_Pet.drink(food_edible)
        elif cmd_str=='shower':
            mypet_Pet.shower()
        elif cmd_str=='play':
            mypet_Pet.play_with()
        elif cmd_str=='status':
            mypet_Pet.show_status()
        elif cmd_str=='sleep':
            mypet_Pet.sleep()
        elif cmd_str=='q':
            break
        else:
            print("Invalid command.")

    print("Bye ~")


if __name__ == "__main__":
    main()