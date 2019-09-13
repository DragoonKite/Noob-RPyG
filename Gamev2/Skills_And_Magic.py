class Skill:
    def __init__ (self, name, description, mp_cost, damage_type, req_stat, min_stat):
        self.name = name
        self.description = description
        self.mp_cost = mp_cost
        self.damage_type = damage_type
        self.required_stat = req_stat
        self.minimum_stat = min_stat


soldier_tree = []

soldier_tree.insert(0, Skill("Lunge", "Attack enemy for 2x damage", 5, "Physical", "atk", 5))
soldier_tree.insert(1, Skill("Throw", "Throw weapon at enemy for 1.5x damage", 5, "Physical", "atk", 7))
soldier_tree.insert(2, Skill("Impale", "Attack enemy for 5x damage", 5, "Physical", "atk", 17))
