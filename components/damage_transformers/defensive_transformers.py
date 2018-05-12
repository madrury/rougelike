class ElementalTransformer:
    """Reduce damage of a certain element by some amount.

    Attributes
    ----------
    strength: int
      The amount to reduce damage.

    element: Element
      The element whose damage to reduce.
    """
    def __init__(self, strength, element):
        self.strength = strength
        self.element = element

    def transform_damage(self, amount, element):
        if element == self.element:
            return max(0, amount - self.strength)
        return amount

