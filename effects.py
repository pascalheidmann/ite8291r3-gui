class Effect:
    def __init__(self, name, speed=True, color=True, direction=False, reactive=False):
        self.name = name
        self.reactive = reactive
        self.direction = direction
        self.color = color
        self.speed = speed


effects = dict(
    [(value.name, value) for value in [
            Effect("breathing"),
            Effect("wave", color=False, direction=True),
            Effect("random", reactive=True),
            Effect("rainbow", speed=False, color=False),
            Effect("ripple", reactive=False),
            Effect("marquee", color=False),
            Effect("raindrop"),
            Effect("aurora", reactive=True),
            Effect("fireworks", reactive=True),
        ]
     ]
)
