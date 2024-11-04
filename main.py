import json
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, species, sound):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__sound = sound

    '''Name'''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    '''Age'''

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    '''species'''

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @species.deleter
    def species(self):
        del self.__species

    '''sound'''

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, sound):
        self.__sound = sound

    @sound.deleter
    def sound(self):
        del self.__sound

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, species, sound, breed):
        super(Dog, self).__init__(name, age, species, sound)
        self.breed = breed

    def make_sound(self):
        return f"Dog: It {self.sound} shunaqa ovoz"

    def get_info(self):
        return f"ismi:{self.name}\n Yoshi:{self}\n Turi:{self.species}\n Ovozi:{self.sound}\n Zoti:{self.breed}"

    def save_json(self):
        all_data = {
            "Ismi": self.name,
            "Yoshi": self.age,
            "Turi": self.species,
            "Ovoz": self.sound,
            "Zoti": self.breed,
        }
        with open("dog_data.json", mode="w", encoding='utf-8') as file:
            json.dump(all_data, file, indent=4)
            return f"Ma'lumotlaringiz {file.name} fayliga muvaffaqiyatli saqlandi!"


class Cat(Animal):
    def __init__(self, name, age, species, sound, gender):
        super(Cat, self).__init__(name, age, species, sound)
        self.gender = gender

    def make_sound(self):
        return f"Cat: Mushuk {self.sound} ovoz chiqaradi"

    def get_info(self):
        return f"ismi:{self.name}\n Yoshi:{self}\n Turi:{self.species}\n Ovozi:{self.sound}\n genderi:{self.gender}"

    def save_json(self):
        all_data = {
            "Ismi": self.name,
            "Yoshi": self.age,
            "Turi": self.species,
            "Ovoz": self.sound,
            "Genderi": self.gender,
        }
        with open("cat_data.json", mode="w", encoding='utf-8') as file:
            json.dump(all_data, file, indent=4)
            return f"Ma'lumotlaringiz {file.name} fayliga muvaffaqiyatli saqlandi!"


dog = Dog("Rokki", 15, "uy hayvoni", "Vov-Vov", "Alabama")
cat = Cat("kitty", 5, "uy hayvoni", "Meow-Meow", "Erkak")

print(cat.save_json())
print(dog.save_json())
