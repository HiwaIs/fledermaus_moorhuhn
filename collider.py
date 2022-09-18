import pygame as pg
vec = pg.Vector2

'''
    Collider Class
    The original C++ Code belongs to David Barr, aka javidx9, OneLoneCoder 
    Adapted to Python: Christian Krauss

    Resources for this code:
    https://www.gamedev.net/tutorials/programming/general-and-gameplay-programming/swept-aabb-collision-detection-and-response-r3084/
    https://github.com/OneLoneCoder/olcPixelGameEngine/blob/master/Videos/OneLoneCoder_PGE_Rectangles.cpp
    '''


class Collider:

    def __init__(self):
        pass

    '''
        Collision Point and Rect vs Rect
    '''

    def PointVsRect(self, point, rect):
        # Test if a point is colliding with a rect
        # returns True or False
        return point.x >= rect.x and point.y >= rect.y and point.x < rect.x + rect.width and point.y < rect.y + rect.height

    def RectVsRect(self, rect1, rect2):
        # Test if rect1 is colliding with rect2
        # returns True or False
        return rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y

 