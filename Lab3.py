class Artifact:
    def __init__(self, name, price, mana):
        self.name = name
        self.price = price
        self.mana = mana

    def __repr__(self):
        return f"Artifact - {self.name}: Price: {self.price}, Mana: {self.mana}"


class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

    def __repr__(self):
        return f"Weapon - {self.name}: Price: {self.price}, Damage: {self.damage}"


class Character:
    def __init__(self, name, level, profession, race):
        self.name = name
        self.level = level
        self.profession = profession
        self.race = race
        self.artifacts = []  # список артефактів
        self.weapons = []    # список зброї

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def __repr__(self):
        artifacts_info = "\n".join(map(str, self.artifacts))
        weapons_info = "\n".join(map(str, self.weapons))
        return f"Character - {self.name}: Level: {self.level}, Profession: {self.profession}, Race: {self.race}\nArtifacts:\n{artifacts_info}\nWeapons:\n{weapons_info}"


# Приклад використання ієрархії класів:

character1 = Character("Warrior1", 5, "Warrior", "Human")
artifact1 = Artifact("Amulet", 50, 20)
artifact2 = Artifact("Ring", 30, 15)
weapon1 = Weapon("Sword", 100, 30)

character1.add_artifact(artifact1)
character1.add_artifact(artifact2)
character1.add_weapon(weapon1)

print(character1)
