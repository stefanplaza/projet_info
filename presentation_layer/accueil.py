print("Quelle est votre adresse ?")
x = input()
print("Quelles sont les services que vous désirez ?")
y = input()
print("Quel est le type de caarburant souhaité ?")
z = input()

from abc import ABC, abstractmethod

class AbstractView(ABC):
    def display_info(self):
        return None

    @abstractmethod
    def make_choice(self):
        pass

class Connexion_View(AbstractView):
    