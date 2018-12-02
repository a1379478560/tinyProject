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
        # modify the following code
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []

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
                self._thirst=self.get_thirst_level()-liquid.get_quantity()   #########
                if self.get_thirst_level()<0:
                    self._thirst=0
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
                self._hunger=self.get_hunger_level()-food.get_quantity()   #########
                if self.get_hunger_level()<0:
                    self._hunger=0
                self._reply_to_master("feed")
        else:
            print("Not edible")
            print(type(food))
            print(self._edible_items)
        self._update_status()

    def shower(self):
        # Pet shower.
        self._time_pass_by(4)
        self._smell=0
        self._loneliness=self._loneliness-4 ########
        if self._loneliness<=0:
            self._loneliness=0
        self._reply_to_master("shower")
        self._update_status()

    def sleep(self):
        # Pet sleep.
        self._time_pass_by(7)
        self._energy=self.get_energy_level()+7  #######
        if self.get_energy_level()>10:
            self._energy=10
        self._reply_to_master("sleep")
        self._update_status()

    def play_with(self):
        # Play with Pet.
        self._time_pass_by(4)
        self._energy=self.get_energy_level()-4   #######
        self._loneliness=self._loneliness-4
        self._smell=self._smell+4
        if self._smell>10:
            self._smell=10
        if self._loneliness<0:
            self._loneliness=0
        if self.get_energy_level()<0:
            self._energy=0
        self._reply_to_master("play")
        self._update_status()

    def _reply_to_master(self, event='newborn'):
        # Print some hint.
        # this function is complete #
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
        # partially formatted string for your guidance
        #s = "{:<12s}: [{:<20s}]".format() + "{:5.2f}/{:2d}".format()
        print("{:<12s}: [{:<20s}]".format("Energy","#"*round(self.get_energy_level())*2)  ########
              + "{:5.2f}/{:2d}".format(self.get_energy_level(),10))
        print("{:<12s}: [{:<20s}]".format("Hunger","#"*round(self.get_hunger_level())*2)
              + "{:5.2f}/{:2d}".format(self.get_hunger_level(),10))
        print("{:<12s}: [{:<20s}]".format("Loneliness","#"*round(self._loneliness)*2)
              + "{:5.2f}/{:2d}".format(self._loneliness,10))
        print("{:<12s}: [{:<20s}]".format("Smell","#"*round(self._smell)*2)
              + "{:5.2f}/{:2d}".format(self._smell,10))
        print("{:<12s}: [{:<20s}]".format("Thirst","#"*round(self._thirst)*2)
              + "{:5.2f}/{:2d}".format(self._thirst,10))

    def _update_status(self):
        # Updata pet's status.
        # this function is complete #
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
        Pet.__init__(self,species="cat",name=name,gender=gender,color=color)
        self._edible_items=cat_edible_items
        self._drinkable_items=cat_drinkable_items

class Dog(Pet):
    #Dog class inherits from Pet.
    def __init__(self,name='fluffy', gender='male', color='white'):
        Pet.__init__(self,species="dog",name=name,gender=gender,color=color)
        self._edible_items=dog_edible_items
        self._drinkable_items=dog_drinkable_items


def main():
    #Main function.
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "

    # error checking for user input
    while True:
        pet = input(prompt)        #########
        if pet=="":         ###########
            pet="dog fluffy male white"
        pet=pet.strip()
        pet=pet.split()
        if len(pet)!=4:
            continue
        if (pet[0] in ("dog","cat")) and (pet[2] in ("male","female")):
            break

    # create a pet object
    if pet[0]=="dog":          ########
        pet_instance=Dog(name=pet[1],gender=pet[2],color=pet[3])
    if pet[0]=="cat":
        pet_instance=Cat(name=pet[1],gender=pet[2],color=pet[3])

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
    while True:
        command=input(prompt)
        command=command.strip() #######可以删掉，包括上一个strip
        if command=="feed":
            while True:
                food_account = input("How much food ? 1 - 10 scale:")
                if not food_account.isdigit():
                    print("Invalid input.")
                    continue
                if int(food_account)>10 or int(food_account)<1:
                    print("Invalid input.")
                    continue
                if pet_instance._species=="Dog":
                    edible=DogFood(int(food_account))
                else:
                    edible=CatFood(int(food_account))
                break
            pet_instance.feed(edible)
        elif command=="play":
            pet_instance.play_with()
        elif command=="drink":
            while True:
                food_account = input("How much drink ? 1 - 10 scale:")
                if not food_account.isdigit():
                    print("Invalid input.")
                    continue
                if int(food_account)>10 or int(food_account)<1:
                    print("Invalid input.")
                    continue
                edible=Water(int(food_account))
                break
            pet_instance.drink(edible)
        elif command=="shower":
            pet_instance.shower()
        elif command=="sleep":
            pet_instance.sleep()
        elif command=="status":
            pet_instance.show_status()
        elif command=="q":
            break
        else:
            print("Invalid command.")

    print("Bye ~")


if __name__ == "__main__":
    main()