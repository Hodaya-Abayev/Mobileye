from PIL import Image

"""
Saves image frame and the traffic light point
"""
class Frame:
    def __init__(self, img: Image, red_points: list, green_points: list):
        self.img=img
        self.red_points=red_points
        self.green_points=green_points

