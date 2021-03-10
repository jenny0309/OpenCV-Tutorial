import numpy as np
import cv2


cap = cv2.VideoCapture(0)  # indicate which webcam to be used

while True:
    ret, frame = cap.read()  # ret: tell you whether the capture actually works properly // frame: image itself as a numpy array
    width = int(cap.get(3))
    height = int(cap.get(4))

    # divide the webcam screen into 4 parts
    # be careful on the shape when rotating the image!
    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0, 0), fx=.5, fy=.5)
    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # top left
    # image[height//2:, :width//2] = smaller_frame  # bottom left
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # top right
    # image[height//2:, width//2:] = smaller_frame  # bottom right

    # drawing line
    # cv2.line(SOURCE IMAGE, STARTING POSITION, ENDING POSITION, COLOUR, LINE THICKNESS)
    # the origin(0, 0) is put on top left
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)  # top left to bottom right
    img = cv2.line(img, (width, 0), (0, height), (0, 255, 0), 10)  # top right to bottom left
    # cv2.rectangle(SOURCE IMAGE, CENTER POSITION, RADIUS, COLOUR, LINE THICKNESS(-1 TO FILL))
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_ITALIC
    # cv2.putText(SOURCE IMAGE, TEXT, CENTER POSITION, FONT, FONT SCALE, COLOUR, LINE THICKNESS, LINE TYPE)
    img = cv2.putText(img, 'Cavin is Great!', (200, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
