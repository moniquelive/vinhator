import math
import time
from abc import ABC

import cv2
import numpy as np

from video import \
    CLR, \
    HEIGHT, \
    Video, \
    WIDTH


class QuicaQuica(Video, ABC):
    def __init__(self):
        super().__init__()
        self.vel_x = self.vel_y = self.x = self.y = self.radius = 0

    def setup(self):
        self.vel_x = self.vel_y = 5
        self.x = self.y = self.radius = 200

    def update(self):
        self.radius = int(math.fabs(200 * math.cos(time.time())))
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.vel_x *= -1
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.vel_y *= -1


class NihonFlag(QuicaQuica):
    def draw(self, canvas):
        cv2.rectangle(canvas, (0, 0), (WIDTH, HEIGHT), CLR['WHITE'], -1)
        cv2.circle(canvas, (self.x, self.y), self.radius, (0, 0, 255), -1)


class HueFlag(QuicaQuica):
    def draw(self, canvas):
        cv2.rectangle(canvas, (0, 0), (WIDTH, HEIGHT), CLR['GREEN'], -1)
        pts = np.array([[50, HEIGHT // 2], [WIDTH // 2, 50], [WIDTH - 50, HEIGHT // 2], [WIDTH // 2, HEIGHT - 50]],
                       np.int32)
        cv2.fillPoly(canvas, [pts], CLR['YELLOW'])
        cv2.circle(canvas, (self.x, self.y), self.radius, CLR['BLUE'], -1)


class Gopher(Video):
    def setup(self):
        pass

    def update(self):
        pass

    def draw(self, canvas):
        # face
        cv2.rectangle(canvas, (0, 0), (WIDTH, HEIGHT), CLR['GOPHER'], -1)
        # left eye
        self.eye(canvas, WIDTH // 4, 200, 180)
        # right eye
        self.eye(canvas, int(WIDTH * 0.75), 200, 200)

    @staticmethod
    def eye(canvas, x, y, radius):
        # fill
        cv2.circle(canvas, (x, y), radius, CLR['WHITE'], -1)
        # border
        cv2.circle(canvas, (x, y), radius, CLR['BLACK'], 4)

        # iris
        iris_x = int(x + radius * 0.6)
        cv2.circle(canvas, (iris_x, y), int(radius * 0.2), CLR['BLACK'], -1)
        # pupil
        pupil_radius = int(radius * 0.05)
        cv2.circle(canvas, (int(iris_x*1.02), int(y - pupil_radius * 0.9)), pupil_radius, CLR['WHITE'], -1)


if __name__ == '__main__':
    # NihonFlag().generate() #dt.timedelta(seconds=5))
    # HueFlag().generate()  # datetime.timedelta(seconds=5))
    Gopher().generate()  # datetime.timedelta(seconds=5))
    cv2.destroyAllWindows()
