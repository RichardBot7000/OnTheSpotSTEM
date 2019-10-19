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
COLOR = [GREEN_D, BLUE, RED_D]
SCALE = 2/5
SHIFT_UP = -1
SHIFT_RIGHT = 0
CIRCLE_COLOR = WHITE
SIZE = 1/4
TRANS_UP = -2.5
TRANS_RIGHT = 0

POINTS = np.array([
    [0, -2, 0],
    [0, 1, 0],
    [-1, -2, 0],
    [0, -3, 0],
    [-1, -3, 0],
    [3, -2, 0],
    [3, 1, 0],
    [-4, -1, 0],
    [-3, 2, 0],
    [-2, -1, 0],
    [-2, 3, 0],
    [-6, 3, 0],
    [-6, -1, 0],
    [-2/3, 1, 0],
    [-7/3, -3, 0],
    [7/3, -3, 0],
    [-1/3, -5/3, 0],
    [-1/3, -3, 0],
    [-61/39, -15/13, 0],
    [11/15, -13/15, 0],
])

POINTS0 = np.array([
	[0*SCALE+SHIFT_RIGHT, -5*SCALE+SHIFT_UP, 0],
	[4*SCALE+SHIFT_RIGHT, 3*SCALE+SHIFT_UP, 0],
	[-7/5*SCALE+SHIFT_RIGHT, 24/5*SCALE+SHIFT_UP, 0],
	[-24/5*SCALE+SHIFT_RIGHT, 7/5*SCALE+SHIFT_UP, 0],
	[10*SCALE+SHIFT_RIGHT, -5*SCALE+SHIFT_UP, 0],
	[25/13*SCALE+SHIFT_RIGHT, 75/13*SCALE+SHIFT_UP, 0],
	[-125/31*SCALE+SHIFT_RIGHT, 125/31*SCALE+SHIFT_UP, 0],
	[-20/3*SCALE+SHIFT_RIGHT, -5*SCALE+SHIFT_UP, 0],
])

POINTS1 = np.array([
	[0*SIZE+TRANS_RIGHT, 0*SIZE+TRANS_UP, 0],
	[-5*SIZE+TRANS_RIGHT, 12*SIZE+TRANS_UP, 0],
	[-14*SIZE+TRANS_RIGHT, 0*SIZE+TRANS_UP, 0],
	[7*SIZE+TRANS_RIGHT, 10.5*SIZE+TRANS_UP, 0],
	[-1.4*SIZE+TRANS_RIGHT, 16.8*SIZE+TRANS_UP, 0],
	[7*SIZE+TRANS_RIGHT, 0*SIZE+TRANS_UP, 0],
	[-5, 1, 0],
	[3, -2, 0],
	[3, 2, 0],
	[-6, 2, 0],
])

DIR = np.array([
	[3, 2, 0],
	[-2, 1, 0],
	[-2, 2, 0],
	[2, 2, 0],
	[0, 1, 0],
	[-1, 1, 0],
	[10.5*0.25, 0, 0],
	[1, 0, 0],
])



class Intro(Scene):
	def construct(self):
		title = TextMobject("5 Proofs without Words").shift(2.5*UP).scale(2)
		definition = TextMobject("def:").shift(UP+6.3*LEFT).scale(0.75)
		text = TextMobject("proofs that can be demonstrated without verbal explanation")
		self.play(Write(title))
		self.wait()
		self.play(Write(definition))
		self.wait()
		self.play(Write(text))



class Ending(Scene):
	def construct(self):
		OTSS = 3.5
		title = TextMobject("Thanks for Watching!").shift(2.5*UP).scale(1.5)
		subscribe = TextMobject("Subscribe!").shift(OTSS*LEFT+1.25*UP)
		video = TextMobject("Most Recent Video!").shift(OTSS*RIGHT+1.25*UP)
		arrow_L = Vector(DOWN).move_to([-OTSS, 0.25, 0])
		arrow_R = Vector(DOWN).move_to([OTSS, 0.25, 0])
		self.play(Write(title))
		self.wait()
		self.play(Write(subscribe), GrowArrow(arrow_L))
		self.wait()
		self.play(Write(video), GrowArrow(arrow_R))
		self.wait()



class Pythag(Scene):
	def construct(self):
		text = TextMobject("Pythagorean Theorem")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		self.wait()
		tri = Triangle()
		self.play(ShowCreation(tri), run_time = 1)
		a = a_square()
		b = b_square()
		c = c_square()
		side_a = TextMobject("$a$", color = A_COLOR).shift(2.2*DOWN+0.5*LEFT)
		side_b = TextMobject("$b$", color = B_COLOR).shift(0.5*DOWN+0.2*RIGHT)
		side_c = TextMobject("$c$", color = C_COLOR).shift(0.5*DOWN+ 0.7*LEFT)
		self.play(
			FadeInFromDown(side_a),
			FadeInFrom(side_b, RIGHT),
			FadeInFrom(side_c, LEFT),
		)
		self.wait()
		area_a = TextMobject("$a^2$", color = A_COLOR).shift((POINTS[0]+POINTS[2]+POINTS[4]+POINTS[3])/4)
		area_b = TextMobject("$b^2$", color = B_COLOR).shift((POINTS[1]+POINTS[0]+POINTS[5]+POINTS[6])/4)
		area_c = TextMobject("$c^2$", color = C_COLOR).shift((POINTS[2]+POINTS[1]+POINTS[8]+POINTS[7])/4)
		self.play(
			ShowCreation(a),
			ShowCreation(b),
			ShowCreation(c),
			Transform(side_a, area_a),
			Transform(side_b, area_b),
			Transform(side_c, area_c),
			run_time = 3,
		)
		self.wait(1)
		tri2 = Triangle()
		self.add(tri2)
		x = 3
		y = 4
		z = 1
		self.play(
			side_a.shift, DIR[0],
			side_b.shift, DIR[0],
			tri.shift, DIR[0],
			a.shift, DIR[0],
			b.shift, DIR[0],
			side_c.shift, DIR[1],
			tri2.shift, DIR[1],
			c.shift, DIR[1],
			FadeOut(text),
			run_time = 2,
		)
		tri3 = Triangle().move_to(tri2)
		tri4 = Triangle().move_to(tri2)
		tri5 = Triangle().move_to(tri2)
		tri6 = Triangle().move_to(tri)
		tri7 = Triangle().move_to(tri)
		tri8 = Triangle().move_to(tri)
		self.play(
			tri3.shift, 3*LEFT+UP,
			tri3.rotate, PI,
			tri4.shift, LEFT+2*UP,
			tri4.rotate, PI/2,
			tri5.shift, DOWN+2*LEFT,
			tri5.rotate, -PI/2,
			tri6.rotate, PI,
			tri7.shift, 2*RIGHT+2*DOWN,
			tri7.rotate, PI/2,
			tri8.shift, 2*DOWN+2*RIGHT,
			tri8.rotate, -PI/2,
			run_time = 2,
		)
		big = big_square()
		self.play(
			ShowCreation(big),
			run_time = 2,
		)
		big2 = big_square()
		self.play(
			big2.shift, 8*RIGHT,
			run_time = 2,
		)
		self.play(
			FadeOut(tri),
			FadeOut(tri2),
			FadeOut(tri3),
			FadeOut(tri4),
			FadeOut(tri5),
			FadeOut(tri6),
			FadeOut(tri7),
			FadeOut(tri8),
		)
		equal = TextMobject("$=$").shift(1.2*LEFT+2*DOWN)
		plus = TextMobject("$+$").shift(1.2*RIGHT+2*DOWN)
		self.play(
			Write(equal),
			Write(plus),
			side_c.move_to, 2.4*LEFT+2*DOWN,
			side_a.move_to, 2*DOWN,
			side_b.move_to, 2.4*RIGHT+2*DOWN,
			run_time = 2,
		)
		self.play(
			side_c.scale, 2,
			side_b.scale, 2,
			side_a.scale, 2,
			equal.scale, 2,
			plus.scale, 2,
		)
		self.wait(2)



class area_rs(Scene):
	def construct(self):
		text = TextMobject("Inradius Area Formula")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		self.wait()
		tri = Polygon(*POINTS[[13, 14, 15]], color = WHITE)
		self.play(ShowCreation(tri), run_time = 2)
		circle = Circle(radius = 4/3, color = WHITE).shift(POINTS[16])
		self.play(GrowFromCenter(circle), run_time = 2)
		radius = []
		square = []
		lengths = []
		SHIFT = 1/4
		smalltri = []
		for x in range(3):
			radius.append(Line(POINTS[16], POINTS[17+x]))
			square.append(Square().scale(0.1))
			lengths.append(TextMobject("$r$"))
			lengths[x].shift((POINTS[16]+POINTS[17+x])/2)
			smalltri.append(Polygon(*POINTS[[16, 13+x, 13+((x+1)%3)]], color = COLOR[x], fill_color = COLOR[x], fill_opacity = 0.5))
		self.play(
			ShowCreation(radius[0]),
			ShowCreation(radius[1]),
			ShowCreation(radius[2]),
			run_time = 1.5,
		)
		square[0].shift(POINTS[17]+[1/10, 1/10, 0])
		square[1].rotate(np.arcsin(12/13)).shift(POINTS[18]+[1/10*7/13, -1/10*17/13, 0])
		square[2].rotate(np.arcsin(3/5)).shift(POINTS[19]+[-1/10*7/5, 1/10*1/5, 0])
		self.play(
			FadeIn(square[0]),
			FadeIn(square[1]),
			FadeIn(square[2]),
		)
		lengths[0].shift([-SHIFT, 0, 0])
		lengths[1].shift([SHIFT*5/13, SHIFT*12/13, 0])
		lengths[2].shift([SHIFT*3/5, -SHIFT*4/5, 0])
		self.play(
			FadeOutAndShiftDown(circle),
			FadeInFromDown(lengths[0]),
			FadeInFromDown(lengths[1]),
			FadeInFromDown(lengths[2]),
			run_time = 1.5,
		)
		self.play(
			ShowCreation(smalltri[0]),
			ShowCreation(smalltri[1]),
			ShowCreation(smalltri[2]),
			run_time = 4,
		)
		lengths.append(TextMobject("$a$", color = B_COLOR).shift((POINTS[14]+POINTS[15])/2+[0, -SHIFT, 0]))
		lengths.append(TextMobject("$b$", color = C_COLOR).shift((POINTS[15]+POINTS[13])/2+[SHIFT*4/5, SHIFT*3/5, 0]))
		lengths.append(TextMobject("$c$", color = A_COLOR).shift((POINTS[13]+POINTS[14])/2+[-SHIFT*5/13, SHIFT*12/13, 0]))
		self.play(
			FadeOut(tri),
			FadeInFromDown(lengths[3]),
			FadeInFrom(lengths[4], RIGHT),
			FadeInFrom(lengths[5], LEFT),
		)
		self.wait()
		self.play(
			FadeOut(text),
			smalltri[0].shift, DIR[2],
			smalltri[2].shift, DIR[3],
			smalltri[1].shift, DIR[4],
			radius[0].shift, DIR[4],
			radius[1].shift, DIR[2],
			radius[2].shift, DIR[3],
			lengths[0].shift, DIR[4],
			lengths[1].shift, DIR[2],
			lengths[2].shift, DIR[3],
			lengths[3].shift, DIR[4],
			lengths[4].shift, DIR[3],
			lengths[5].shift, DIR[2],
			square[0].shift, DIR[4],
			square[1].shift, DIR[2],
			square[2].shift, DIR[3],
			run_time = 3,
		)
		for x in range(3):
			lengths.append(TextMobject("$A =$").move_to(lengths[3+x]))
		for x in range(3):
			lengths.append(TextMobject("$\\frac{1}{2}$").move_to(lengths[3+x]))
		lengths[6].shift([-4*SHIFT, -2*SHIFT, 0])
		lengths[7].shift([4*SHIFT, 0, 0])
		lengths[8].shift([-8*SHIFT, 0, 0])
		lengths[9].shift([-1*SHIFT, -2*SHIFT, 0])
		lengths[10].shift([7*SHIFT, 0, 0])
		lengths[11].shift([-5*SHIFT, 0, 0])
		self.play(
			FadeIn(lengths[6]),
			FadeIn(lengths[7]),
			FadeIn(lengths[8]),
			FadeIn(lengths[9]),
			FadeIn(lengths[10]),
			FadeIn(lengths[11]),
			lengths[0].move_to, lengths[6],
			lengths[0].shift, 4.5*SHIFT*RIGHT,
			lengths[1].move_to, lengths[8],
			lengths[1].shift, 4.5*SHIFT*RIGHT,
			lengths[2].move_to, lengths[7],
			lengths[2].shift, 5*SHIFT*RIGHT,
			lengths[3].move_to, lengths[6],
			lengths[3].shift, 6*SHIFT*RIGHT,
			lengths[4].move_to, lengths[7],
			lengths[4].shift, 6.4*SHIFT*RIGHT+0.25*SHIFT*UP,
			lengths[5].move_to, lengths[8],
			lengths[5].shift, 6*SHIFT*RIGHT,
			run_time = 2,
		)
		self.wait()
		plus1 = TextMobject("$+$").move_to(lengths[6]).shift(DIR[5]+7.5*SHIFT*RIGHT)
		plus2 = TextMobject("$+$").move_to(lengths[6]).shift(DIR[5]+13.5*SHIFT*RIGHT)
		par1 = TextMobject("$($").move_to(lengths[6]).shift(DIR[5]+4.5*SHIFT*RIGHT)
		par2 = TextMobject("$)$").move_to(lengths[6]).shift(DIR[5]+13.5*SHIFT*RIGHT)
		s = TextMobject("$s$").move_to(lengths[6]).shift(DIR[5]+8.25*SHIFT*RIGHT)
		self.play(
			smalltri[0].shift, -DIR[2]+2.5*UP,
			smalltri[2].shift, -DIR[3]+2.5*UP,
			smalltri[1].shift, -DIR[4]+2.5*UP,
			radius[0].shift, -DIR[4]+2.5*UP,
			radius[1].shift, -DIR[2]+2.5*UP,
			radius[2].shift, -DIR[3]+2.5*UP,
			square[0].shift, -DIR[4]+2.5*UP,
			square[1].shift, -DIR[2]+2.5*UP,
			square[2].shift, -DIR[3]+2.5*UP,
			lengths[6].shift, DIR[5],
			lengths[0].shift, DIR[5],
			lengths[3].shift, DIR[5],
			lengths[9].shift, DIR[5],
			lengths[7].move_to, lengths[6],
			lengths[7].shift, DIR[5],
			lengths[2].move_to, lengths[6],
			lengths[2].shift, DIR[5]+10.5*SHIFT*RIGHT,
			lengths[4].move_to, lengths[6],
			lengths[4].shift, DIR[5]+12*SHIFT*RIGHT+0.25*SHIFT*UP,
			lengths[8].move_to, lengths[6],
			lengths[8].shift, DIR[5],
			lengths[10].move_to, lengths[6],
			lengths[10].shift, DIR[5]+9*SHIFT*RIGHT,
			lengths[1].move_to, lengths[6],
			lengths[1].shift, DIR[5]+16.5*SHIFT*RIGHT,
			lengths[5].move_to, lengths[6],
			lengths[5].shift, DIR[5]+18*SHIFT*RIGHT,
			lengths[11].move_to, lengths[6],
			lengths[11].shift, DIR[5]+15*SHIFT*RIGHT,
			FadeIn(plus1),
			FadeIn(plus2),
			run_time = 4,
		)
		self.wait()
		self.play(
			lengths[0].shift, DIR[6],
			lengths[10].move_to, lengths[9],
			lengths[11].move_to, lengths[9],
			lengths[1].move_to, lengths[0],
			lengths[1].shift, DIR[6],
			lengths[2].move_to, lengths[0],
			lengths[2].shift, DIR[6],
			lengths[4].shift, 3*SHIFT*LEFT,
			lengths[5].shift, 6*SHIFT*LEFT,
			plus2.shift, 3*SHIFT*LEFT,
			FadeIn(par1),
			FadeIn(par2),
			FadeOut(lengths[7]),
			FadeOut(lengths[8]),
			run_time = 3,
		)
		self.play(
			FadeOutAndShift(lengths[9], RIGHT),
			FadeOutAndShift(lengths[10], RIGHT),
			FadeOutAndShift(lengths[11], RIGHT),
			FadeOutAndShift(par1, RIGHT),
			FadeOutAndShift(lengths[3], RIGHT),
			FadeOutAndShift(plus1, RIGHT),
			FadeOutAndShift(lengths[4], LEFT),
			FadeOutAndShift(plus2, LEFT),
			FadeOutAndShift(lengths[5], LEFT),
			FadeOutAndShift(par2, LEFT),
			FadeIn(s),
			FadeOut(lengths[1]),
			FadeOut(lengths[2]),
			run_time = 3,
		)
		self.play(
			lengths[6].shift, DIR[7],
			lengths[0].move_to, lengths[6],
			lengths[0].shift, 6*SHIFT*RIGHT+DIR[7]+0.5*SHIFT*DOWN,
			s.move_to, lengths[6],
			s.shift, 9*SHIFT*RIGHT+DIR[7]+0.5*SHIFT*DOWN,
			run_time = 2,
		)
		self.play(
			lengths[6].scale, 2,
			lengths[0].scale, 2,
			s.scale, 2,
		)
		self.wait(2)



class Excircle(Scene):
	def construct(self):
		text = TextMobject("Exradius Area Formula")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		self.wait()
		tri = Polygon(*POINTS1[[0, 1, 2]], color = WHITE)
		line = [Line(POINTS1[1], POINTS1[4]), Line(POINTS1[0], POINTS1[5]), Line(POINTS1[3], POINTS1[4]), Line(POINTS1[3], POINTS1[5])]
		circle = Circle(color = WHITE, radius = 10.5*SIZE).move_to(POINTS1[3])
		arr = ["$b$", "$a$", "$c$"]
		lengths = []
		SHIFT = 1/4
		MOVE_RIGHT = [0, 12/13, -4/5]
		MOVE_UP = [-1, 5/13, 3/5]
		square = [Square().scale(0.1), Square().scale(0.1)]
		square[0].move_to(POINTS1[5]).shift(0.1*UP+0.1*LEFT)
		square[1].move_to(POINTS1[4]).rotate(np.arcsin(4/5)).shift(0.14*DOWN+0.02*RIGHT)
		for x in range(3):
			lengths.append(TextMobject(arr[x]).move_to((POINTS1[(x+2)%3]+POINTS1[(x+3)%3])/2+SHIFT*MOVE_RIGHT[x]*RIGHT+SHIFT*MOVE_UP[x]*UP))
		lengths.append(TextMobject("$r_a$").move_to((POINTS1[3]+POINTS1[4])/2).shift(SHIFT*4/5*UP+SHIFT*3/5*RIGHT))
		lengths.append(TextMobject("$r_a$").move_to((POINTS1[3]+POINTS1[5])/2).shift(SHIFT*RIGHT))
		triangle = [Polygon(*POINTS1[[2, 1, 3]], color = RED_D, fill_color = RED_D, fill_opacity = 0.5)]
		triangle.append(Polygon(*POINTS1[[2, 0, 3]], color = BLUE, fill_color = BLUE, fill_opacity = 0.5))
		triangle.append(Polygon(*POINTS1[[3, 1, 0]], color = BLACK, fill_color = BLACK, fill_opacity = 1))
		for x in range(3):
			lengths.append(TextMobject("$\\frac{1}{2}$"))
		lengths[5].move_to(POINTS1[6])
		lengths[6].move_to(POINTS1[7])
		lengths[7].move_to(POINTS1[8])
		lengths.append(TextMobject("$r_a$").move_to(POINTS1[8]+1.5*SHIFT*RIGHT))
		minus = TextMobject("$-$").move_to(POINTS1[8]-1.5*SHIFT*RIGHT)
		area = TextMobject("$A=$").move_to(POINTS1[9]+0.5*SHIFT*UP)
		plus = TextMobject("$+$").move_to(POINTS1[9]+7.5*SHIFT*RIGHT)
		times = TextMobject("$\\cdot$").move_to(POINTS1[9]+4.5*SHIFT*RIGHT)
		parl = TextMobject("$($").move_to(POINTS1[9]+7.5*SHIFT*RIGHT)
		parr = TextMobject("$)$").move_to(POINTS1[9]+16.5*SHIFT*RIGHT)
		plus2 = TextMobject("$+$").move_to(POINTS1[9]+13.5*SHIFT*RIGHT)
		a = TextMobject("$a$").move_to(POINTS1[9]+15*SHIFT*RIGHT)
		two = TextMobject("$2$").move_to(POINTS1[9]+18*SHIFT*RIGHT)
		s = TextMobject("$s$").move_to(POINTS1[9]+12*SHIFT*RIGHT)
		self.play(ShowCreation(tri), run_time = 2)
		self.play(
			FadeInFrom(lengths[0], DOWN),
			FadeInFrom(lengths[1], RIGHT),
			FadeInFrom(lengths[2], LEFT),
		)
		self.play(
			ShowCreation(line[0]),
			ShowCreation(line[1]),
		)
		self.play(GrowFromCenter(circle), FadeOutAndShift(text, UP), run_time = 2)
		self.play(
			ShowCreation(line[2]),
			ShowCreation(line[3]),
			run_time = 1.5,
		)
		self.play(
			FadeIn(square[0]),
			FadeIn(square[1]),
			FadeInFrom(lengths[3], UR),
			FadeInFrom(lengths[4], RIGHT),
			FadeOutAndShift(circle, UR),
			run_time = 2,
		)
		self.play(
			ShowCreation(triangle[0]),
			ShowCreation(triangle[1]),
			lengths[0].set_color, BLUE,
			lengths[2].set_color, RED_D,
			run_time = 3,
		)
		self.wait()
		self.play(
			FadeInFrom(lengths[5], RIGHT),
			FadeInFrom(lengths[6], UP),
			lengths[3].move_to, POINTS1[6]+1.5*SHIFT*RIGHT,
			lengths[4].move_to, POINTS1[7]+1.5*SHIFT*RIGHT,
			lengths[0].move_to, POINTS1[7]+3*SHIFT*RIGHT,
			lengths[2].move_to, POINTS1[6]+3*SHIFT*RIGHT,
			run_time = 3,
		)
		self.wait()
		self.play(
			FadeIn(triangle[2]),
			FadeInFrom(lengths[7], UR),
			FadeInFrom(lengths[8], UR),
			FadeInFrom(minus, UR),
			lengths[1].move_to, POINTS1[8]+3*SHIFT*RIGHT,
			run_time = 3,
		)
		self.wait()
		self.play(
			FadeOut(triangle[0]),
			FadeOut(triangle[1]),
			run_time = 1,
		)
		self.play(
			FadeOut(triangle[2]), 
			FadeOut(line[0]),
			FadeOut(line[1]),
			FadeOut(line[2]),
			FadeOut(line[3]),
			FadeOut(square[0]),
			FadeOut(square[1]),
			run_time = 0.5,
		)
		self.wait()
		self.play(
			FadeInFrom(area, UP),
			lengths[6].move_to, POINTS1[9]+3*SHIFT*RIGHT,
			lengths[4].move_to, POINTS1[9]+4.5*SHIFT*RIGHT,
			lengths[0].move_to, POINTS1[9]+6*SHIFT*RIGHT,
			run_time = 2,
		)
		self.play(
			FadeInFrom(plus, UP),
			lengths[5].move_to, POINTS1[9]+9*SHIFT*RIGHT,
			lengths[3].move_to, POINTS1[9]+10.5*SHIFT*RIGHT,
			lengths[2].move_to, POINTS1[9]+12*SHIFT*RIGHT,
			run_time = 2,
		)
		self.play(
			ShowCreation(line[0]),
			ShowCreation(line[1]),
			GrowFromCenter(circle),
			minus.move_to, POINTS1[9]+13.5*SHIFT*RIGHT,
			lengths[7].move_to, POINTS1[9]+15*SHIFT*RIGHT,
			lengths[8].move_to, POINTS1[9]+16.5*SHIFT*RIGHT,
			lengths[1].move_to, POINTS1[9]+18*SHIFT*RIGHT,
			run_time = 3,
		)
		self.wait()
		self.play(
			FadeIn(times),
			FadeIn(parl),
			FadeIn(parr),
			lengths[3].move_to, POINTS1[9]+3*SHIFT*RIGHT,
			lengths[4].move_to, POINTS1[9]+3*SHIFT*RIGHT,
			lengths[8].move_to, POINTS1[9]+3*SHIFT*RIGHT,
			lengths[5].move_to, POINTS1[9]+6*SHIFT*RIGHT,
			lengths[6].move_to, POINTS1[9]+6*SHIFT*RIGHT,
			lengths[7].move_to, POINTS1[9]+6*SHIFT*RIGHT,
			lengths[0].move_to, POINTS1[9]+9*SHIFT*RIGHT,
			plus.move_to, POINTS1[9]+10.5*SHIFT*RIGHT,
			lengths[2].move_to, POINTS1[9]+12*SHIFT*RIGHT,
			minus.move_to, POINTS1[9]+13.5*SHIFT*RIGHT,
			lengths[1].move_to, POINTS1[9]+15*SHIFT*RIGHT,
			run_time = 3,
		)
		self.wait()
		self.play(
			Write(plus2),
			Write(a),
			Write(two),
			minus.shift, 3*SHIFT*RIGHT,
			lengths[1].shift, 4.5*SHIFT*RIGHT,
			parr.shift, 4.5*SHIFT*RIGHT,
			FadeOut(lengths[6]),
			FadeOut(lengths[7]),
			FadeOut(lengths[4]),
			FadeOut(lengths[8]),
			run_time = 4,
		)
		self.wait()
		self.play(
			FadeOutAndShift(lengths[5], RIGHT),
			FadeOutAndShift(lengths[0], RIGHT),
			FadeOutAndShift(plus, RIGHT),
			FadeOut(lengths[2]),
			FadeOutAndShift(plus2, LEFT),
			FadeOut(two),
			FadeOutAndShift(a, LEFT),
			Write(s),
			parl.shift, 1.5*SHIFT*RIGHT,
			FadeOut(times),
			lengths[3].shift, 3*SHIFT*RIGHT,
			minus.shift, 1.5*SHIFT*LEFT,
			lengths[1].shift, 1.5*SHIFT*LEFT,
			run_time = 4,
		)
		self.wait()
		self.play(
			area.scale, 2,
			lengths[3].scale, 2,
			parl.scale, 2,
			s.scale, 2,
			minus.scale, 2,
			lengths[1].scale, 2,
			parr.scale, 2,
			run_time = 1,
		)
		self.wait(2)



class Pitot(Scene):
	def construct(self):
		text = TextMobject("Pitot Theorem")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		self.wait()
		quad = Polygon(*POINTS0[[4, 5, 6, 7]], color = WHITE)
		circle = Circle(radius = 5*SCALE, color = CIRCLE_COLOR, fill_color = CIRCLE_COLOR, fill_opacity = 0.5)
		circle.shift([SHIFT_RIGHT, SHIFT_UP, 0])
		tangent = []
		color_array = ["#FF0000", "#FFFF00", "#00FF00", "#0000FF"]
		arr = ["$a$", "$b$", "$c$", "$d$"]
		lengths = []
		SHIFT = 1/4
		MOVE_RIGHT = [-7/25, -24/25, 0, 4/5]
		MOVE_UP = [24/25, 7/25, -1, 3/5]
		seg = [10, 45/13, 85/31, 20/3]
		left = -5.5
		right = -3.5
		for x in range(4):
			tangent.append(Line(POINTS0[x+4], POINTS0[x], color = color_array[x]))
			tangent.append(Line(POINTS0[x+4], POINTS0[(x+1)%4], color = color_array[x]))
			lengths.append(TextMobject(arr[x]).move_to((POINTS0[(x+1)%4+4]+POINTS0[(x+2)%4+4])/2+SHIFT*MOVE_RIGHT[x]*RIGHT+SHIFT*MOVE_UP[x]*UP))
		self.play(ShowCreation(quad), run_time = 2.5)
		self.play(GrowFromCenter(circle), run_time = 1.5)
		self.play(
			FadeInFrom(lengths[0], UP),
			FadeInFrom(lengths[1], LEFT),
			FadeInFrom(lengths[2], DOWN),
			FadeInFrom(lengths[3], RIGHT),
		)
		self.play(
			ShowCreation(tangent[0]),
			ShowCreation(tangent[1]),
			ShowCreation(tangent[2]),
			ShowCreation(tangent[3]),
			ShowCreation(tangent[4]),
			ShowCreation(tangent[5]),
			ShowCreation(tangent[6]),
			ShowCreation(tangent[7]),
			run_time = 2.5,
		)
		plus0 = TextMobject("$+$").move_to([left+1.5*SHIFT, 3, 0])
		plus1 = TextMobject("$+$").move_to([left+1.5*SHIFT, 2, 0])
		equals0 = TextMobject("$=$").move_to([left+4.5*SHIFT, 3, 0])
		equals1 = TextMobject("$=$").move_to([left+4.5*SHIFT, 2, 0])
		self.play(
			Rotating(tangent[3], radians = -np.arcsin(7/25), about_point = POINTS0[2], rate_func = smooth, run_time = 2),
			Rotating(tangent[4], radians = -np.arcsin(7/25), about_point = POINTS0[2], rate_func = smooth, run_time = 2),
			run_time = 1,
		)
		self.play(
			FadeOutAndShift(text, UP),
			lengths[0].move_to, [left, 3, 0],
			tangent[3].move_to, [right+SCALE*(seg[2]+seg[1]/2), 3, 0],
			tangent[4].move_to, [right+SCALE*(seg[2]/2), 3, 0],
			run_time = 2,
		)
		self.play(
			FadeInFrom(plus0, DOWN),
			FadeInFromDown(equals0),
			lengths[2].move_to, [left+3*SHIFT, 3, 0],
			tangent[7].move_to, [right+SCALE*(seg[2]+seg[1]+seg[3]/2), 3, 0],
			tangent[0].move_to, [right+SCALE*(seg[2]+seg[1]+seg[3]+seg[0]/2), 3, 0],
			run_time = 3,
		)
		self.play(
			Rotating(tangent[5], radians = PI-np.arcsin(24/25), about_point = POINTS0[3], rate_func = smooth, run_time = 2),
			Rotating(tangent[6], radians = PI-np.arcsin(24/25), about_point = POINTS0[3], rate_func = smooth, run_time = 2),
			run_time = 1,
		)
		self.play(
			lengths[1].move_to, [left, 2, 0],
			tangent[5].move_to, [right+SCALE*(seg[2]/2), 2, 0],
			tangent[6].move_to, [right+SCALE*(seg[2]+seg[3]/2), 2, 0],
			run_time = 2,
		)
		self.play(
			Rotating(tangent[1], radians = np.arcsin(4/5), about_point = POINTS0[1], rate_func = smooth, run_time = 2),
			Rotating(tangent[2], radians = np.arcsin(4/5), about_point = POINTS0[1], rate_func = smooth, run_time = 2),
			run_time = 1,
		)
		self.play(
			FadeInFrom(plus1, DOWN),
			FadeInFromDown(equals1),
			lengths[3].move_to, [left+3*SHIFT, 2, 0],
			tangent[2].move_to, [right+SCALE*(seg[2]+seg[3]+seg[1]/2), 2, 0],
			tangent[1].move_to, [right+SCALE*(seg[2]+seg[3]+seg[1]+seg[0]/2), 2, 0],
			run_time = 2,
		)
		self.play(
			FadeOutAndShift(tangent[0], RIGHT),
			FadeOutAndShift(tangent[1], RIGHT),
			FadeOutAndShift(tangent[2], RIGHT),
			FadeOutAndShift(tangent[3], RIGHT),
			FadeOutAndShift(tangent[4], RIGHT),
			FadeOutAndShift(tangent[5], RIGHT),
			FadeOutAndShift(tangent[6], RIGHT),
			FadeOutAndShift(tangent[7], RIGHT),
			equals0.move_to, [0, 2.5, 0],
			equals1.move_to, [0, 2.5, 0],
			lengths[0].move_to, [0-9*SHIFT, 2.5, 0],
			lengths[1].move_to, [0+3*SHIFT, 2.5, 0],
			lengths[2].move_to, [0-3*SHIFT, 2.5, 0],
			lengths[3].move_to, [0+9*SHIFT, 2.5, 0],
			plus0.move_to, [0-6*SHIFT, 2.5, 0],
			plus1.move_to, [0+6*SHIFT, 2.5, 0],
			run_time = 3,
		)
		self.play(
			lengths[0].scale, 2,
			lengths[1].scale, 2,
			lengths[2].scale, 2,
			lengths[3].scale, 2,
			plus0.scale, 2,
			plus1.scale, 2,
			equals0.scale, 2,
			equals1.scale, 2,
		)
		self.wait(2)



class Geometric_Series(Scene):
	def construct(self):
		text = TextMobject("Infinite Geometric Series")
		text.shift(2.5*UP)
		text.scale(2)
		self.play(Write(text), run_time = 1)
		self.wait()
		UNIT = 4
		RATIO = 2/3
		line = []
		power = []
		plus = []
		lengths = [TextMobject("$S$"), TextMobject("$1$"), TextMobject("$r$"), TextMobject("$1-r$"), TextMobject("$1$")]
		lengths[0].set_color(BLUE)
		lengths[1].set_color(BLUE)
		lengths[3].set_color(RED_D)
		lengths[4].set_color(RED_D)
		TICK_LENGTH = 0.1
		x = -UNIT/(2*(1-RATIO))
		y = -2.5
		LOW = 6
		NUM = 12
		COORD = np.array([
			[x, y, 0],
			[-x, y, 0],
			[x, y+UNIT, 0],
			[x+UNIT, y+UNIT*RATIO, 0],
			[x+UNIT, y+UNIT, 0],
			[x+UNIT, y, 0],
			[4, 2, 0],
			[1, 1, 0],
		])
		tick = [Line([x, y-TICK_LENGTH, 0], [x, y+TICK_LENGTH, 0])]
		power.append(TextMobject("$r^0$"))
		power.append(TextMobject("$r^1$"))
		power.append(TextMobject("$r^2$"))
		power.append(TextMobject("$r^3$"))
		power.append(TextMobject("$r^4$"))
		power.append(TextMobject("$r^5$"))
		lengths[0].move_to([0, y-0.5, 0])
		lengths[1].move_to([x-0.5, y+UNIT/2, 0])
		lengths[2].move_to([x+UNIT-0.5, y+UNIT*RATIO/2, 0])
		lengths[3].move_to([x+UNIT+1, y+UNIT*RATIO+UNIT*(1-RATIO)/2, 0])
		lengths[4].move_to([x+UNIT/2, y+UNIT+0.5, 0])
		for i in range(LOW, NUM):
			power.append(TextMobject("$.$"))
		self.play(FadeIn(tick[0]), run_time = 0.2)
		for i in range(NUM):
			line.append(Line([x, y, 0], [x+UNIT*(RATIO**i), y, 0]))
			power[i].move_to([x+UNIT*(RATIO**i)/2, y-0.5, 0])
			x += UNIT*(RATIO**i)
			tick.append(Line([x, y-TICK_LENGTH, 0], [x, y+TICK_LENGTH, 0]))
			plus.append(TextMobject("$+$").move_to([x, y-0.5, 0]))
			if i == 5:
				power[i].shift(0.1*RIGHT)
			if i < 3:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
				)
			elif i < LOW:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
					run_time = 0.75,
				)
			else:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
					run_time = 0.5,
				)
		line.append(Line([x, y, 0], [UNIT/(2*(1-RATIO)), y, 0]))
		line.append(Line([-UNIT/(2*(1-RATIO)), y+UNIT, 0], [UNIT/(2*(1-RATIO)), y, 0]))
		square = Square().scale(UNIT/2).move_to([-UNIT/(2*(1-RATIO))+UNIT/2, y+UNIT/2, 0]).rotate(PI/2)
		triangle = Polygon(*COORD[[2, 0, 1]], color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
		updatedtriangle = Polygon(*COORD[[3, 5, 1]], color = RED_D, fill_color = RED_D, fill_opacity = 0.5)
		equals = TextMobject("$=$").move_to(COORD[6])
		frac_L = Line(COORD[6]+1.5*LEFT, COORD[6]+0.5*LEFT)
		frac_R = Line(COORD[6]+1.5*RIGHT, COORD[6]+0.5*RIGHT)
		self.play(ShowCreation(square), run_time = 2)
		self.play(ShowCreation(line[NUM+1]), run_time = 2)
		self.play(ShowCreation(line[NUM]), run_time = 0.2)
		for i in range(LOW-1):
			self.play(FadeIn(plus[i]), run_time = 0.5)
		self.play(
			FadeInFrom(lengths[1], LEFT),
			FadeInFrom(lengths[4], DOWN),
			FadeOutAndShift(text, UP),
			run_time = 2,
		)
		self.play(
			ShowCreation(triangle),
			run_time = 2,
		)
		self.play(
			triangle.scale, RATIO,
			triangle.shift, UNIT/2*RIGHT+UNIT*(1-RATIO)/2*DOWN,
			FadeInFrom(lengths[2], LEFT),
			run_time = 2,
		)
		self.play(
			FadeInFrom(lengths[3], RIGHT),
			run_time = 1.5,
		)
		self.play(
			GrowFromCenter(updatedtriangle),
			run_time = 1.5,
		)
		self.play(
			updatedtriangle.scale, (1-RATIO)/RATIO,
			updatedtriangle.shift, UNIT/2*LEFT+UNIT*(RATIO-1/2)*UP,
			run_time = 1,
		)
		self.play(
			Rotating(updatedtriangle, radians = -PI, about_point = COORD[3], rate_func = smooth, run_time = 3),
			run_time = 2,
		)
		self.play(
			triangle.scale, 1/RATIO,
			triangle.shift, UNIT/2*LEFT+UNIT*(1-RATIO)/2*UP,
			run_time = 2,
		)
		self.play(
			FadeIn(lengths[0]),
			FadeOutAndShift(power[0], RIGHT),
			FadeOutAndShift(power[1], RIGHT),
			FadeOutAndShift(power[2], RIGHT),
			FadeOutAndShift(power[3], LEFT),
			FadeOutAndShift(power[4], LEFT),
			FadeOutAndShift(power[5], LEFT),
			FadeOutAndShift(power[6], LEFT),
			FadeOutAndShift(power[7], LEFT),
			FadeOutAndShift(power[8], LEFT),
			FadeOutAndShift(power[9], LEFT),
			FadeOutAndShift(power[10], LEFT),
			FadeOutAndShift(power[11], LEFT),
			FadeOutAndShift(plus[0], RIGHT),
			FadeOutAndShift(plus[1], LEFT),
			FadeOutAndShift(plus[2], LEFT),
			FadeOutAndShift(plus[3], LEFT),
			FadeOutAndShift(plus[4], LEFT),
			run_time = 2,
		)
		self.play(
			FadeIn(equals),
			FadeIn(frac_L),
			lengths[0].move_to, COORD[6]+0.35*UP+LEFT,
			lengths[1].move_to, COORD[6]+0.35*DOWN+LEFT,
			run_time = 3,
		)
		self.play(
			FadeIn(frac_R),
			lengths[4].move_to, COORD[6]+0.35*UP+RIGHT,
			lengths[3].move_to, COORD[6]+0.35*DOWN+RIGHT,
			run_time = 3,
		)
		self.play(
			FadeOutAndShiftDown(lengths[1]),
			FadeOutAndShiftDown(frac_L),
			lengths[0].move_to, COORD[6]+LEFT,
			run_time = 2,
		)
		self.play(
			equals.move_to, COORD[7],
			lengths[0].move_to, (COORD[7]+LEFT),
			lengths[4].move_to, (COORD[7]+0.7*UP+2*RIGHT),
			frac_R.move_to, (COORD[7]+2*RIGHT),
			lengths[3].move_to, (COORD[7]+0.7*DOWN+2*RIGHT),
			run_time = 3,
		)
		self.play(
			equals.scale, 2,
			lengths[0].scale, 2,
			lengths[4].scale, 2,
			frac_R.scale, 2,
			lengths[3].scale, 2,
		)
		self.wait(2)



class NewSceneRotateUpdate(Scene):
    def construct(self):
        arrow=Vector(UP)
        arrow.to_corner(UL)

        direction=RIGHT*12+DOWN*4
        radians=TAU
        arrow.starting_mobject=arrow.copy()

        def update_arrow(mob,alpha):
            mob.become(mob.starting_mobject)
            mob.rotate(alpha*radians)
            mob.shift(alpha*direction)

        self.play(GrowArrow(arrow))
        self.play(
            UpdateFromAlphaFunc(arrow,update_arrow,rate_func=linear,run_time=5)
        )
        self.wait()



class RotatingAndMove(Animation):
	CONFIG = {
		"axis": OUT,
		"radians": TAU,
		"run_time": 5,
		"rate_func": smooth,
		"about_point": None,
		"about_edge": None,
	}
	def __init__(self, mobject, direction,**kwargs):
		assert(isinstance(mobject, Mobject))
		digest_config(self, kwargs)
		self.mobject = mobject
		self.direction = direction

	def interpolate_mobject(self, alpha):
		self.mobject.become(self.starting_mobject)
		self.mobject.rotate(
			alpha * self.radians,
			axis=self.axis,
			about_point=self.about_point,
			about_edge=self.about_edge,
		)
		self.mobject.shift(alpha*self.direction)



def Triangle(**kwargs):
	return Polygon(*POINTS[[1, 0, 2]], color = TRI_COLOR, **kwargs, fill_color = TRI_COLOR, fill_opacity = 0.5)

def a_square(**kwargs):
    return Polygon(*POINTS[[0, 2, 4, 3]], color = A_COLOR, **kwargs, fill_color = A_COLOR, fill_opacity = 0.5)

def b_square(**kwargs):
    return Polygon(*POINTS[[1, 0, 5, 6]], color = B_COLOR, **kwargs, fill_color = B_COLOR, fill_opacity = 0.5)

def c_square(**kwargs):
    return Polygon(*POINTS[[2, 1, 8, 7]], color = C_COLOR, **kwargs, fill_color = C_COLOR, fill_opacity = 0.5)

def big_square(**kwargs):
	return Polygon(*POINTS[[9, 10, 11, 12]], color = WHITE, **kwargs, fill_color = WHITE, fill_opacity = 0)