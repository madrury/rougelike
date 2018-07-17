from etc.enum import ResultTypes, Elements
from etc.game_config import FREEZE_BASE_DAMAGE


class EnemyFreezable:

    def freeze(self, game_map):
        print(f"{self.owner.name} is frozen.")
        return [{
            ResultTypes.FREEZE: self.owner,
            ResultTypes.DAMAGE: (
                self.owner, None, FREEZE_BASE_DAMAGE, [Elements.ICE])
        }]
