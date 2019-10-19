from big_ol_pile_of_manim_imports import *
import numpy as np
import itertools as it
from copy import deepcopy
import sys

from manimlib.constants import *

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon
from manimlib.once_useful_constructs.region import  region_from_polygon_vertices, region_from_line_boundary

SPRING_COLOR = WHITE
TRI_COLOR = LIGHT_GRAY
A_COLOR = GREEN_D
WHEEL_COLOR = GRAY
BLOCK_COLOR = BLUE
RADIUS = 0.75
SIDE = 1
HEIGHT_L = 1.5
HEIGHT_R = 2.2

POINTS = np.array([
	[-0.1, 1.5, 0],
	[0.1, 1.5, 0],
	[0, 0, 0],
	[-RADIUS+SIDE/2, -HEIGHT_L, 0],
	[-RADIUS+SIDE/2, -HEIGHT_L-SIDE, 0],
	[-RADIUS-SIDE/2, -HEIGHT_L-SIDE, 0],
	[-RADIUS-SIDE/2, -HEIGHT_L, 0],
	[RADIUS+SIDE/2, -HEIGHT_R, 0],
	[RADIUS+SIDE/2, -HEIGHT_R-SIDE, 0],
	[RADIUS-SIDE/2, -HEIGHT_R-SIDE, 0],
	[RADIUS-SIDE/2, -HEIGHT_R, 0],
])


class Physics(Scene):
	def construct(self):
		text = TextMobject("Physics")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		line = Line(1*RIGHT+1.5*UP, 1*LEFT+1.5*UP)
		circle = Circle(radius = RADIUS, color = WHEEL_COLOR, fill_color = WHEEL_COLOR, fill_opacity = 0.5)
		asdf = triangle()
		left = leftblock()
		right = rightblock()
		line_l = Line(RADIUS*LEFT, RADIUS*LEFT+HEIGHT_L*DOWN)
		line_r = Line(RADIUS*RIGHT, RADIUS*RIGHT+HEIGHT_R*DOWN)
		self.play(ShowCreation(line), ShowCreation(circle), run_time = 0.5)
		self.play(FadeIn(asdf), run_time = 0.75)
		self.play(
			ShowCreation(left), 
			ShowCreation(right), 
			ShowCreation(line_l),
			ShowCreation(line_r),
			run_time = 1.25
		)
		leftnew = left
		rightnew = right
		line_lnew = Line(RADIUS*LEFT, RADIUS*LEFT+HEIGHT_R*DOWN)
		line_rnew = Line(RADIUS*RIGHT, RADIUS*RIGHT+HEIGHT_L*DOWN)
		self.play(
			left.apply_function,
			lambda p: p + np.array([
				0,
				HEIGHT_L-HEIGHT_R,
				0
			]),
			right.apply_function,
			lambda p: p + np.array([
				0,
				HEIGHT_R-HEIGHT_L,
				0
			]),
			Transform(line_l, line_lnew),
			Transform(line_r, line_rnew),
			run_time = 1.5,
		)
		self.wait(1)
		otss = TextMobject("On The Spot STEM").scale(3)
		self.play(
			FadeOutAndShiftDown(line),
			FadeOutAndShiftDown(circle),
			FadeOutAndShiftDown(asdf),
			FadeOutAndShiftDown(left),
			FadeOutAndShiftDown(right),
			FadeOutAndShiftDown(line_l),
			FadeOutAndShiftDown(line_r),
			Transform(text, otss),
		)
		self.wait()


def triangle(**kwargs):
	return Polygon(*POINTS[[0, 1, 2]], color = TRI_COLOR, **kwargs, fill_color = TRI_COLOR, fill_opacity = 1)

def leftblock(**kwargs):
	return Polygon(*POINTS[[3, 4, 5, 6]], color = BLOCK_COLOR, **kwargs, fill_color = BLOCK_COLOR, fill_opacity = 0.8)

def rightblock(**kwargs):
	return Polygon(*POINTS[[10, 9, 8, 7]], color = BLOCK_COLOR, **kwargs, fill_color = BLOCK_COLOR, fill_opacity = 0.8)
