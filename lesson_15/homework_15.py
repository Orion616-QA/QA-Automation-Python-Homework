class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більшою за 0")
            object.__setattr__(self, key, value)

        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах (0, 180)")
            object.__setattr__(self, key, value)
            object.__setattr__(self, "angle_b", 180 - value)

        elif key == "angle_b":
            raise AttributeError("кут_б визначається автоматично від кута_а")

        else:
            object.__setattr__(self, key, value)

    def __repr__(self):
        return f"Ромб(сторона_a={self.side_a}, кут_a={self.angle_a}, кут_б={self.angle_b})"