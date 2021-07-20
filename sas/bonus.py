
class BonusGuild:

    def __init__(self):
        self.space_academy = 0
        self.guild_passive = 0


class BonusChar:

    def __init__(self):
        self.virtue = 0
        self.orb_star = 0
        self.orb_level = 0
        self.orb_total = 0
        self.legendary = 0
        self.asc_dmg = 0
        self.asc_hp = 0
        self.trophy_hp = 0
        self.trophy_dmg = 0

    def loadSpinbox(self, spinbox):
        self.virtue = int(spinbox['virtue'])
        self.orb_star = int(spinbox['orb_star'])
        self.orb_level = int(spinbox['orb_level'])
        self.orb_total = (0.02*pow(self.orb_star, 2)+self.orb_level/100*(0.08*self.orb_star+0.04)*0.4)*(1+self.virtue*0.005)
        self.legendary = int(spinbox['legendary']) / 100
        self.asc_dmg = int(spinbox['asc_dmg']) / 50
        self.asc_hp = int(spinbox['asc_hp']) / 50
        self.trophy_hp = int(spinbox['trophy_hp']) / 100
        self.trophy_dmg = int(spinbox['trophy_dmg']) / 100
        return self
