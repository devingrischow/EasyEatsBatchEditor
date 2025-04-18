#usrInput = input("Enter a numeric Value!")

import cv2

availBackends = [cv2.videoio_registry.getBackendName(i) for i in cv2.videoio_registry.getBackends()]

print(availBackends)