from big_ol_pile_of_manim_imports import *
import numpy as np
import itertools as it
from copy import deepcopy
import sys

from manimlib.constants import *

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon
from manimlib.once_useful_constructs.region import  region_from_polygon_vertices, region_from_line_boundary

SHIFT1R = -5
SHIFT1U = 1
SCALE1 = 0.2
SHIFT2R = 2
SHIFT2U = 1
SCALE2 = 0.2
SHIFT3R = -5
SHIFT3U = -3
SCALE3 = 0.2
SHIFT4R = 2
SHIFT4U = -3
SCALE4 = 0.2
POINTSR = -1
POINTSU = -2.75
POINTSSCALE = 0.5
transform = [-0.7, -1, 0.35, -3.7]
quadtransform = [-2, 0, 0.75, 0, 0, 0.75]
righttransform = [1.4, -2.5, 0.4]

METHOD1 = np.array([
	[0*SCALE1+SHIFT1R, 12*SCALE1+SHIFT1U, 0],
	[9*SCALE1+SHIFT1R, 0*SCALE1+SHIFT1U, 0],
	[-5*SCALE1+SHIFT1R, 0*SCALE1+SHIFT1U, 0],
	[0*SCALE1+SHIFT1R, 0*SCALE1+SHIFT1U, 0],
])

METHOD2 = np.array([
	[0*SCALE2+SHIFT2R, 12*SCALE2+SHIFT2U, 0],
	[9*SCALE2+SHIFT2R, 0*SCALE2+SHIFT2U, 0],
	[-5*SCALE2+SHIFT2R, 0*SCALE2+SHIFT2U, 0],	
])

METHOD3 = np.array([
	[0*SCALE3+SHIFT3R, 12*SCALE3+SHIFT3U, 0],
	[9*SCALE3+SHIFT3R, 0*SCALE3+SHIFT3U, 0],
	[-5*SCALE3+SHIFT3R, 0*SCALE3+SHIFT3U, 0],	
	[1*SCALE3+SHIFT3R, 4*SCALE3+SHIFT3U, 0],
	[1*SCALE3+SHIFT3R, 0*SCALE3+SHIFT3U, 0],
	[-35/13*SCALE3+SHIFT3R, 72/13*SCALE3+SHIFT3U, 0],
	[21/5*SCALE3+SHIFT3R, 32/5*SCALE3+SHIFT3U, 0],
])

METHOD4 = np.array([
	[0*SCALE4+SHIFT4R, 12*SCALE4+SHIFT4U, 0],
	[9*SCALE4+SHIFT4R, 0*SCALE4+SHIFT4U, 0],
	[-5*SCALE4+SHIFT4R, 0*SCALE4+SHIFT4U, 0],
	[2*SCALE4+SHIFT4R, 33/8*SCALE4+SHIFT4U, 0],
])

POINTS = np.array([
	[0*POINTSSCALE+POINTSR, 12*POINTSSCALE+POINTSU, 0],
	[-5*POINTSSCALE+POINTSR, 0*POINTSSCALE+POINTSU, 0],
	[9*POINTSSCALE+POINTSR, 0*POINTSSCALE+POINTSU, 0],	
	[1*POINTSSCALE+POINTSR, 4*POINTSSCALE+POINTSU, 0],
	[1*POINTSSCALE+POINTSR, 0*POINTSSCALE+POINTSU, 0],
	[21/5*POINTSSCALE+POINTSR, 32/5*POINTSSCALE+POINTSU, 0],
	[-35/13*POINTSSCALE+POINTSR, 72/13*POINTSSCALE+POINTSU, 0],
])

POINTS0 = np.array([
	[0*transform[2]+transform[0], 12*transform[2]+transform[1], 0],
	[-5*transform[2]+transform[0], 0*transform[2]+transform[1], 0],
	[9*transform[2]+transform[0], 0*transform[2]+transform[1], 0],	
	[1*transform[2]+transform[0], 4*transform[2]+transform[1], 0],
	[1*transform[2]+transform[0], 0*transform[2]+transform[1], 0],
	[21/5*transform[2]+transform[0], 32/5*transform[2]+transform[1], 0],
	[-35/13*transform[2]+transform[0], 72/13*transform[2]+transform[1], 0],
	[9*transform[2]+transform[0], -8*transform[2]+transform[1], 0],
	[11/3*transform[2]+transform[0], 0*transform[2]+transform[1], 0]
])

POINTS1 = np.array([
	[0*transform[2]+transform[3], 12*transform[2]+transform[1], 0],
	[-5*transform[2]+transform[3], 0*transform[2]+transform[1], 0],
	[9*transform[2]+transform[3], 0*transform[2]+transform[1], 0],	
	[1*transform[2]+transform[3], 4*transform[2]+transform[1], 0],
	[1*transform[2]+transform[3], 0*transform[2]+transform[1], 0],
	[21/5*transform[2]+transform[3], 32/5*transform[2]+transform[1], 0],
	[-35/13*transform[2]+transform[3], 72/13*transform[2]+transform[1], 0],
	[9*transform[2]+transform[3], -8*transform[2]+transform[1], 0],
	[11/3*transform[2]+transform[3], 0*transform[2]+transform[1], 0]
])

CYCLICQUAD = np.array([
	[-3*quadtransform[2]+quadtransform[0], 4*quadtransform[2]+quadtransform[1], 0],
	[-4*quadtransform[2]+quadtransform[0], -3*quadtransform[2]+quadtransform[1], 0],
	[4*quadtransform[2]+quadtransform[0], -3*quadtransform[2]+quadtransform[1], 0],
	[7/5*quadtransform[2]+quadtransform[0], 24/5*quadtransform[2]+quadtransform[1], 0],
	[0*quadtransform[2]+quadtransform[0], 0*quadtransform[2]+quadtransform[1], 0],
	[-3*quadtransform[5]+quadtransform[3], 4*quadtransform[5]+quadtransform[4], 0],
	[-4*quadtransform[5]+quadtransform[3], -3*quadtransform[5]+quadtransform[4], 0],
	[4*quadtransform[5]+quadtransform[3], -3*quadtransform[5]+quadtransform[4], 0],
	[7/5*quadtransform[5]+quadtransform[3], 24/5*quadtransform[5]+quadtransform[4], 0],
	[0*quadtransform[5]+quadtransform[3], 0*quadtransform[5]+quadtransform[4], 0],
])

RIGHTTRIANGLE = np.array([
	[0*righttransform[2]+righttransform[0], 0*righttransform[2]+righttransform[1], 0],
	[0*righttransform[2]+righttransform[0], 12*righttransform[2]+righttransform[1], 0],
	[-16*righttransform[2]+righttransform[0], 0*righttransform[2]+righttransform[1], 0],
	[9*righttransform[2]+righttransform[0], 0*righttransform[2]+righttransform[1], 0],
])

COLOR = ["#FF0000", "#00FF00", "#0000FF", RED_D, GREEN_D, BLUE]



class ShowAreas(Scene):
	def construct(self):
		horiz = Line([-8, 0, 0], [8, 0, 0])
		vert = Line([0, -4.5, 0], [0, 4.5, 0])
		self.play(
			GrowFromCenter(horiz),
			GrowFromCenter(vert),
			run_time = 2,
		)
		triangle1 = Polygon(*METHOD1[[0, 1, 2]], color = WHITE)
		triangle2 = Polygon(*METHOD2[[0, 1, 2]], color = WHITE)
		triangle3 = Polygon(*METHOD3[[0, 1, 2]], color = WHITE)
		triangle4 = Polygon(*METHOD4[[0, 1, 2]], color = WHITE)
		alt = Line(METHOD1[0], METHOD1[3])
		incircle = Circle(color = WHITE, radius = 4*SCALE3).move_to(METHOD3[3])
		circumcircle = Circle(color = WHITE, radius = 65/8*SCALE4).move_to(METHOD4[3])
		rtangle = Square().scale(0.1).move_to(METHOD1[3]+0.1*RIGHT+0.1*UP)
		angle = Arc(radius = 0.2, angle = np.arcsin(4/5)).move_to(METHOD2[1]).rotate(PI-np.arcsin(4/5)).shift(0.16*LEFT+0.08*UP)
		radius = []
		points = []
		lengths = []
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP]
		constant = 0.15
		MOVE = [constant*LEFT, constant*12/13*UP+constant*5/13*RIGHT, constant*3/5*RIGHT+constant*4/5*DOWN, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		x = 16
		y = 9
		LOC = np.array([[x*SCALE1+SHIFT1R, y*SCALE1+SHIFT1U, 0], [x*SCALE2+SHIFT2R, y*SCALE2+SHIFT2U, 0],
			[x*SCALE3+SHIFT3R, y*SCALE3+SHIFT3U, 0], [x*SCALE4+SHIFT4R, y*SCALE4+SHIFT4U, 0]])
		for i in range(3):
			radius.append(Line(METHOD3[3], METHOD3[4+i]))
			points.append(TextMobject(arr[i]).move_to(METHOD1[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD2[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD3[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD4[(3-i)%3]).shift(DIR[i]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD1[(4-i)%3]+METHOD1[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD2[(4-i)%3]+METHOD2[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD3[(4-i)%3]+METHOD3[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD4[(4-i)%3]+METHOD4[(5-i)%3])/2).shift(DIR[i+3]))
		lengths.append(TextMobject("$h$").move_to((METHOD1[0]+METHOD1[3])/2).shift(0.25*RIGHT))
		for i in range(3):
			radius.append(Line(METHOD4[3], METHOD4[i]))
			lengths.append(TextMobject("$r$").move_to((METHOD3[3]+METHOD3[4+i])/2).shift(MOVE[i]))
		for i in range(3):
			lengths.append(TextMobject("$R$").move_to((METHOD4[3]+METHOD4[i])/2).shift(MOVE[3+i]))
		for i in range(12):
			points[i].scale(0.75)
		for i in range(19):
			lengths[i].scale(0.6)
		area = [TextMobject("$A = \\frac{1}{2}ah$"), TextMobject("$A = \\frac{1}{2}ab\\sin{C}$"), TextMobject("$A = rs$")]
		area.append(TextMobject("$A = \\frac{abc}{4R}$"))
		radius_group = VGroup()
		points_group = VGroup()
		lengths_group = VGroup()
		for i in range(len(radius)):
			radius_group.add(radius[i])
		for i in range(len(points)):
			points_group.add(points[i])
		for i in range(len(lengths)):
			lengths_group.add(lengths[i])
		for i in range(4):
			area[i].move_to(LOC[i])
		self.play(
			ShowCreation(triangle1),
			ShowCreation(triangle2),
			ShowCreation(triangle3),
			ShowCreation(triangle4),
			run_time = 2,
		)
		self.play(
			ShowCreation(alt),
			GrowFromCenter(incircle),
			GrowFromCenter(circumcircle),
			run_time = 2,
		)
		self.play(
			ShowCreation(radius[0]),
			ShowCreation(radius[1]),
			ShowCreation(radius[2]),
			ShowCreation(radius[3]),
			ShowCreation(radius[4]),
			ShowCreation(radius[5]),
			FadeIn(rtangle),
			FadeIn(angle),
		)
		self.play(
			FadeIn(points_group)
		)
		self.play(
			FadeIn(lengths_group)
		)
		self.play(
			Write(area[0]),
			Write(area[1]),
			Write(area[2]),
			Write(area[3]),
		)
		self.wait()


class IntroduceHerons(Scene):
	def construct(self):
		SHIFTR = -0.5
		SHIFTU = -1
		SCALE = 0.25
		HERONS = np.array([
			[0*SCALE+SHIFTR, 12*SCALE+SHIFTU, 0],
			[-5*SCALE+SHIFTR, 0*SCALE+SHIFTU, 0],
			[9*SCALE+SHIFTR, 0*SCALE+SHIFTU, 0],
		])
		herons = TextMobject("Heron's Formula").scale(2.5)
		s = TextMobject("$s = \\frac{a+b+c}{2}$").shift(3*DOWN)
		area = TextMobject("$A = \\sqrt{s(s-a)(s-b)(s-c)}$").shift(2*DOWN)
		triangle = Polygon(*HERONS[[0, 1, 2]], color = WHITE)
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		text = []
		MOVE = [SCALE*UP, SCALE*LEFT, SCALE*RIGHT, SCALE*DOWN, SCALE*4/5*RIGHT+SCALE*3/5*UP, SCALE*12/13*LEFT+SCALE*5/13*UP]
		for i in range(3):
			text.append(TextMobject(arr[i]).move_to(HERONS[i]).shift(MOVE[i]))
		for i in range(3):
			text.append(TextMobject(arr[i+3]).move_to((HERONS[(i+1)%3]+HERONS[(i+2)%3])/2).shift(MOVE[i+3]))
		self.play(Write(herons))
		box = SurroundingRectangle(area, color = YELLOW)
		self.play(
			herons.scale, 0.8,
			herons.shift, 3*UP,
		)
		self.play(ShowCreation(triangle))
		self.play(
			FadeIn(text[0]),
			FadeIn(text[1]),
			FadeIn(text[2]),
			FadeIn(text[3]),
			FadeIn(text[4]),
			FadeIn(text[5]),
		)
		self.wait()
		self.play(Write(area))
		self.play(ShowCreation(box))
		self.wait()
		self.play(Write(s))
		self.wait()


class AlgebraProof(Scene):
	def construct(self):
		RIGHTSCALE = 0.3
		RIGHTSHIFTR = -4.75
		RIGHTSHIFTU = -3
		RIGHTPOINTS = np.array([
			[0*RIGHTSCALE+RIGHTSHIFTR, 12*RIGHTSCALE+RIGHTSHIFTU, 0],
			[-5*RIGHTSCALE+RIGHTSHIFTR, 0*RIGHTSCALE+RIGHTSHIFTU, 0],
			[9*RIGHTSCALE+RIGHTSHIFTR, 0*RIGHTSCALE+RIGHTSHIFTU, 0],
		])
		constant = 0.25
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		DIR = [constant*UP, constant*LEFT, constant*RIGHT, 
		constant*DOWN, constant*4/5*RIGHT+constant*3/5*UP, constant*24/25*LEFT+constant*7/25*UP]
		tri = Polygon(*RIGHTPOINTS[[0, 1, 2]], color = WHITE)
		self.play(ShowCreation(tri), run_time = 2)
		values = []
		arcradius = 0.4
		angle = Arc(radius = arcradius, angle = np.arcsin(4/5)).move_to(RIGHTPOINTS[2]).rotate(PI-np.arcsin(4/5)).shift(arcradius*4/5*LEFT+arcradius*2/5*UP)
		for i in range(3):
			values.append(TextMobject(arr[i]).move_to(RIGHTPOINTS[i]).shift(DIR[i]))
		for i in range(3):
			values.append(TextMobject(arr[3+i]).move_to((RIGHTPOINTS[(i+1)%3]+RIGHTPOINTS[(i+2)%3])/2).shift(DIR[3+i]))
		for i in range(3):
			values[i].scale(1)
		for i in range(3, 6):
			values[i].scale(1)
		self.play(FadeInFrom(values[0], UP), FadeInFrom(values[1], LEFT), FadeInFrom(values[2], RIGHT))
		self.play(FadeInFrom(values[3], DOWN), FadeInFrom(values[4], UR), FadeInFrom(values[5], UL))
		self.play(FadeIn(angle))
		lines = ["$A = \\frac{1}{2}ab\\sin{C}$", 
			"$\\sin{C} = \\sqrt{1-\\cos^2{C}}$",
			"$c^2 = a^2+b^2-2ab\\cos{C}$",
			"$\\cos{C} = \\frac{a^2+b^2-c^2}{2ab}$",
			"$= \\frac{1}{2}ab\\sqrt{1-\\cos^2{C}}$",
			"$= \\frac{1}{2}ab\\frac{\\sqrt{4a^2b^2-(a^2+b^2-c^2)^2}}{2ab}$",
			"$= \\frac{1}{4}\\sqrt{4a^2b^2-(a^2+b^2-c^2)^2}$",
			"$= \\frac{1}{4}\\sqrt{(2ab-(a^2+b^2-c^2))(2ab+(a^2+b^2-c^2))}$",
			"$= \\frac{1}{4}\\sqrt{(c^2-(a-b)^2)((a+b)^2-c^2)}$",
			"$= \\sqrt{\\frac{(c-(a-b))(c+(a-b))((a+b)-c)((a+b)+c)}{16}}$",
			"$= \\sqrt{\\frac{(b+c-a)}{2}\\frac{(a+c-b)}{2}\\frac{(a+b-c)}{2}\\frac{(a+b+c)}{2}}$",
			"$= \\sqrt{\\frac{(a+b+c)}{2}\\frac{(b+c-a)}{2}\\frac{(a+c-b)}{2}\\frac{(a+b-c)}{2}}$",
			"$A = \\sqrt{s(s-a)(s-b)(s-c)}$",
		]
		y = 3.5
		proof = [TextMobject(lines[0]).move_to([-0.3, y, 0]).scale(0.75)]
		y -= 0.5
		a = -4.25
		b = 3.75
		LOC = [a, b, 0]
		BOX = np.array([
			[a-2.25, b, 0],
			[a+2.25, b, 0],
			[a+2.25, b-2, 0],
			[a-2.25, b-2, 0],
		])
		for i in range(1, 4):
			proof.append(TextMobject(lines[i]).scale(0.75).move_to([LOC+i*0.5*DOWN]))
		for i in range(4, len(lines)-1):
			proof.append(TextMobject(lines[i]).move_to([2, y, 0]).scale(0.75).align_to(proof[0], LEFT))
			if (i < 4):
				y -= 0.5
			elif (i < 9):
				y -= 0.65
			else:
				y -= 0.75
		for i in range(4, len(lines)-1):
			proof[i].shift(0.39*RIGHT)
		box = Polygon(*BOX[[0, 1, 2, 3]], color = BLUE)
		self.play(Write(proof[0]), run_time = 1)
		self.wait()
		for i in range(1, len(proof)):
			self.play(Write(proof[i]), run_time = 0.5)
			if i == 3:
				self.play(ShowCreation(box), run_time = 2)
				self.wait()
		formula = TexMobject("A", "=", "\\sqrt{", "s", "\\left(", "s", "-", "a\\right)", "\\left(", "s", "-", "b\\right)", "\\left(", "s", "-", "c\\right))}").scale(0.75).move_to(proof[11].get_center()+0.75*DOWN).align_to(proof[0], LEFT)
		self.play(Write(formula), run_time = 1.5)
		rect = SurroundingRectangle(formula, color=YELLOW)
		self.play(ShowCreation(rect), run_time = 2)
		self.wait()
		v_text = VGroup(proof[0])
		for i in range(4, 12):
			v_text.add(proof[i])
		movetriangle = [4.15, 2.5, 0]
		self.play(
			FadeOutAndShift(proof[1], UL),
			FadeOutAndShift(proof[2], UL),
			FadeOutAndShift(proof[3], UL),
			FadeOutAndShift(box, UL),
			FadeOutAndShift(v_text, UR),
			tri.shift, movetriangle,
			values[0].shift, movetriangle,
			values[1].shift, movetriangle,
			values[2].shift, movetriangle,
			values[3].shift, movetriangle,
			values[4].shift, movetriangle,
			values[5].shift, movetriangle,
			angle.shift, movetriangle,
			formula.move_to, [0, -2, 0],
			rect.move_to, [0, -2, 0],
			run_time = 2,
		)
		self.play(
			formula.scale, 2,
			rect.scale, 2,
		)
		self.wait()
		highlight = formula.copy()
		changes = [4, 6, 10, 14]
		self.play(*[WiggleOutThenIn(formula[i]) for i in changes])
		self.wait()


class EnlargeIncircle(Scene):
	def construct(self):
		INSCALE = 0.5
		INSHIFTR = -3
		INSHIFTU = -2.75
		SCALEDTRIANGLE = np.array([
			[0*INSCALE+INSHIFTR, 12*INSCALE+INSHIFTU, 0],
			[9*INSCALE+INSHIFTR, 0*INSCALE+INSHIFTU, 0],
			[-5*INSCALE+INSHIFTR, 0*INSCALE+INSHIFTU, 0],	
			[1*INSCALE+INSHIFTR, 4*INSCALE+INSHIFTU, 0],
			[1*INSCALE+INSHIFTR, 0*INSCALE+INSHIFTU, 0],
			[-35/13*INSCALE+INSHIFTR, 72/13*INSCALE+INSHIFTU, 0],
			[21/5*INSCALE+INSHIFTR, 32/5*INSCALE+INSHIFTU, 0],
		])
		horiz = Line([-8, 0, 0], [8, 0, 0])
		vert = Line([0, -4.5, 0], [0, 4.5, 0])
		triangle1 = Polygon(*METHOD1[[0, 1, 2]], color = WHITE)
		triangle2 = Polygon(*METHOD2[[0, 1, 2]], color = WHITE)
		triangle3 = Polygon(*METHOD3[[0, 1, 2]], color = WHITE)
		triangle4 = Polygon(*METHOD4[[0, 1, 2]], color = WHITE)
		alt = Line(METHOD1[0], METHOD1[3])
		incircle = Circle(color = WHITE, radius = 4*SCALE3).move_to(METHOD3[3])
		circumcircle = Circle(color = WHITE, radius = 65/8*SCALE4).move_to(METHOD4[3])
		rtangle = Square().scale(0.1).move_to(METHOD1[3]+0.1*RIGHT+0.1*UP)
		angle = Arc(radius = 0.2, angle = np.arcsin(4/5)).move_to(METHOD2[1]).rotate(PI-np.arcsin(4/5)).shift(0.16*LEFT+0.08*UP)
		radius = []
		points = []
		lengths = []
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP]
		constant = 0.15
		MOVE = [constant*LEFT, constant*12/13*UP+constant*5/13*RIGHT, constant*3/5*RIGHT+constant*4/5*DOWN, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		x = 16
		y = 9
		LOC = np.array([[x*SCALE1+SHIFT1R, y*SCALE1+SHIFT1U, 0], [x*SCALE2+SHIFT2R, y*SCALE2+SHIFT2U, 0],
			[x*SCALE3+SHIFT3R, y*SCALE3+SHIFT3U, 0], [x*SCALE4+SHIFT4R, y*SCALE4+SHIFT4U, 0]])
		for i in range(3):
			radius.append(Line(METHOD3[3], METHOD3[4+i]))
			points.append(TextMobject(arr[i]).move_to(METHOD1[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD2[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD3[(3-i)%3]).shift(DIR[i]))
			points.append(TextMobject(arr[i]).move_to(METHOD4[(3-i)%3]).shift(DIR[i]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD1[(4-i)%3]+METHOD1[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD2[(4-i)%3]+METHOD2[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD3[(4-i)%3]+METHOD3[(5-i)%3])/2).shift(DIR[i+3]))
			lengths.append(TextMobject(arr[3+i]).move_to((METHOD4[(4-i)%3]+METHOD4[(5-i)%3])/2).shift(DIR[i+3]))
		lengths.append(TextMobject("$h$").move_to((METHOD1[0]+METHOD1[3])/2).shift(0.25*RIGHT))
		for i in range(3):
			radius.append(Line(METHOD4[3], METHOD4[i]))
			lengths.append(TextMobject("$r$").move_to((METHOD3[3]+METHOD3[4+i])/2).shift(MOVE[i]))
		for i in range(3):
			lengths.append(TextMobject("$R$").move_to((METHOD4[3]+METHOD4[i])/2).shift(MOVE[3+i]))
		for i in range(12):
			points[i].scale(0.75)
		for i in range(19):
			lengths[i].scale(0.6)
		area = [TextMobject("$A = \\frac{1}{2}ah$"), TextMobject("$A = \\frac{1}{2}ab\\sin{C}$"), TextMobject("$A = rs$")]
		area.append(TextMobject("$A = \\frac{abc}{4R}$"))
		for i in range(4):
			area[i].move_to(LOC[i])
		self.add(horiz, vert, triangle1, triangle2, triangle3, triangle4, alt, incircle, circumcircle, rtangle, angle)
		v_drawing = VGroup(horiz, vert, triangle1, triangle2, triangle4, alt, circumcircle, rtangle, angle)
		for i in range(6):
			self.add(radius[i])
		for i in range(12):
			self.add(points[i])
		for i in range(19):
			self.add(lengths[i])
		for i in range(4):
			self.add(area[i])
		box = SurroundingRectangle(area[2], color = YELLOW)
		self.wait()
		self.play(ShowCreation(box))
		self.wait()
		for i in range(3, 6):
			v_drawing.add(radius[i])
		for i in range(12):
			if i % 4 != 2:
				v_drawing.add(points[i])
		for i in range(13):
			if i % 4 != 2:
				v_drawing.add(lengths[i])
		for i in range(16, 19):
			v_drawing.add(lengths[i])
		for i in range(4):
			if i != 2:
				v_drawing.add(area[i])
		self.play(FadeOut(v_drawing))
		self.wait()
		bigtri = Polygon(*SCALEDTRIANGLE[[0, 1, 2]], color = WHITE)
		bigincircle = Circle(color = WHITE, radius = 4*INSCALE).move_to(SCALEDTRIANGLE[3])
		bigradius = []
		newpoints = []
		matrix = [[0, 1, 2], [2, 6, 10], [2, 6, 10, 13, 14, 15]]
		for i in range(3):
			bigradius.append(Line(SCALEDTRIANGLE[3], SCALEDTRIANGLE[4+i]))
		for i in range(3):
			newpoints.append(TextMobject(arr[i]).move_to(SCALEDTRIANGLE[(3-i)%3]).shift(DIR[i]))
			newpoints.append(TextMobject(arr[3+i]).move_to((SCALEDTRIANGLE[(4-i)%3]+SCALEDTRIANGLE[(5-i)%3])/2).shift(DIR[i+3]))
			newpoints.append(TextMobject("$r$").move_to((SCALEDTRIANGLE[3]+SCALEDTRIANGLE[4+i])/2).shift(MOVE[i]*2))
		#remaining radius[0, 1, 2], points[2, 6, 10], lengths[2, 6, 10, 13, 14, 15], area[2], triangle, incircle
		self.play(
			Transform(triangle3, bigtri),
			Transform(incircle, bigincircle),
			Transform(radius[0], bigradius[0]),
			Transform(radius[1], bigradius[1]),
			Transform(radius[2], bigradius[2]),
			Transform(points[2], newpoints[0]),
			Transform(points[6], newpoints[3]),
			Transform(points[10], newpoints[6]),
			Transform(lengths[2], newpoints[1]),
			Transform(lengths[6], newpoints[4]),
			Transform(lengths[10], newpoints[7]),
			Transform(lengths[13], newpoints[2]),
			Transform(lengths[14], newpoints[5]),
			Transform(lengths[15], newpoints[8]),
			area[2].scale, 2.5,
			area[2].shift, 5.5*RIGHT+2*UP,
			box.scale, 2.5,
			box.shift, 5.5*RIGHT+2*UP,
			run_time = 2,
		)


class DrawTriangle(Scene):
	def construct(self):
		triangle = Polygon(*POINTS[[0, 1, 2]], color = WHITE)
		self.play(ShowCreation(triangle), run_time = 2)
		circle = Circle(color = WHITE, radius = 4*POINTSSCALE).move_to(POINTS[3])
		self.play(GrowFromCenter(circle), run_time = 1.5)
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP]
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		constant = 0.15
		MOVE = [constant*LEFT, constant*3/5*RIGHT+constant*4/5*DOWN, constant*12/13*UP+constant*5/13*RIGHT, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		labels = []
		radius = []
		v_group = []
		for i  in range(4):
			v_group.append(VGroup())
		for i in range(3):
			labels.append(TextMobject(arr[i]).move_to(POINTS[i]).shift(DIR[i]*1.5))
			labels.append(TextMobject(arr[3+i]).move_to((POINTS[(i+1)%3]+POINTS[(i+2)%3])/2).shift(DIR[i+3]*1.5))
			labels.append(TextMobject("$r$").move_to((POINTS[3]+POINTS[4+i])/2).shift(MOVE[i]*2))
			radius.append(Line(POINTS[3], POINTS[4+i]))
		for i in range(9):
			v_group[i%3].add(labels[i])
		self.play(ShowCreation(radius[0]), ShowCreation(radius[1]), ShowCreation(radius[2]), run_time = 1.5)
		self.wait()
		self.play(FadeIn(v_group[0]))
		self.play(FadeIn(v_group[1]))
		self.play(FadeIn(v_group[2]))
		self.wait()
		tangents = []
		for i in range(3):
			tangents.append(Line(POINTS[i], POINTS[(i+1)%3+4], color = COLOR[i]))
			tangents.append(Line(POINTS[i], POINTS[(i+2)%3+4], color = COLOR[i]))
		self.play(
			ShowCreation(tangents[0]),
			ShowCreation(tangents[1]),
			ShowCreation(tangents[2]),
			ShowCreation(tangents[3]),
			ShowCreation(tangents[4]),
			ShowCreation(tangents[5]),
			run_time = 2,
		)
		self.wait()


class FindTangents(Scene):
	def construct(self):
		triangle = Polygon(*POINTS[[0, 1, 2]], color = WHITE)
		circle = Circle(color = WHITE, radius = 4*POINTSSCALE).move_to(POINTS[3])
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP]
		arr = ["A", "B", "C", "$a$", "$b$", "$c$", "$x$", "$y$", "$z$"]
		constant = 0.15
		MOVE = [constant*LEFT, constant*3/5*RIGHT+constant*4/5*DOWN, constant*12/13*UP+constant*5/13*RIGHT, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		labels = []
		radius = []
		v_group = []
		tangents = []
		xyz = []
		for i in range(3):
			tangents.append(Line(POINTS[i], POINTS[(i+1)%3+4], color = COLOR[i]))
			tangents.append(Line(POINTS[i], POINTS[(i+2)%3+4], color = COLOR[i]))
		for i  in range(6):
			v_group.append(VGroup())
		#[0] vertex, [1] side, [2] r, [3] radius, [4], triangle and incircle, [5] xyz
		for i in range(3):
			labels.append(TextMobject(arr[i]).move_to(POINTS[i]).shift(DIR[i]*1.5))
			labels.append(TextMobject(arr[3+i]).move_to((POINTS[(i+1)%3]+POINTS[(i+2)%3])/2).shift(DIR[i+3]*1.5))
			labels.append(TextMobject("$r$").move_to((POINTS[3]+POINTS[4+i])/2).shift(MOVE[i]*2))
			radius.append(Line(POINTS[3], POINTS[4+i]))
		for i in range(9):
			v_group[i%3].add(labels[i])
		self.add(triangle, circle)
		for i in range(3):
			self.add(radius[i])
			v_group[3].add(radius[i])
		for i in range(9):
			self.add(labels[i])
		for i in range(6):
			self.add(tangents[i])
		self.wait()
		self.play(FadeOutAndShift(labels[0], UP), FadeOutAndShift(labels[3], DL), FadeOutAndShift(labels[6], DR))
		self.wait()
		self.play(FadeOut(v_group[3]), FadeOut(v_group[2]))
		self.wait()
		self.play(
			labels[1].shift, DIR[3]*2,
			labels[4].shift, DIR[4]*2,
			labels[7].shift, DIR[5]*2,
			run_time = 2,
		)
		for i in range(3):
			xyz.append(TextMobject(arr[6+i], color = COLOR[3+i]).move_to((POINTS[i]+POINTS[(i+1)%3+4])/2).shift(DIR[3+(i+1)%3]))
			xyz.append(TextMobject(arr[6+i], color = COLOR[3+i]).move_to((POINTS[i]+POINTS[(i+2)%3+4])/2).shift(DIR[3+(i+2)%3]))
		for i in range(6):
			v_group[5].add(xyz[i])
		self.wait()
		self.play(
			FadeInFrom(xyz[0], UR),
			FadeInFrom(xyz[1], UL),
			FadeInFrom(xyz[2], UL),
			FadeInFrom(xyz[3], DOWN),
			FadeInFrom(xyz[4], DOWN),
			FadeInFrom(xyz[5], UR),
			run_time = 1.5
		)
		v_group[4].add(triangle, circle)
		for i in range(6):
			v_group[4].add(tangents[i])
		self.wait()
		self.play(
			v_group[1].shift, 3*LEFT,
			v_group[4].shift, 3*LEFT,
			v_group[5].shift, 3*LEFT,
			run_time = 2,
		)
		self.wait()
		self.play(
			WiggleOutThenIn(xyz[0]),
			WiggleOutThenIn(xyz[1]),
		)
		self.wait()
		self.play(
			WiggleOutThenIn(xyz[2]),
			WiggleOutThenIn(xyz[3]),
		)
		self.wait()
		self.play(
			WiggleOutThenIn(xyz[4]),
			WiggleOutThenIn(xyz[5]),
		)
		self.wait()
		EQU = [3.5, 2, 0]
		equals = []
		plus = []
		for i in range(10):
			equals.append(TextMobject("$=$").move_to(EQU).shift(0.5*i*DOWN))
		for i in range(3):
			plus.append(TextMobject("$+$").move_to(EQU).shift(0.5*i*DOWN+LEFT))
		for i in range(3):
			self.play(FadeIn(equals[i]), FadeIn(plus[i]), run_time = 0.2)
		self.wait()
		self.play(
			xyz[3].move_to, EQU+1.5*LEFT,
			xyz[4].move_to, EQU+0.5*LEFT,
			xyz[5].move_to, EQU+1.5*LEFT+0.5*DOWN,
			xyz[0].move_to, EQU+0.5*LEFT+0.5*DOWN,
			xyz[1].move_to, EQU+1.5*LEFT+DOWN,
			xyz[2].move_to, EQU+0.5*LEFT+DOWN,
			labels[1].move_to, EQU+0.5*RIGHT,
			labels[4].move_to, EQU+0.5*RIGHT+0.5*DOWN,
			labels[7].move_to, EQU+0.5*RIGHT+DOWN,
			run_time = 2.5,
		)
		eqnL = TextMobject("$2$", "$x$", "$+$", "$2$", "$y$", "$+$", "$2$", "$z$")
		for i in range(3):
			eqnL[1+3*i].set_color(COLOR[3+i])
		eqnR = TextMobject("$a$", "$+$", "$b$", "$+$", "$c$")
		eqnL.move_to(EQU+1.5*DOWN).align_to(xyz[2], RIGHT)
		eqnR.move_to(EQU+1.5*DOWN).align_to(labels[7], LEFT)
		self.wait()
		self.play(Write(eqnL[0:8]))
		self.play(Write(equals[3]), run_time = 0.2)
		self.play(Write(eqnR[0:5]))
		self.wait()
		eqnR1 = TextMobject("$2$", "$s$").align_to(labels[7], LEFT).align_to(eqnL, UP)
		eqnL2 = TextMobject("$x$", "$+$", "$y$", "$+$", "$z$").align_to(eqnL, DOWN).align_to(eqnL, RIGHT)
		for i in range(3):
			eqnL2[2*i].set_color(COLOR[3+i])
		eqnR2 = TextMobject("$s$").align_to(eqnR1, DOWN).align_to(eqnR, LEFT)
		self.play(Transform(eqnR, eqnR1))
		self.play(Transform(eqnL, eqnL2), Transform(eqnR, eqnR2), run_time = 1.5)
		self.wait()
		eqnL3 = TextMobject("$x$", "$+$", "$y$", "$+$", "$z$").align_to(eqnL, DOWN).align_to(eqnL, RIGHT).shift(0.5*DOWN)
		for i in range(3):
			eqnL3[2*i].set_color(COLOR[3+i])
		eqnR3 = TextMobject("$s$").align_to(eqnR2, UP).align_to(eqnR, LEFT).shift(0.5*DOWN)
		self.play(Write(eqnL3[0:8]))
		self.play(Write(equals[4]), run_time = 0.2)
		self.play(Write(eqnR3[0:5]))
		self.wait()
		eqnL4 = TextMobject("$x$", "$+$", "$a$").align_to(eqnL, UP).align_to(eqnL, RIGHT).shift(0.5*DOWN)
		eqnL4[0].set_color(COLOR[3])
		self.play(Transform(eqnL3, eqnL4))
		self.wait()
		eqnL5 = TextMobject("$x$").move_to(eqnL4).align_to(eqnL, RIGHT).set_color(COLOR[3])
		eqnR5 = TextMobject("$s$", "$-$", "$a$").align_to(eqnR3, UP).align_to(eqnR3, LEFT)
		self.play(Transform(eqnL3, eqnL5), Transform(eqnR3, eqnR5))
		self.wait()
		#same for y and z
		eqnL6 = TextMobject("$y$", "$+$", "$z$", "$+$", "$x$").align_to(eqnL, DOWN).align_to(eqnL, RIGHT).shift(DOWN)
		eqnL7 = TextMobject("$z$", "$+$", "$x$", "$+$", "$y$").align_to(eqnL, DOWN).align_to(eqnL, RIGHT).shift(1.5*DOWN)
		for i in range(3):
			eqnL6[2*i].set_color(COLOR[(i+1)%3+3])
			eqnL7[2*i].set_color(COLOR[(i+2)%3+3])
		eqnR6 = TextMobject("$s$").align_to(eqnR2, UP).align_to(eqnR, LEFT).shift(DOWN)
		eqnR7 = TextMobject("$s$").align_to(eqnR2, UP).align_to(eqnR, LEFT).shift(1.5*DOWN)
		self.play(Write(eqnL6[0:8]), run_time = 0.5)
		self.play(Write(equals[5]), run_time = 0.1)
		self.play(Write(eqnR6[0:5]), run_time = 0.5)
		self.play(Write(eqnL7[0:8]), run_time = 0.5)
		self.play(Write(equals[6]), run_time = 0.1)
		self.play(Write(eqnR7[0:5]), run_time = 0.5)
		self.wait(0.5)
		eqnL8 = TextMobject("$y$", "$+$", "$b$").align_to(eqnL, DOWN).align_to(eqnL, RIGHT).shift(DOWN)
		eqnL8[0].set_color(COLOR[4])
		eqnL9 = TextMobject("$z$", "$+$", "$c$").align_to(eqnL, UP).align_to(eqnL, RIGHT).shift(1.5*DOWN)
		eqnL9[0].set_color(COLOR[5])
		self.play(Transform(eqnL6, eqnL8), Transform(eqnL7, eqnL9))
		eqnL10 = TextMobject("$y$").align_to(eqnL6, DOWN).align_to(eqnL, RIGHT).set_color(COLOR[4])
		eqnR10 = TextMobject("$s$", "$-$", "$b$").align_to(eqnR3, DOWN).align_to(eqnR3, LEFT).shift(0.5*DOWN)
		eqnL11 = TextMobject("$z$").move_to(equals[6]).align_to(eqnL, RIGHT).set_color(COLOR[5])
		eqnR11 = TextMobject("$s$", "$-$", "$c$").align_to(eqnR3, UP).align_to(eqnR3, LEFT).shift(DOWN)
		self.play(Transform(eqnL6, eqnL10), Transform(eqnL7, eqnL11), Transform(eqnR6, eqnR10), Transform(eqnR7, eqnR11))
		self.wait()


class RevisitFormula(Scene):
	def construct(self):
		RIGHTSCALE = 0.4
		RIGHTSHIFTR = -4.75
		RIGHTSHIFTU = -3
		RIGHTPOINTS = np.array([
			[0*RIGHTSCALE+RIGHTSHIFTR, 12*RIGHTSCALE+RIGHTSHIFTU, 0],
			[-5*RIGHTSCALE+RIGHTSHIFTR, 0*RIGHTSCALE+RIGHTSHIFTU, 0],
			[9*RIGHTSCALE+RIGHTSHIFTR, 0*RIGHTSCALE+RIGHTSHIFTU, 0],
		])
		constant = 0.25
		arr = ["A", "B", "C", "$a$", "$b$", "$c$"]
		DIR = [constant*UP, constant*LEFT, constant*RIGHT, 
		constant*DOWN, constant*4/5*RIGHT+constant*3/5*UP, constant*24/25*LEFT+constant*7/25*UP]
		tri = Polygon(*RIGHTPOINTS[[0, 1, 2]], color = WHITE)
		values = []
		arcradius = 0.4
		angle = Arc(radius = arcradius, angle = np.arcsin(4/5)).move_to(RIGHTPOINTS[2]).rotate(PI-np.arcsin(4/5)).shift(arcradius*4/5*LEFT+arcradius*2/5*UP)
		for i in range(3):
			values.append(TextMobject(arr[i]).move_to(RIGHTPOINTS[i]).shift(DIR[i]))
		for i in range(3):
			values.append(TextMobject(arr[3+i]).move_to((RIGHTPOINTS[(i+1)%3]+RIGHTPOINTS[(i+2)%3])/2).shift(DIR[3+i]))
		for i in range(3):
			values[i].scale(1)
		for i in range(3, 6):
			values[i].scale(1)
		formula = TexMobject("A", "=", "\\sqrt{", "s", "\\left(", "s", "-", "a\\right)", "\\left(", "s", "-", "b\\right)", "\\left(", "s", "-", "c\\right))}").scale(1.5).move_to([0, -3, 0])
		movetriangle = [-RIGHTSHIFTR-2*RIGHTSCALE, 1.5, 0]
		for i in range(6):
			values[i].shift(movetriangle)
			self.add(values[i])
		tri.shift(movetriangle)
		self.add(tri)
		angle.shift(movetriangle)
		self.add(angle)
		rect = SurroundingRectangle(formula, color = YELLOW)
		self.add(formula)
		self.play(ShowCreation(rect), run_time = 2)
		self.wait()
		highlight = formula.copy()
		changes = [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15]]
		colorarr = [RED, GREEN, BLUE]
		for i in range(3):
			for j in range(len(changes[i])):
				highlight[changes[i][j]].set_color(colorarr[i])
		self.play(Transform(formula, highlight))
		v_group = [VGroup(), VGroup(), VGroup()]
		self.wait()
		for i in range(3):
			for j in range(len(changes[i])):
				v_group[i].add(formula[changes[i][j]])
		self.play(*[WiggleOutThenIn(v_group[i]) for i in range(3)])
		self.wait()
		self.play(WiggleOutThenIn(formula[4]))
		self.wait()


class DrawRadii(Scene):
	def construct(self):
		triangle = Polygon(*POINTS[[0, 1, 2]], color = WHITE)
		circle = Circle(color = WHITE, radius = 4*POINTSSCALE).move_to(POINTS[3])
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP]
		MULTIPLIER = [1.5, 3, 3]
		arr = ["A", "B", "C", "$s-a$", "$s-b$", "$s-c$"]
		constant = 0.15
		MOVE = [constant*LEFT, constant*3/5*RIGHT+constant*4/5*DOWN, constant*12/13*UP+constant*5/13*RIGHT, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		labels = []
		radius = []
		v_group = []
		for i  in range(4):
			v_group.append(VGroup())
		for i in range(3):
			labels.append(TextMobject(arr[i]).move_to(POINTS[i]).shift(DIR[i]*1.5))
			labels.append(TextMobject("$r$").move_to((POINTS[3]+POINTS[4+i])/2).shift(MOVE[i]*2))
			radius.append(Line(POINTS[3], POINTS[4+i]))
		for i in range(3):
			labels.append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS[i%3]+POINTS[(i+1)%3+4])/2).shift(DIR[(i+1)%3+3]*MULTIPLIER[(i+1)%3]))
			labels.append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS[i%3]+POINTS[(i+2)%3+4])/2).shift(DIR[(i+2)%3+3]*MULTIPLIER[(i+2)%3]))
		self.add(triangle, circle)
		for i in range(3):
			self.add(radius[i])
		for i in range(12):
			self.add(labels[i])
		tangents = []
		for i in range(3):
			tangents.append(Line(POINTS[i], POINTS[(i+1)%3+4], color = COLOR[i]))
			tangents.append(Line(POINTS[i], POINTS[(i+2)%3+4], color = COLOR[i]))
		for i in range(6):
			self.add(tangents[i])
		self.wait()
		segments = []
		for i in range(3):
			segments.append(Line(POINTS[3], POINTS[i], color = YELLOW))
		self.play(ShowCreation(segments[0]), ShowCreation(segments[1]), ShowCreation(segments[2]), run_time = 2)
		self.wait(2)
		self.play(
			WiggleOutThenIn(labels[9]),
			WiggleOutThenIn(labels[10]),
			run_time = 2,
		)
		self.wait(3)
		self.play(
			WiggleOutThenIn(labels[6]),
			WiggleOutThenIn(labels[7]),
			run_time = 2,
		)
		self.wait()
		similar = Polygon(*POINTS[[0, 3, 5]], color = PURPLE_A, fill_color = PURPLE_A, fill_opacity = 0.5)
		self.play(ShowCreation(similar), run_time = 2)
		self.wait()
		self.play(FadeOut(similar), run_time = 2)
		self.wait()


class DrawSimilarTriangle(Scene):
	def construct(self):
		triangle = [Polygon(*POINTS[[0, 1, 2]], color = WHITE), Polygon(*POINTS0[[0, 1, 2]], color = WHITE), Polygon(*POINTS0[[1, 2, 7]], color = PURPLE_A), Polygon(*POINTS0[[0, 5, 3]], color = PURPLE_A)]
		circle = [Circle(color = WHITE, radius = 4*POINTSSCALE).move_to(POINTS[3]), Circle(color = WHITE, radius = 4*transform[2]).move_to(POINTS0[3])]
		DIR = [0.25*UP, 0.25*LEFT, 0.25*RIGHT, 0.25*DOWN, 0.2*RIGHT+0.15*UP, 0.24*LEFT+0.07*UP, 0.24*UP+0.07*RIGHT]
		MULTIPLIER = [1.5, 3, 3]
		arr = ["A", "B", "C", "$s-a$", "$s-b$", "$s-c$", "D", "E", "F", "I"]
		constant = 0.15
		MOVE = [constant*LEFT, constant*3/5*RIGHT+constant*4/5*DOWN, constant*12/13*UP+constant*5/13*RIGHT, 
		constant*63/65*RIGHT+constant*8/65*UP, constant*33/65*LEFT+constant*56/65*DOWN, constant*33/65*LEFT+constant*56/65*UP]
		labels = [[], []]
		radius = [[], []]
		v_group = []
		for i  in range(4):
			v_group.append(VGroup())
		for i in range(3):
			labels[0].append(TextMobject(arr[i]).move_to(POINTS[i]).shift(DIR[i]*1.5))
			labels[0].append(TextMobject("$r$").move_to((POINTS[3]+POINTS[4+i])/2).shift(MOVE[i]*2))
			radius[0].append(Line(POINTS[3], POINTS[4+i]))
			labels[1].append(TextMobject(arr[i]).move_to(POINTS0[i]).shift(DIR[i]*1.5*transform[2]/POINTSSCALE).scale(transform[2]/POINTSSCALE))
			labels[1].append(TextMobject("$r$").move_to((POINTS0[3]+POINTS0[4+i])/2).shift(MOVE[i]*2*transform[2]/POINTSSCALE).scale(transform[2]/POINTSSCALE))
			radius[1].append(Line(POINTS0[3], POINTS0[4+i]))
		for i in range(3):
			labels[0].append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS[i%3]+POINTS[(i+1)%3+4])/2).shift(DIR[(i+1)%3+3]*MULTIPLIER[(i+1)%3]))
			labels[0].append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS[i%3]+POINTS[(i+2)%3+4])/2).shift(DIR[(i+2)%3+3]*MULTIPLIER[(i+2)%3]))
			labels[1].append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS0[i%3]+POINTS0[(i+1)%3+4])/2).shift(DIR[(i+1)%3+3]*MULTIPLIER[(i+1)%3]*transform[2]/POINTSSCALE).scale(transform[2]/POINTSSCALE))
			labels[1].append(TextMobject(arr[3+i], color = COLOR[i+3]).move_to((POINTS0[i%3]+POINTS0[(i+2)%3+4])/2).shift(DIR[(i+2)%3+3]*MULTIPLIER[(i+2)%3]*transform[2]/POINTSSCALE).scale(transform[2]/POINTSSCALE))
		for i in range(4):
			labels[0].append(TextMobject(arr[6+i]).move_to(POINTS[3+(i+1)%4]).shift(DIR[3+i]*1.5))
			labels[1].append(TextMobject(arr[6+i]).move_to(POINTS0[3+(i+1)%4]).shift(DIR[3+i]*1.5*transform[2]/POINTSSCALE).scale(transform[2]/POINTSSCALE))
		self.add(triangle[0], circle[0])
		for i in range(3):
			self.add(radius[0][i])
		for i in range(12):
			self.add(labels[0][i])
		tangents = [[], []]
		for i in range(3):
			tangents[0].append(Line(POINTS[i], POINTS[(i+1)%3+4], color = COLOR[i]))
			tangents[0].append(Line(POINTS[i], POINTS[(i+2)%3+4], color = COLOR[i]))
			tangents[1].append(Line(POINTS0[i], POINTS0[(i+1)%3+4], color = COLOR[i]))
			tangents[1].append(Line(POINTS0[i], POINTS0[(i+2)%3+4], color = COLOR[i]))
		for i in range(6):
			self.add(tangents[0][i])
		segments = [[], []]
		for i in range(3):
			segments[0].append(Line(POINTS[3], POINTS[i], color = YELLOW))
			segments[1].append(Line(POINTS0[3], POINTS0[i], color = YELLOW))
			self.add(segments[0][i])
		self.wait()	
		self.play(FadeIn(labels[0][12]), FadeIn(labels[0][13]), FadeIn(labels[0][14]), FadeIn(labels[0][15]))
		v_group[0].add(triangle[0], circle[0])
		v_group[1].add(triangle[1], circle[1])
		for i in range(16):
			v_group[0].add(labels[0][i])
			v_group[1].add(labels[1][i])
		for i in range(3):
			v_group[0].add(radius[0][i])
			v_group[1].add(radius[1][i])
		for i in range(6):
			v_group[0].add(tangents[0][i])
			v_group[1].add(tangents[1][i])
		for i in range(3):
			v_group[0].add(segments[0][i])
			v_group[1].add(segments[1][i])
		self.play(
			Transform(v_group[0], v_group[1])
		)
		self.wait()
		labels[0].append(TextMobject("H").move_to(POINTS0[7]).scale(transform[2]/POINTSSCALE).shift(transform[2]/POINTSSCALE*1.5*0.25*RIGHT))
		labels[0].append(TextMobject("$a$", color = PURPLE_A).move_to((POINTS0[1]+POINTS0[2])/2).shift(transform[2]/POINTSSCALE*1.5*0.25*DOWN+0.25*RIGHT).scale(transform[2]/POINTSSCALE))
		labels[0].append(TextMobject("$h$", color = PURPLE_A).move_to((POINTS0[2]+POINTS0[7])/2).shift(transform[2]/POINTSSCALE*1.5*0.25*RIGHT).scale(transform[2]/POINTSSCALE))
		labels[0].append(TextMobject("$\\frac{ra}{s-a}$", color = PURPLE_A).move_to((POINTS0[2]+POINTS0[7])/2).shift(transform[2]/POINTSSCALE*2*0.25*RIGHT+3*LEFT).scale(transform[2]/POINTSSCALE))
		labels[0].append(TextMobject("G").move_to(POINTS0[8]).shift(3*LEFT+(0.25*DOWN+0.15*LEFT)*transform[2]/POINTSSCALE*1.5).scale(transform[2]/POINTSSCALE))
		labels[0].append(TextMobject("$\\frac{(s-a)(s-c)}{s}$").move_to((POINTS0[8]+POINTS0[4])/2).shift(3*LEFT+(0.25*DOWN)*transform[2]/POINTSSCALE*1.5+0.5*DOWN).scale(transform[2]/POINTSSCALE))
		arrow = Vector(UP*0.3).move_to(labels[0][21]).shift(0.5*UP)
		self.play(ShowCreation(triangle[3]))
		self.play(
			Transform(triangle[3], triangle[2]),
			labels[0][9].shift, 0.2*RIGHT,
			labels[0][10].shift, 0.25*RIGHT,
			run_time = 3,
		)
		self.play(FadeIn(labels[0][16]))
		self.add(triangle[2])
		self.remove(triangle[3])
		self.wait()
		self.play(
			FadeOut(labels[0][9]),
			FadeOut(labels[0][10]),
			FadeIn(labels[0][17]),
		)
		self.wait()
		self.play(FadeIn(labels[0][18]))
		self.wait()
		v_group[2].add(triangle[0], circle[0])
		for i in range(19):
			if i != 9 and i != 10:
				v_group[2].add(labels[0][i])
		for i in range(3):
			v_group[2].add(radius[0][i])
		for i in range(6):
			v_group[2].add(tangents[0][i])
		for i in range(3):
			v_group[2].add(segments[0][i])
		v_group[2].add(triangle[2])
		self.play(
			v_group[2].shift, 3*LEFT,
			run_time = 1.5,
		)
		LOC = [3, 2, 0]
		eqn = [
			TexMobject("{h", "\\over", "a}", "=", "{r", "\\over", "s-a}").move_to(LOC).scale(0.8),
			TexMobject("h", "=", "{r", "a", "\\over", "s-a").move_to(LOC).scale(0.8),
			TexMobject("{CG", "\\over", "DG}", "=", "{\\frac{ra}{s-a}", "\\over", "r}").move_to(LOC).scale(0.8),
			TexMobject("{CG", "\\over", "DG}", "=", "{\\frac{a}{s-a}").move_to(LOC).scale(0.8),
			TexMobject("{CG", "\\over", "DG}", "+", "1", "=", "\\frac{a}{s-a}", "+", "1").move_to(LOC+DOWN+0.1*RIGHT).scale(0.8),
			TexMobject("{CG+DG", "\\over", "DG}", "=", "{a", "+", "s-a", "\\over", "s-a}").move_to(LOC+DOWN+0.1*LEFT).scale(0.8),
			TexMobject("{CD", "\\over", "DG}", "=", "{s", "\\over", "s-a}").move_to(LOC+DOWN+0.1*RIGHT).scale(0.8),
			TexMobject("{s-c", "\\over", "DG}", "=", "{s", "\\over", "s-a}").move_to(LOC+DOWN).scale(0.8),
			TexMobject("DG", "=", "{(s-a)", "(s-c)", "\\over", "s}").move_to(LOC+2*DOWN+0.8*RIGHT).scale(0.8),
		]
		colorarray = [
			[PURPLE_A, WHITE, PURPLE_A, WHITE, WHITE, WHITE, RED_D],
			[PURPLE_A, WHITE, WHITE, PURPLE_A, WHITE, RED_D],
			[WHITE, WHITE, WHITE, WHITE, PURPLE_A, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, PURPLE_A],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, PURPLE_A, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, PURPLE_A, WHITE, WHITE, WHITE, PURPLE_A],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
		]
		for i in range(len(eqn)):
			for j in range(len(eqn[i])):
				eqn[i][j].set_color(colorarray[i][j])
		eqn[1][1].align_to(eqn[0][3], LEFT)
		alignequals = [3, 5, 3, 3, 3, 1]
		for i in range(3, 9):
			eqn[i][alignequals[i-3]].align_to(eqn[2][3], LEFT)
			eqn[i][alignequals[i-3]].align_to(eqn[2][3], DOWN)
			if i != 3:
				eqn[i][alignequals[i-3]].shift(DOWN)
			if i == 8:
				eqn[i][alignequals[i-3]].shift(DOWN)
		for i in range(3):
			eqn[3][i].align_to(eqn[2][i], UP)
			eqn[3][i].align_to(eqn[2][i], LEFT)
		for i in range(3):
			eqn[7][i+4].align_to(eqn[6][i+4], DOWN)
			eqn[7][i+4].align_to(eqn[6][i+4], LEFT)
		eqn[7][2].align_to(eqn[6][2], DOWN)
		eqn[7][1].align_to(eqn[6][1], DOWN)
		eqn[7][0].align_to(eqn[6][0], DOWN)
		self.play(
			Transform(labels[0][18], eqn[0][0]),
			FadeIn(eqn[0][1]),
			FadeIn(eqn[0][3]),
			FadeIn(eqn[0][5]),
			Transform(labels[0][3], eqn[0][4]),
			labels[0][17].move_to, eqn[0][2],
			labels[0][17].scale, 0.8/transform[2]*POINTSSCALE,
			labels[0][6].move_to, eqn[0][6],
			labels[0][6].scale, 0.8/transform[2]*POINTSSCALE,
			run_time = 2,
		)
		self.remove(labels[0][17], labels[0][6], labels[0][18], labels[0][3], labels[0][6], eqn[0][1], eqn[0][3], eqn[0][5])
		self.add(eqn[0])
		self.wait()
		self.play(Transform(eqn[0], eqn[1]))
		self.wait()
		labels[0][17] = TextMobject("$a$", color = PURPLE_A).move_to((POINTS0[1]+POINTS0[2])/2).shift(transform[2]/POINTSSCALE*1.5*0.25*DOWN+0.25*RIGHT+3*LEFT).scale(transform[2]/POINTSSCALE)
		labels[0][3] = TextMobject("$r$").move_to((POINTS0[3]+POINTS0[5])/2).shift(transform[2]/POINTSSCALE*MOVE[1]*2+3*LEFT).scale(transform[2]/POINTSSCALE)
		labels[0][6] = TextMobject("$s-a$", color = RED_D).move_to((POINTS0[0]+POINTS0[5])/2).shift(transform[2]/POINTSSCALE*DIR[4]*MULTIPLIER[1]+3*LEFT).scale(transform[2]/POINTSSCALE)
		self.play(FadeIn(labels[0][19]), FadeIn(labels[0][17]), FadeIn(labels[0][3]), FadeIn(labels[0][6]))
		self.wait()
		line = [
			Line(POINTS0[3]+3*LEFT, POINTS0[7]+3*LEFT, color = ORANGE), 
			Line(POINTS0[3]+3*LEFT, POINTS0[1]+3*LEFT),
			Line(POINTS0[3]+3*LEFT, POINTS0[7]+3*LEFT),
		]
		line[1].set_color(color = [BLUE, RED])
		line[2].set_color(color = [RED, BLUE])
		line[1].set_stroke(width = 6)
		line[2].set_stroke(width = 6)
		self.play(ShowCreation(line[0]))
		self.wait()
		labels[0][9].shift(3*LEFT)
		labels[0][10].shift(3*LEFT)
		self.play(FadeIn(labels[0][20]), FadeOut(labels[0][17]), FadeIn(labels[0][9]), FadeIn(labels[0][10]))
		self.wait()
		triangle.append(Polygon(*POINTS0[[3, 4, 8]], color = ORANGE, fill_color = ORANGE, fill_opacity = 0.5).shift(3*LEFT))
		triangle.append(Polygon(*POINTS0[[7, 2, 8]], color = ORANGE, fill_color = ORANGE, fill_opacity = 0.5).shift(3*LEFT))
		self.play(FadeOut(eqn[0]), FadeIn(triangle[4]))
		self.play(Transform(triangle[4], triangle[5]))
		self.play(FadeOut(triangle[4]))
		self.wait()
		self.play(Write(eqn[2]))
		self.wait()
		self.play(FadeOut(eqn[2]), FadeIn(eqn[3]))
		self.wait()
		self.play(Write(eqn[4]))
		self.wait()
		self.play(Transform(eqn[4], eqn[5]))
		self.wait()
		self.play(Transform(eqn[4], eqn[6]))
		self.wait()
		self.play(Transform(eqn[4], eqn[7]))
		self.wait()
		self.play(Write(eqn[8]))
		self.wait()
		self.play(Write(labels[0][21]), ShowCreation(arrow))
		self.wait()
		self.play(WiggleOutThenIn(labels[0][9]))
		self.wait()
		BIG = Polygon(*POINTS1[[1, 3, 8]], color = WHITE, fill_opacity = 0.2, fill_color = WHITE)
		self.play(FadeIn(BIG), run_time = 0.5)
		self.wait()
		self.play(WiggleOutThenIn(labels[0][9]), WiggleOutThenIn(labels[0][21]))
		self.play(FadeOut(BIG), run_time = 0.5)
		self.wait()
		self.play(WiggleOutThenIn(labels[0][1]))
		self.wait()
		self.play(ShowCreation(line[1]), ShowCreation(line[2]))
		self.wait(2)
		#begin of ShowRightAngle
		self.play(FadeOut(line[1]), FadeOut(line[2]))
		triangle[3] = Polygon(*POINTS1[[0, 5, 3]], color = PURPLE_A)
		self.play(Transform(triangle[3], triangle[2]))
		self.remove(triangle[3])
		angleradius = 0.3
		alpha = np.arctan(4/7)
		beta = np.arctan(4/6)
		gamma = np.arctan(4/8)
		tempangle = (get_angle(POINTS1[3], POINTS1[1])+get_angle(POINTS1[3], POINTS1[7]))/2
		mobjects = [
			Square().scale(0.1).move_to(POINTS1[2]+0.1*DOWN+0.1*LEFT),
			ArcBetweenPoints(angle = alpha, start_point = POINTS1[1]+angleradius*(np.sin(alpha)*DOWN+np.cos(alpha)*RIGHT), end_point = POINTS1[1]+angleradius*RIGHT, color = RED),
			ArcBetweenPoints(angle = -beta, start_point = POINTS1[1]+angleradius*(np.sin(beta)*UP+np.cos(beta)*RIGHT), end_point = POINTS1[1]+angleradius*RIGHT, color = GREEN),
			ArcBetweenPoints(angle = gamma, start_point = POINTS1[2]+angleradius*(np.sin(gamma)*UP+np.cos(gamma)*LEFT), end_point = POINTS1[2]+angleradius*LEFT, color = BLUE),
			Square().scale(0.1).move_to(POINTS1[3]).rotate(np.arctan(4/6)).shift(0.1*np.sqrt(2)*(np.cos(tempangle)*LEFT+np.sin(tempangle)*DOWN))
		]
		self.play(FadeIn(mobjects[0]), FadeIn(mobjects[1]))
		for e in eqn:
			self.remove(e)
		self.wait()
		LOC = [2, 2.5, 0]
		equations = [
			TexMobject("\\angle{CBH}", "=", "{\\angle{A}", "\\over", "2}").move_to(LOC+0.5*RIGHT),
			TexMobject("\\angle{BCH}", "=", "90^\\circ").move_to(LOC+DOWN),
			TexMobject("\\angle{IBC}", "=", "{\\angle{B}", "\\over", "2}").move_to(LOC+2*DOWN),
			TexMobject("\\angle{ICB}", "=", "{\\angle{C}", "\\over", "2}").move_to(LOC+3*DOWN),
			TexMobject("\\angle{IBH}+\\angle{ICH}", "=", "90^\\circ", "+", "{\\angle{A}", "+", "\\angle{B}", "+", "\\angle{C}", "\\over", "2}").move_to(LOC+4*DOWN),
			TexMobject("\\angle{IBH}+\\angle{ICH}", "=", "90^\\circ", "+", "{180^\\circ", "\\over", "2}").move_to(LOC+4*DOWN),
			TexMobject("\\angle{IBH}+\\angle{ICH}", "=", "90^\\circ", "+", "90^\\circ").move_to(LOC+4*DOWN),
			TexMobject("\\angle{IBH}+\\angle{ICH}", "=", "180^\\circ").move_to(LOC+4*DOWN),
			TexMobject("r", "=", "\\sqrt{", "\\frac{(s-a)(s-c)}{s}", "(s-b)", ")}").move_to(LOC+DOWN+RIGHT),
			TexMobject("r", "=", "\\sqrt{\\frac{(s-a)(s-b)(s-c)}{s}}").move_to(LOC+DOWN),
			TexMobject("A", "=", "rs").move_to(LOC+2*DOWN),
			TexMobject("A", "=", "\\sqrt{s(s-a)(s-b)(s-c)}").move_to(LOC+3*DOWN),
		]
		colorarr = [
			[RED, WHITE, RED, WHITE, WHITE],
			[WHITE, WHITE, WHITE],
			[GREEN, WHITE, GREEN, WHITE, WHITE],
			[BLUE, WHITE, BLUE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, RED, WHITE, GREEN, WHITE, BLUE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
		]
		for i in range(len(equations)):
			equations[i].scale(0.8)
			for j in range(len(equations[i])):
				equations[i][j].set_color(colorarr[i][j])
		for i in range(1, 8):
			temp = equations[0][1].get_center()[0]-equations[i][1].get_center()[0]
			equations[i].shift(temp*RIGHT)
		for i in range(9, 12):
			equations[i].shift(RIGHT*(equations[8][1].get_center()[0]-equations[i][1].get_center()[0]))
		self.play(FadeIn(equations[0]), FadeIn(equations[1]))
		self.wait()
		self.play(FadeIn(mobjects[2]), FadeIn(mobjects[3]))
		self.wait()
		self.play(FadeIn(equations[2]))
		self.play(FadeIn(equations[3]))
		self.wait()
		self.play(FadeIn(equations[4]))
		self.wait()
		changes = [
			[[(4, 5, 6, 7, 8, 9, 10), (4, 4, 4, 4, 4, 5, 6)]],
			[[(4, 5, 6), (4, 4, 4)]],
			[[(2, 3, 4), (2, 2, 2)]],
			[[(0, 1, 2, 3, 4), (0, 1, 2, 2, 2)]]
		]
		for pre_ind, post_ind in changes[0]:
			self.play(*[ReplacementTransform(equations[4][i], equations[5][j]) for i,j in zip(pre_ind, post_ind)])
		self.wait()
		for pre_ind, post_ind in changes[1]:
			self.play(*[ReplacementTransform(equations[5][i], equations[6][j]) for i,j in zip(pre_ind, post_ind)])
		self.wait()
		self.remove(equations[4][2], equations[4][3], equations[5][2], equations[5][3])
		for pre_ind, post_ind in changes[2]:
			self.play(*[ReplacementTransform(equations[6][i], equations[7][j]) for i,j in zip(pre_ind, post_ind)])
		self.wait()
		cycquad = Polygon(*POINTS1[[1, 3, 2, 7]], color = BLUE)
		self.play(ShowCreation(cycquad), run_time = 3)
		self.wait()
		self.play(FadeIn(mobjects[4]))
		self.play(ShowCreation(BIG), run_time = 3)
		self.wait()
		self.play(WiggleOutThenIn(labels[0][9]))
		self.play(WiggleOutThenIn(labels[0][21]))
		self.play(WiggleOutThenIn(labels[0][1]))
		self.play(FadeOut(BIG))
		self.wait()
		#BEGIN OF FindInRadius
		for i in range(4, 7):
			self.remove(equations[i][0], equations[i][1])
		self.play(*[FadeOut(equations[i]) for i in range(4)], FadeOut(equations[7]))	
		self.play(ShowCreation(BIG), run_time = 3)
		self.wait()
		self.play(Write(equations[8]))
		self.wait()
		self.play(FadeOut(equations[8]), FadeIn(equations[9]))
		self.wait(2)
		self.play(Write(equations[10]), run_time = 1.5)
		self.play(Write(equations[11]), run_time = 1.5)
		surroundingrectangle = SurroundingRectangle(equations[11], color = YELLOW)
		self.play(ShowCreation(surroundingrectangle), run_time = 2)
		self.wait()


class CyclicQuad(Scene):
	def construct(self):
		quad = Polygon(*CYCLICQUAD[[0, 1, 2, 3]], color = WHITE)
		circumcircle = Circle(radius = 5*quadtransform[2], color = WHITE).move_to(CYCLICQUAD[4])
		angleradius = 0.25
		labelshift = 0.5
		alpha = ArcBetweenPoints(angle = PI/2+np.arctan(1/7)+np.arctan(2/11), start_point = CYCLICQUAD[0]+angleradius*7/np.sqrt(50)*DOWN+angleradius/np.sqrt(50)*LEFT, end_point = CYCLICQUAD[0]+angleradius*2/np.sqrt(125)*UP+angleradius*11/np.sqrt(125)*RIGHT)
		beta = ArcBetweenPoints(angle = np.arctan(3), start_point = CYCLICQUAD[2]+angleradius*LEFT, end_point = CYCLICQUAD[2]+3*angleradius/np.sqrt(10)*UP+angleradius/np.sqrt(10)*LEFT).rotate(PI)
		anglealpha = np.arctan(3)
		anglebeta = PI/2+np.arctan(1/7)+np.arctan(2/11)
		theta = anglebeta/2-np.arctan(2/11)
		anglelabels = [TexMobject("\\beta").move_to(CYCLICQUAD[2]).shift(labelshift*(np.sin(anglealpha/2)*UP+np.cos(anglealpha/2)*LEFT)), TexMobject("\\alpha").move_to(CYCLICQUAD[0]).shift(labelshift*(np.sin(theta)*DOWN+np.cos(theta)*RIGHT))]
		anglelabels[0].set_color(BLUE)
		anglelabels[1].set_color(RED)
		alpha.set_color(RED)
		beta.set_color(BLUE)
		self.play(ShowCreation(quad), run_time = 3)
		self.wait()
		self.play(GrowFromCenter(alpha), GrowFromCenter(beta), Write(anglelabels[0]), Write(anglelabels[1]))
		self.wait()
		LOC = [4.5, 0, 0]
		eqn = TexMobject("\\alpha", "+", "\\beta", "=", "180^\\circ").move_to(LOC)
		colorarray = [RED, WHITE, BLUE, WHITE, WHITE]
		for i in range(len(eqn)):
			eqn[i].set_color(colorarray[i])
		for i in range(2):
			anglelabels.append(anglelabels[i].copy())
		self.play(anglelabels[3].move_to, eqn[0].get_center(), run_time = 1.5)
		self.play(Write(eqn[1]), run_time = 0.5)
		self.play(anglelabels[2].move_to, eqn[2].get_center(), run_time = 1.5)
		self.play(Write(eqn[3:5]), run_time = 1.5)
		self.wait()
		self.play(GrowFromCenter(circumcircle), run_time = 3)
		self.wait()
		self.play(
			FadeOut(eqn), FadeOut(anglelabels[3]), FadeOut(anglelabels[2]),
			circumcircle.shift, quadtransform[0]*LEFT,
			quad.shift, quadtransform[0]*LEFT,
			alpha.shift, quadtransform[0]*LEFT,
			beta.shift, quadtransform[0]*LEFT,
			anglelabels[0].shift, quadtransform[0]*LEFT,
			anglelabels[1].shift, quadtransform[0]*LEFT,
		)
		self.wait()
		diagonal = [Line(CYCLICQUAD[5], CYCLICQUAD[7]), Line(CYCLICQUAD[8], CYCLICQUAD[6])]
		self.play(ShowCreation(diagonal[0]), ShowCreation(diagonal[1]), FadeOut(anglelabels[0]), FadeOut(anglelabels[1]), FadeOut(alpha), FadeOut(beta))
		self.wait()
		trig = [np.arctan(7), np.arctan(3), np.arctan(13/9), np.arctan(1)]
		angles = []
		anglecolors = [RED, BLUE]
		angleradius = 0.75
		for i in range(2):
			angles.append(ArcBetweenPoints(angle = trig[i%2]-trig[2+i%2], start_point = CYCLICQUAD[6+i%2]+angleradius*(np.cos(trig[i%2])*RIGHT*((-1)**i)+np.sin(trig[i%2])*UP), end_point = CYCLICQUAD[6+i%2]+angleradius*(np.cos(trig[2+i%2])*RIGHT*((-1)**i)+np.sin(trig[2+i%2])*UP)))
			angles[i].set_color(anglecolors[i])
		angles[0].rotate(PI)
		angles.append(Arc(radius = 5*quadtransform[5], angle = -2*(trig[0]-trig[2]), color = GREEN).rotate(angle = np.arctan(-4/3)+PI, about_point = CYCLICQUAD[9]))
		self.play(GrowFromCenter(angles[0]), GrowFromCenter(angles[1]), run_time = 0.5)
		self.play(ShowCreation(angles[2]))
		self.wait()


class InscribedAngle(Scene):
	def construct(self):
		lines = [
			Line(CYCLICQUAD[5], CYCLICQUAD[6]),
			Line(CYCLICQUAD[5], CYCLICQUAD[7]),
			Line(CYCLICQUAD[8], CYCLICQUAD[6]),
			Line(CYCLICQUAD[8], CYCLICQUAD[7]),
			Line(CYCLICQUAD[9], CYCLICQUAD[5]),
			Line(CYCLICQUAD[9], CYCLICQUAD[8]),
		]
		colorarray = [RED, BLUE, RED, BLUE, GREEN, GREEN]
		for i in range(len(lines)):
			lines[i].set_color(colorarray[i])
		lines[1].set_color(WHITE)
		lines[2].set_color(WHITE)
		quad = Polygon(*CYCLICQUAD[[5, 6, 7, 8]], color = WHITE)
		circumcircle = Circle(radius = 5*quadtransform[5], color = WHITE).move_to(CYCLICQUAD[9])
		for i in range(4):
			self.add(lines[i])
		trig = [np.arctan(7), np.arctan(3), np.arctan(13/9), np.arctan(1)]
		angles = []
		anglecolors = [RED, BLUE]
		angleradius = 0.75
		for i in range(2):
			angles.append(ArcBetweenPoints(angle = trig[i%2]-trig[2+i%2], start_point = CYCLICQUAD[6+i%2]+angleradius*(np.cos(trig[i%2])*RIGHT*((-1)**i)+np.sin(trig[i%2])*UP), end_point = CYCLICQUAD[6+i%2]+angleradius*(np.cos(trig[2+i%2])*RIGHT*((-1)**i)+np.sin(trig[2+i%2])*UP)))
			angles[i].set_color(anglecolors[i])
		angles[0].rotate(PI)
		angles.append(Arc(radius = 5*quadtransform[5], angle = -2*(trig[0]-trig[2]), color = GREEN).rotate(angle = np.arctan(-4/3)+PI, about_point = CYCLICQUAD[9]))
		self.add(circumcircle, quad, angles[0], angles[1], angles[2])
		self.wait()
		self.play(
			FadeOut(quad),
			lines[1].set_color, colorarray[1],
			lines[2].set_color, colorarray[2],
		)
		self.wait()
		dot0 = Dot().move_to(CYCLICQUAD[6]).scale(0.00001)
		dot1 = Dot().move_to(CYCLICQUAD[7]).scale(0.00001)
		group = VGroup(lines[0], lines[1], lines[2], lines[3], angles[0], angles[1])
		centralangle = [get_angle(CYCLICQUAD[5], CYCLICQUAD[9]), get_angle(CYCLICQUAD[8], CYCLICQUAD[9])]
		labelshift = 1
		theta = [
			TexMobject("\\theta").set_color(RED),
			TexMobject("\\theta").set_color(BLUE),
			TexMobject("2\\theta").set_color(GREEN).move_to(CYCLICQUAD[9]).shift(labelshift*(RIGHT*np.cos((centralangle[0]+centralangle[1])/2)+UP*np.sin((centralangle[0]+centralangle[1])/2))),
		]
		angle_group = VGroup(theta[0], theta[1])
		def update(group):
			lines[0] = Line(CYCLICQUAD[5], dot0.get_center()).set_color(colorarray[0])
			lines[1] = Line(CYCLICQUAD[5], dot1.get_center()).set_color(colorarray[1])
			lines[2] = Line(CYCLICQUAD[8], dot0.get_center()).set_color(colorarray[2])
			lines[3] = Line(CYCLICQUAD[8], dot1.get_center()).set_color(colorarray[3])
			rad = [get_angle(dot0.get_center(), CYCLICQUAD[5]), get_angle(dot1.get_center(), CYCLICQUAD[5]), get_angle(dot0.get_center(), CYCLICQUAD[8]), get_angle(dot1.get_center(), CYCLICQUAD[8])]
			angles[0] = ArcBetweenPoints(angle = rad[2]-rad[0], start_point = dot0.get_center()+angleradius*(np.cos(rad[0])*RIGHT+np.sin(rad[0])*UP), end_point = dot0.get_center()+angleradius*(np.cos(rad[2])*RIGHT+np.sin(rad[2])*UP)).set_color(RED)
			angles[1] = ArcBetweenPoints(angle = rad[3]-rad[1], start_point = dot1.get_center()+angleradius*(np.cos(rad[1])*RIGHT+np.sin(rad[1])*UP), end_point = dot1.get_center()+angleradius*(np.cos(rad[3])*RIGHT+np.sin(rad[3])*UP)).set_color(BLUE)
			new_group = VGroup(lines[0], lines[1], lines[2], lines[3], angles[0], angles[1])
			group.become(new_group)
			return group
		labelshift = 1.25
		def update_angles(angle_group):
			rad = [get_angle(dot0.get_center(), CYCLICQUAD[5]), get_angle(dot1.get_center(), CYCLICQUAD[5]), get_angle(dot0.get_center(), CYCLICQUAD[8]), get_angle(dot1.get_center(), CYCLICQUAD[8])]
			theta[0] = TexMobject("\\theta").set_color(RED).move_to(dot0.get_center()).shift(labelshift*(RIGHT*np.cos((rad[0]+rad[2])/2)+UP*np.sin((rad[0]+rad[2])/2)))
			theta[1] = TexMobject("\\theta").set_color(BLUE).move_to(dot1.get_center()).shift(labelshift*(RIGHT*np.cos((rad[1]+rad[3])/2)+UP*np.sin((rad[1]+rad[3])/2)))
			new_angle_group = VGroup(theta[0], theta[1])
			angle_group.become(new_angle_group)
			return angle_group
		self.play(
			Rotating(dot0, radians = PI/2+np.arctan(4/3), about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 1.5),
			UpdateFromFunc(group, update)
		)
		self.play(
			Rotating(dot0, radians = -3*PI/4, about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 2),
			UpdateFromFunc(group, update)
		)
		rad = [get_angle(dot0.get_center(), CYCLICQUAD[5]), get_angle(dot1.get_center(), CYCLICQUAD[5]), get_angle(dot0.get_center(), CYCLICQUAD[8]), get_angle(dot1.get_center(), CYCLICQUAD[8])]
		theta[0] = TexMobject("\\theta").set_color(RED).move_to(dot0.get_center()).shift(labelshift*(RIGHT*np.cos((rad[0]+rad[2])/2)+UP*np.sin((rad[0]+rad[2])/2)))
		theta[1] = TexMobject("\\theta").set_color(BLUE).move_to(dot1.get_center()).shift(labelshift*(RIGHT*np.cos((rad[1]+rad[3])/2)+UP*np.sin((rad[1]+rad[3])/2)))
		self.play(FadeIn(theta[0]), FadeIn(theta[1]))
		self.remove(theta[0], theta[1])
		self.play(
			Rotating(dot0, radians = 3*PI/5, about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 2.5),
			Rotating(dot1, radians = -3*PI/4, about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 2.5),
			UpdateFromFunc(group, update),
			UpdateFromFunc(angle_group, update_angles),
		)
		self.play(
			ShowCreation(lines[4]),
			ShowCreation(lines[5]),
			FadeIn(theta[2]),
		)
		self.wait()
		self.play(
			Rotating(dot0, radians = -3*PI/5+3*PI/4-PI/2-np.arctan(4/3), about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 2.5),
			Rotating(dot1, radians = 3*PI/4, about_point = CYCLICQUAD[9], rate_func = smooth, run_time = 2.5),
			UpdateFromFunc(group, update),
			UpdateFromFunc(angle_group, update_angles),
		)
		self.wait()


class ZoomOnRightTriangle(Scene):
	def construct(self):
		triangle = [Polygon(*RIGHTTRIANGLE[[1, 2, 3]], color = WHITE), Polygon(*RIGHTTRIANGLE[[2, 0, 1]], color = RED, fill_color = RED, fill_opacity = 0.5), Polygon(*RIGHTTRIANGLE[[1, 0, 3]], color = BLUE, fill_color = BLUE, fill_opacity = 0.5)]
		alt = Line(RIGHTTRIANGLE[1], RIGHTTRIANGLE[0])
		bisect = (get_angle(RIGHTTRIANGLE[1], RIGHTTRIANGLE[2])+get_angle(RIGHTTRIANGLE[1], RIGHTTRIANGLE[3]))/2
		square = [
			Square().scale(0.2).move_to(RIGHTTRIANGLE[1]).rotate(get_angle(RIGHTTRIANGLE[1], RIGHTTRIANGLE[3])).shift(0.2*(np.cos(bisect)*LEFT+np.sin(bisect)*DOWN)*np.sqrt(2)),
			Square().scale(0.2).move_to(RIGHTTRIANGLE[0]).shift(0.2*(UP+LEFT))
		]
		labels = [
			TexMobject("a", color = RED).move_to((RIGHTTRIANGLE[2]+RIGHTTRIANGLE[0])/2).shift(0.3*DOWN),
			TexMobject("b", color = BLUE).move_to((RIGHTTRIANGLE[3]+RIGHTTRIANGLE[0])/2).shift(0.3*DOWN),
			TexMobject("h").move_to((RIGHTTRIANGLE[1]+RIGHTTRIANGLE[0])/2).shift(0.25*LEFT),
			TexMobject("\\sqrt{", "a", "b", "b}").move_to((RIGHTTRIANGLE[1]+RIGHTTRIANGLE[0])/2).shift(0.6*LEFT),
		]
		LOC = [-4.5, 2.5, 0]
		eqn = [
			TexMobject("{h", "\\over", "a}", "=", "{b", "\\over", "h}").move_to(LOC),
			TexMobject("h", "^2", "=", "a", "b").move_to(LOC+DOWN),
			TexMobject("h", "=", "\\sqrt{", "a", "b", "b}").move_to(LOC+2*DOWN),
		]
		shiftequals = []
		for i in range(2):
			shiftequals.append(eqn[i+1][1].get_center()[0]-eqn[0][3].get_center()[0])
			# eqn[i+1].shift(shiftequals[i]*RIGHT)
		eqn[2].shift((eqn[2][1].get_center()[0]-eqn[0][3].get_center()[0])*LEFT)
		coloreqn = [
			[WHITE, WHITE, RED, WHITE, BLUE, WHITE, WHITE],
			[WHITE, WHITE, WHITE, RED, BLUE],
			[WHITE, WHITE, WHITE, WHITE, RED, BLUE],
		]
		for i in range(len(eqn)):
			for j in range(len(eqn[i])):
				eqn[i][j].set_color(coloreqn[i][j])
		self.play(ShowCreation(triangle[0]), run_time = 3)
		self.play(ShowCreation(alt), FadeIn(square[0]), run_time = 1.5)
		self.play(FadeIn(square[1]))
		self.wait()
		self.play(ShowCreation(triangle[1]), run_time = 2)
		self.play(Transform(triangle[1].copy(), triangle[2]), run_time = 3)
		self.wait()
		self.play(FadeInFromDown(labels[0]), FadeInFromDown(labels[1]))
		self.play(FadeIn(labels[2]))
		self.wait()
		for i in range(3):
			labels.append(labels[i].copy())
		labels.append(labels[2].copy())
		self.play(
			labels[4].move_to, eqn[0][2],
			labels[5].move_to, eqn[0][4],
			labels[6].move_to, eqn[0][0],
			labels[7].move_to, eqn[0][6],
			FadeIn(eqn[0][1]),
			FadeIn(eqn[0][3]),
			FadeIn(eqn[0][5]),
			run_time = 2,
		)
		changes = [
			[[(0, 2, 4, 6, 3), (0, 3, 4, 0, 2)]],
			[[(0, 1, 2, 3, 4, 1), (0, 2, 1, 4, 5, 3)]]
		]
		self.wait()
		for pre_ind, post_ind in changes[0]:
			self.play(*[Transform(eqn[0][i].copy(), eqn[1][j]) for i,j in zip(pre_ind, post_ind)], FadeIn(eqn[1][1]))
		self.wait()
		for pre_ind, post_ind in changes[1]:
			self.play(*[Transform(eqn[1][i].copy(), eqn[2][j]) for i,j in zip(pre_ind, post_ind)])
		self.wait()
		self.play(Transform(eqn[2][2:6], labels[3][0:4]), FadeOut(labels[2]))
		self.wait()


class ProofConclusion(Scene):
	def construct(self):
		VERTEX = np.array([
			[-3, 3, 0],
			[-5.5, -3, 0],
			[1.5, -3, 0],
		])
		triangle = Polygon(*VERTEX[[0, 1, 2]], color = WHITE)
		self.play(ShowCreation(triangle), run_time = 3)
		mobjects = []
		lengths = []
		coords = [VERTEX[0], VERTEX[1], VERTEX[2]]
		colorarray = [RED, GREEN, BLUE]
		for i in range(3):
			mobjects.append(DecimalNumber(2*get_distance(coords[i], coords[(i+1)%3]), num_decimal_places = 3, background_stroke_width = 10, background_stroke_color = BLACK, color = colorarray[(i+2)%3]).move_to((VERTEX[i]+VERTEX[(i+1)%3])/2))
			lengths.append(2*get_distance(coords[i], coords[(i+1)%3]))
		for i in range(3):
			mobjects.append(Dot().move_to(VERTEX[i]).scale(0.001))
		for i in range(3):
			mobjects.append(Line(VERTEX[i], VERTEX[(i+1)%3]))
			self.add(mobjects[i+6])
		self.remove(triangle)
		self.play(*[FadeIn(mobjects[i]) for i in range(3, 6)])
		LOC = [3.5, 2, 0]
		mobjects.append(TexMobject("A", "=", "\\sqrt{s(s-", "a", ")(s-", "b", ")(s-", "c", ")").move_to(LOC))
		for i in range(3):
			mobjects[9][3+2*i].set_color(colorarray[i])
		mobjects.append(TexMobject("=").move_to(mobjects[9][1]).shift(DOWN))
		mobjects.append(DecimalNumber(get_area(lengths[0], lengths[1], lengths[2]), num_decimal_places = 3).next_to(mobjects[10], RIGHT, buff = MED_SMALL_BUFF))
		box = SurroundingRectangle(mobjects[11], color = YELLOW)
		self.play(FadeIn(mobjects[0]), FadeIn(mobjects[1]), FadeIn(mobjects[2]), FadeIn(mobjects[9]), FadeIn(mobjects[10]), FadeIn(mobjects[11]), FadeIn(box))
		group = VGroup()
		for i in range(3, 15):
			group.add(mobjects[i%12])
		group.add(box)
		def update(group):
			for i in range(3):
				lengths[i] = 2*get_distance(mobjects[i+3].get_center(), mobjects[(i+1)%3+3].get_center())
				mobjects[i+6] = Line(mobjects[i+3].get_center(), mobjects[(i+1)%3+3].get_center())
				mobjects[i] = DecimalNumber(lengths[i], num_decimal_places = 3, background_stroke_width = 10, background_stroke_color = BLACK, color = colorarray[(i+2)%3]).move_to((mobjects[i+3].get_center()+mobjects[(i+1)%3+3].get_center())/2)
			mobjects[11] = DecimalNumber(get_area(lengths[0], lengths[1], lengths[2]), num_decimal_places = 3, background_stroke_width = 10, background_stroke_color = BLACK).next_to(mobjects[10], RIGHT, buff = MED_SMALL_BUFF)
			box = SurroundingRectangle(mobjects[11], color = YELLOW)
			new_group = VGroup()
			for i in range(3, 15):
				new_group.add(mobjects[i%12])
			new_group.add(box)
			group.become(new_group)
			return group
		for i in range(3, 15):
			self.add(mobjects[i%12])
		self.add(box)
		self.play(mobjects[3].shift, 2*RIGHT, UpdateFromFunc(group, update), run_time = 2)
		self.play(mobjects[5].shift, UP, UpdateFromFunc(group, update), run_time = 2)
		self.play(
			Rotating(mobjects[4], radians = PI/8, about_point = [-3.5, -2, 0], rate_func = smooth, run_time = 2), 
			Rotating(mobjects[3], radians = PI/6, about_point = [0, 0, 0], rate_func = smooth, run_time = 2),
			UpdateFromFunc(group, update), 
			run_time = 2
		)
		self.play(
			mobjects[5].shift, DOWN+RIGHT,
			mobjects[4].shift, UP+RIGHT,
			UpdateFromFunc(group, update), 
			run_time = 2,
		)
		self.play(
			mobjects[3].shift, 3*LEFT,
			mobjects[4].shift, 2*RIGHT+UP,
			UpdateFromFunc(group, update),
			run_time = 2,
		)
		self.play(
			mobjects[4].shift, 4*LEFT+2*DOWN,
			mobjects[3].shift, UP+RIGHT,
			UpdateFromFunc(group, update),
			run_time = 2,
		)
		self.play(
			mobjects[4].move_to, [-6, -3.5, 0],
			mobjects[5].move_to, [4, -3.5, 0],
			mobjects[3].move_to, [-3, 3.5, 0],
			UpdateFromFunc(group, update),
			run_time = 2,
		)
		self.play(
			mobjects[3].move_to, VERTEX[0],
			mobjects[4].move_to, VERTEX[1],
			mobjects[5].move_to, VERTEX[2],
			UpdateFromFunc(group, update),
			run_time = 2,
		)
		self.wait()


def get_angle(a, b):
	if b[0]-a[0] == 0:
		return PI/2
	elif (b[1]-a[1])/(b[0]-a[0]) < 0:
		return np.arctan((b[1]-a[1])/(b[0]-a[0]))+PI
	else: 
		return np.arctan((b[1]-a[1])/(b[0]-a[0]))

def get_distance(a, b):
	return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def get_area(a, b, c):
	s = (a+b+c)/2
	return (s*(s-a)*(s-b)*(s-c))**0.5


