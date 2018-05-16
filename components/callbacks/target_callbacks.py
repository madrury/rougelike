from entity import get_blocking_entity_at_location

class LanceCallback:

    def execute(self, game_map, entities, target, source):
        dx, dy = target.x - source.x, target.y - source.y
        targets = [target]
        if game_map.within_bounds(target.x + dx, target.y + dy):
            new_target = get_blocking_entity_at_location(
                entities, target.x + dx, target.y + dy)
            if new_target:
                targets.append(new_target)
        if game_map.within_bounds(target.x + 2*dx, target.y + 2*dy):
            new_target = get_blocking_entity_at_location(
                entities, target.x + 2*dx, target.y + 2*dy)
            if new_target:
                targets.append(new_target)
        return targets
