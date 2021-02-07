'''
ECE 172A, Homework 1 BONGO
Author: regreer@ucsd.edu
For use by UCSD ECE 172A students only.
'''

import numpy as np
import matplotlib.pyplot as plt
import random
from skimage import draw

def generate_one_shape(numSides, orientation):
    xCenter = random.randint(200,300)
    yCenter = random.randint(200,300)
    theta = np.linspace(0, 2*np.pi, numSides + 1)
    theta = theta - np.pi/orientation;
    radius = random.randint(40,150)
    x = radius * np.cos(theta) + xCenter;
    y = radius * np.sin(theta) + yCenter;
    binaryImage = poly2mask(x, y, (500, 500))
    return binaryImage

def poly2mask(vertex_row_coords, vertex_col_coords, shape):
    fill_row_coords, fill_col_coords = draw.polygon(vertex_row_coords, vertex_col_coords, shape)
    mask = np.zeros(shape, dtype=np.bool)
    mask[fill_row_coords, fill_col_coords] = True
    return mask

def generator1():
    empty = np.zeros((500,500))
    label = random.randint(0, 1)
    shape = random.randint(3, 4)
    orientation = random.randint(1, 6)
    test_img = generate_one_shape(shape, orientation)
    if label == 0:
        orientation = random.randint(1, 6)
        A = generate_one_shape(shape, orientation)
        B = empty
    else:
        A = empty
        orientation = random.randint(1, 6)
        B = generate_one_shape(shape, orientation)
    return A,B, test_img, label

def generator2():
    label = random.randint(0, 1)
    shape = random.randint(3, 4)
    orientation = random.randint(1, 10)
    test_img = generate_one_shape(shape, orientation)
    orientation = random.randint(1, 10)
    if label == 0:
        A = test_img
        B = generate_one_shape(7-shape, orientation)
    else:
        A = generate_one_shape(7-shape, orientation)
        B = test_img
    return A,B, test_img, label

def generator3():
    label = random.randint(0, 1)
    orientation = random.randint(1, 10)
    test_img = generate_one_shape(3, orientation)
    orientation = random.randint(1, 10)
    if label == 0:
        A = generate_one_shape(3, orientation)
        B = generate_one_shape(4, orientation)
    else:
        A = generate_one_shape(4, orientation)
        B = generate_one_shape(3, orientation)
    return A,B, test_img, label

def generator4():
    label = random.randint(0, 1)
    shape = random.randint(3, 6)
    if label == 0:
        orientation = random.randint(1, 10)
        test_img = generate_one_shape(shape, orientation)
        orientation = random.randint(1, 10)
        A = generate_one_shape(shape, orientation)
        orientation = random.randint(1, 10)
        B = generate_one_shape(9-shape, orientation)
    else:
        orientation = random.randint(1, 10)
        test_img = generate_one_shape(shape, orientation)
        orientation = random.randint(1, 10)
        A = generate_one_shape(9-shape, orientation)
        orientation = random.randint(1, 10)
        B = generate_one_shape(shape, orientation)
    return A,B, test_img, label

def visualize(question,count):
    for i in range(count):
        if question == 1:
            A,B,test_img,label = generator1()
        elif question == 2:
            [A,B,test_img,label] = generator2();
        elif question == 3:
            [A,B,test_img,label] = generator3();
        else: 
            [A,B,test_img,label] = generator4();
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.imshow(A, cmap='gray')
        ax1.set_title('Block 0')
        ax2.imshow(B, cmap='gray')
        ax2.set_title('Block 1')
        ax3.imshow(test_img, cmap='gray')
        ax3.set_title('Test Image, label = %d' %label)
        fig.suptitle("BONGO Puzzle Type %d"%question)
        plt.show()

puzzle = input("Which BONGO puzzle would you like to observe? [Enter a number 1-4]. ")
count = input("How many examples of BONGO puzzle %d would you like to see? " % int(puzzle))
visualize(int(puzzle), int(count))