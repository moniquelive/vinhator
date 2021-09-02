import datetime as dt

import cv2
import numpy as np

WINDOW_TITLE = "Vinhator"
WHITE_CLR = (255, 255, 255)
HEIGHT = 768
WIDTH = 1024
FPS = 60


def video_generator(duration=None):
    # cv2.namedWindow(window_title, cv2.WINDOW_OPENGL)
    canvas = np.full((HEIGHT, WIDTH, 3), WHITE_CLR, dtype=np.uint8)

    x = y = radius = 200
    vel_x = vel_y = 5
    now = dt.datetime.now()
    video = None
    if duration:
        video = cv2.VideoWriter('filename.mkv',
                                cv2.VideoWriter_fourcc(*'X264'),
                                FPS, (WIDTH, HEIGHT))

    while True:
        cv2.rectangle(canvas, (0, 0), (WIDTH, HEIGHT), WHITE_CLR, -1)
        cv2.circle(canvas, (x, y), radius, (0, 0, 255), -1)
        cv2.imshow(WINDOW_TITLE, canvas)
        if duration and dt.datetime.now() > duration + now:
            break
        if cv2.waitKey(1) & 255 == 27:
            break

        x += vel_x
        y += vel_y
        if x + radius >= WIDTH or x - radius <= 0:
            vel_x *= -1
        if y + radius >= HEIGHT or y - radius <= 0:
            vel_y *= -1

        if video:
            video.write(canvas)

    video.release()


if __name__ == '__main__':
    video_generator(dt.timedelta(seconds=5))
    cv2.destroyAllWindows()
