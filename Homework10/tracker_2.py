import os
import cv2
import natsort
#import pickle
#import numpy as np
from matplotlib import pyplot as plt

# Load the dataset
folder = '/home/iliyas/Desktop/pythonProject/pythonProject/frames'
frames = os.listdir(folder)
boxes = []

# Sort (alphabetically) to ensure temporal consecutiveness
#frames.sort()
frames = natsort.natsorted(frames)
print(frames)
idx = frames.index('34.jpg')

# Let's assume the detector has detected a vehicle
x1, y1 = 760, 340
x2, y2 = 840, 425

width = x2 - x1
height = y2 - y1

# Limit the search to a certain vicinity (since the cars can only move that fast)
search = 150

# Set up tracker
tracker_types = ['MIL', 'KCF', 'CSRT']
tracker_type = tracker_types[2]

if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()

if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()

if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

# Genrate tracking template
img = cv2.imread(os.path.join(folder, frames[idx]))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize tracker
bbox = (x1, y1, width, height)
ok = tracker.init(img, bbox)

# Tracking loop
for ii in range(idx+1, idx + 171):
    img = cv2.imread(os.path.join(folder, frames[ii]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    ok, bbox = tracker.update(img)
    print(ok, bbox)

    # Show the tracker working
    x1, y1 = bbox[0], bbox[1]
    width, height = bbox[2], bbox[3]
    cv2.rectangle(img, (x1, y1), (x1 + width, y1 + height), (0, 255, 0), 2)
    plt.imshow(img)
    plt.show(), plt.draw()
    plt.waitforbuttonpress(0.1)
    plt.clf()
