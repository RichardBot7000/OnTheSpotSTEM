from big_ol_pile_of_manim_imports import *
import numpy as np
import itertools as it
from copy import deepcopy
import sys

from manimlib.constants import *

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon
from manimlib.once_useful_constructs.region import  region_from_polygon_vertices, region_from_line_boundary

A_COLOR = GREEN_D
B_COLOR = BLUE
C_COLOR = RED_D
TRI_COLOR = PURPLE_A

#moved everything DOWN
POINTS = np.array([
    [0, -2, 0],
    [0, 1, 0],
    [1, -2, 0],
    [0, -3, 0],
    [1, -3, 0],
    [-3, -2, 0],
    [-3, 1, 0],
    [4, -1, 0],
    [3, 2, 0],
])

class Math(Scene):
	def construct(self):
		text = TextMobject("Math")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		tri = Triangle()
		self.play(ShowCreation(tri), run_time = 1)
		a = a_square()
		b = b_square()
		c = c_square()
		self.play(
			ShowCreation(a),
			ShowCreation(b),
			ShowCreation(c),
			run_time = 3,
		)
		self.wait(1)
		otss = TextMobject("On The Spot STEM").scale(3)
		self.play(
			FadeOutAndShiftDown(a),
			FadeOutAndShiftDown(b),
			FadeOutAndShiftDown(c),
			FadeOutAndShiftDown(tri),
			Transform(text, otss)
		)
		self.wait()


class Triangle(Polygon):
    def __init__(self, **kwargs):
        kwargs["color"] = TRI_COLOR
        Polygon.__init__(
            self, 
            *POINTS[[1, 0, 2]],
            edge_colors = [B_COLOR, C_COLOR, A_COLOR],
            fill_color = TRI_COLOR,
            fill_opacity = 0.5,
            **kwargs
        )
        #nudge = 0.2
        #target = POINTS[0]+nudge*(UP+RIGHT)
        #for direction in UP, RIGHT:
            #self.add_line(POINTS[0]+nudge*direction, target, color = WHITE)


def a_square(**kwargs):
    return Polygon(*POINTS[[0, 2, 4, 3]], color = A_COLOR, **kwargs, fill_color = A_COLOR, fill_opacity = 0.5)

def b_square(**kwargs):
    return Polygon(*POINTS[[1, 0, 5, 6]], color = B_COLOR, **kwargs, fill_color = B_COLOR, fill_opacity = 0.5)

def c_square(**kwargs):
    return Polygon(*POINTS[[2, 1, 8, 7]], color = C_COLOR, **kwargs, fill_color = C_COLOR, fill_opacity = 0.5)
