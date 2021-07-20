from .loader_base import LoaderBase, Singleton
from sas.bonus import BonusGuild


class LoaderShip(LoaderBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.bonus_guild = None
        self.getters = ['getBonusGuild']
        self._raw_lines = {
            'raw_academy': 23,
            'raw_guild': 24,
        }

    def getBonusGuild(self):
        text, raw_academy = self._getRawLine('raw_academy')
        text, raw_guild = self._getRawLine('raw_guild')
        self.bonus_guild = BonusGuild()
        self.bonus_guild.space_academy = float(raw_academy[:-2]) / 100
        self.bonus_guild.guild_passive = float(raw_guild[:-2]) / 100
        return self.bonus_guild


