import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
        self.initial = dict(kwargs)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents = []
            return drawn
        drawn = random.sample(self.contents, num_balls)
        new_contents = self.contents.copy()
        for ball in drawn:
            new_contents.remove(ball)
        self.contents = new_contents
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        new_hat = Hat(**hat.initial)
        drawn = new_hat.draw(num_balls_drawn)
        drawn_count = {}
        for color in drawn:
            drawn_count[color] = drawn_count.get(color, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break
        if success:
            successes += 1
    return successes / num_experiments