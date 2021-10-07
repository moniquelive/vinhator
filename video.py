import datetime as dt
from abc import ABCMeta, abstractmethod

import cv2
import numpy as np

WINDOW_TITLE = "Vinhator"
WIDTH, HEIGHT = 1024, 768
FPS = 60

CLR = {
    'BLACK':  (0, 0, 0),
    'WHITE':  (255, 255, 255),
    'GREEN':  (0, 128, 0),
    'BLUE':   (204, 0, 0),
    'YELLOW': (0, 204, 204),
    'GOPHER': (0xe6, 0xff, 0x9a),
}


class Video(metaclass=ABCMeta):
    @abstractmethod
    def setup(self):
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        raise NotImplementedError()

    @abstractmethod
    def draw(self, canvas):
        raise NotImplementedError()

    # Template Method
    def generate(self, duration=None):
        # cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_OPENGL)
        canvas = np.full((HEIGHT, WIDTH, 3), CLR['WHITE'], dtype=np.uint8)

        now = dt.datetime.now()
        video = None
        if duration:
            video = cv2.VideoWriter('filename.mkv',
                                    cv2.VideoWriter_fourcc(*'X264'),
                                    FPS, (WIDTH, HEIGHT))

        self.setup()

        while True:
            self.draw(canvas)
            cv2.imshow(WINDOW_TITLE, canvas)

            if duration and dt.datetime.now() > duration + now:
                break
            if cv2.waitKey(1) & 255 == 27:
                break

            self.update()

            if video:
                video.write(canvas)

        if video:
            video.release()
