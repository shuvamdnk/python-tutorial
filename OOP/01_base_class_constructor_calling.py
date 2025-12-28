class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Chai.__init__(self, type_, strength) # Explicit call
        super().__init__(type_, strength) # super function
        self.spice_level = spice_level

ginger_tea = GingerChai('Ginger','high','high')

print(ginger_tea.type)
        
