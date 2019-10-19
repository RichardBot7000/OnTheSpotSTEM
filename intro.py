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

A_COLOR = GREEN_D
B_COLOR = BLUE
C_COLOR = RED_D
TRIANGLE_COLOR = PURPLE_A

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

POINTS2 = np.array([
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

class Intro(Scene):
	def construct(self):
		self.wait(3)
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
		self.play(
			FadeOutAndShiftDown(line),
			FadeOutAndShiftDown(circle),
			FadeOutAndShiftDown(asdf),
			FadeOutAndShiftDown(left),
			FadeOutAndShiftDown(right),
			FadeOutAndShiftDown(line_l),
			FadeOutAndShiftDown(line_r),
			FadeOutAndShiftDown(text),
		)
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
		self.play(
			FadeOutAndShiftDown(a),
			FadeOutAndShiftDown(b),
			FadeOutAndShiftDown(c),
			FadeOutAndShiftDown(tri),
			FadeOutAndShiftDown(text),
		)
		text = TextMobject("Computer Science")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text),run_time = 1)
		circle = []
		for x in range(15):
			circle.append(Circle(color = WHITE, radius = 0.25, fill_color = WHITE, fill_opacity = 0))
		circle[0].shift([0,1,0])
		for x in range(2):
			circle[1+x].shift([-2+4*x,0,0])
		for x in range(4):
			circle[3+x].shift([-3+2*x,-1,0]),
		for x in range(8):
			circle[7+x].shift([-3.5+x,-2,0]),
		for c in circle:
			self.play(GrowFromCenter(c), run_time = 0.2)  
		line = [] 
		for x in range(2):
			line.append(Line([-0.3+0.6*x,0.85,0],[-1.7+3.4*x,0.15,0]))
		for x in range(4):
			line.append(Line([-2.2+0.4*(x%2)+4*(x//2),-0.2,0],[-2.8+1.6*(x%2)+4*(x//2),-0.8,0]))
		for x in range(8):
			line.append(Line([-3.15+0.3*(x%2)+2*(x//2),-1.3,0],[-3.35+0.7*(x%2)+2*(x//2),-1.7,0]))
		self.play(
			ShowCreation(line[0]),
			ShowCreation(line[1]),
			ShowCreation(line[2]),
			ShowCreation(line[3]),
			ShowCreation(line[4]),
			ShowCreation(line[5]),
			ShowCreation(line[6]),
			ShowCreation(line[7]),
			ShowCreation(line[8]),
			ShowCreation(line[9]),
			ShowCreation(line[10]),
			ShowCreation(line[11]),
			ShowCreation(line[12]),
			ShowCreation(line[13]),
			run_time = 1,
		)
		#computer science intro done
		self.wait(0.5)
		self.play (
			FadeOutAndShiftDown(circle[0]),
			FadeOutAndShiftDown(circle[1]),
			FadeOutAndShiftDown(circle[2]),
			FadeOutAndShiftDown(circle[3]),
			FadeOutAndShiftDown(circle[4]),
			FadeOutAndShiftDown(circle[5]),
			FadeOutAndShiftDown(circle[6]),
			FadeOutAndShiftDown(circle[7]),
			FadeOutAndShiftDown(circle[8]),
			FadeOutAndShiftDown(circle[9]),
			FadeOutAndShiftDown(circle[10]),
			FadeOutAndShiftDown(circle[11]),
			FadeOutAndShiftDown(circle[12]),
			FadeOutAndShiftDown(circle[13]),
			FadeOutAndShiftDown(circle[14]),
			FadeOutAndShiftDown(line[0]),
			FadeOutAndShiftDown(line[1]),
			FadeOutAndShiftDown(line[2]),
			FadeOutAndShiftDown(line[3]),
			FadeOutAndShiftDown(line[4]),
			FadeOutAndShiftDown(line[5]),
			FadeOutAndShiftDown(line[6]),
			FadeOutAndShiftDown(line[7]),
			FadeOutAndShiftDown(line[8]),
			FadeOutAndShiftDown(line[9]),
			FadeOutAndShiftDown(line[10]),
			FadeOutAndShiftDown(line[11]),
			FadeOutAndShiftDown(line[12]),
			FadeOutAndShiftDown(line[13]),
			FadeOutAndShiftDown(text),
			run_time = 0.5,
		)
		otss = TextMobject("On The Spot STEM").scale(3)
		self.play (
			Write(otss),
			run_time = 2,
		)
		self.wait(3)


class Triangle(Polygon):
    def __init__(self, **kwargs):
        kwargs["color"] = TRIANGLE_COLOR
        Polygon.__init__(
            self, 
            *POINTS2[[1, 0, 2]],
            edge_colors = [B_COLOR, C_COLOR, A_COLOR],
            fill_color = TRIANGLE_COLOR,
            fill_opacity = 0.5,
            **kwargs
        )
        #nudge = 0.2
        #target = POINTS[0]+nudge*(UP+RIGHT)
        #for direction in UP, RIGHT:
            #self.add_line(POINTS[0]+nudge*direction, target, color = WHITE)


def a_square(**kwargs):
    return Polygon(*POINTS2[[0, 2, 4, 3]], color = A_COLOR, **kwargs, fill_color = A_COLOR, fill_opacity = 0.5)

def b_square(**kwargs):
    return Polygon(*POINTS2[[1, 0, 5, 6]], color = B_COLOR, **kwargs, fill_color = B_COLOR, fill_opacity = 0.5)

def c_square(**kwargs):
    return Polygon(*POINTS2[[2, 1, 8, 7]], color = C_COLOR, **kwargs, fill_color = C_COLOR, fill_opacity = 0.5)


def triangle(**kwargs):
	return Polygon(*POINTS[[0, 1, 2]], color = TRI_COLOR, **kwargs, fill_color = TRI_COLOR, fill_opacity = 1)

def leftblock(**kwargs):
	return Polygon(*POINTS[[3, 4, 5, 6]], color = BLOCK_COLOR, **kwargs, fill_color = BLOCK_COLOR, fill_opacity = 0.8)

def rightblock(**kwargs):
	return Polygon(*POINTS[[10, 9, 8, 7]], color = BLOCK_COLOR, **kwargs, fill_color = BLOCK_COLOR, fill_opacity = 0.8)
