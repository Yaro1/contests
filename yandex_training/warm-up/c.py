import sys
import math

def angle_of_line(x1, y1, x2, y2):
    return math.atan2(-(y2-y1), x2-x1)

def found_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def solution():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    alpha = math.atan2(y1, x1)
    beta = math.atan2(y2, x2)
    diff_angle = abs(beta - alpha)
    min_, max_ = min(found_distance([x1, y1], [0, 0]), found_distance([x2, y2], [0, 0])), max(found_distance([x1, y1], [0, 0]), found_distance([x2, y2], [0, 0]))
    way1 = min_ + max_
    way2 = min_ * diff_angle + (max_ - min_)
    print(min(way1, way2))
solution()