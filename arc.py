from big_ol_pile_of_manim_imports import *
import numpy as np
import itertools as it
from copy import deepcopy
import sys

from manimlib.constants import *

from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon
from manimlib.mobject.functions import *
from manimlib.once_useful_constructs.region import  region_from_polygon_vertices, region_from_line_boundary


class Calculus(GraphScene):
	def construct(self):
		text = TextMobject("What is Calculus?").scale(2)
		self.play(Write(text))
		self.play(FadeOut(text))
		GraphScene.setup(self)
		self.setup_axes()
		self.wait()
		def func(x):
			return 0.06*(x-1)*(x-4)*(x-8)+4
		graph = self.get_graph(func, x_min = 0, x_max = 10)
		self.play(ShowCreation(graph))
		kwargs = {
			"x_min" : 2,
			"x_max" : 8,
			"fill_opacity" : 0.75,
			"stroke_width" : 0.25,
		}
		num=6
		self.rect_list = self.get_riemann_rectangles_list(
			graph, num,start_color=GREEN,end_color=PURPLE, **kwargs
		)
		flat_rects = self.get_riemann_rectangles(
			self.get_graph(lambda x : 0), dx = 0.5,start_color=invert_color(GREEN),end_color=invert_color(PURPLE),**kwargs
		)
		rects = self.rect_list[0]
		self.transform_between_riemann_rects(
			flat_rects, rects, 
			replace_mobject_with_target_in_scene = True,
			run_time=0.9
		)
		for j in range(4,6):
			for w in self.rect_list[j]:
				color=w.get_color()
				w.set_stroke(color,1.5)
		for j in range(1,6):
			self.transform_between_riemann_rects(
			self.rect_list[j-1], self.rect_list[j], dx=1,
			replace_mobject_with_target_in_scene = True,
			run_time=0.9
			)


class Zoom(GraphScene, MovingCameraScene):
	def construct(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)
		self.setup_axes()
		def func(x):
			return 1.5*np.sin(3*x)+2.5*np.cos(5*x)+4
		def get_x_value(input_tracker):
			return input_tracker.get_value()
		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))
		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))
		graph = self.get_graph(func, x_min = 0, x_max = 10)
		self.play(ShowCreation(graph), run_time = 2)
		dot = Dot().move_to(get_graph_point(ValueTracker(3.7))).scale(0.0001)
		self.play(FadeIn(dot))
		self.play(
			self.camera_frame.scale, 0.01,
			self.camera_frame.move_to, dot,
			run_time = 5
		)
		self.wait()


class Divide(GraphScene):
	def construct(self):
		GraphScene.setup(self)
		self.setup_axes()
		def func(x):
			return np.sin(x)+2*np.cos(20/11*x)+4
		def get_x_value(input_tracker):
			return input_tracker.get_value()
		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))
		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))
		graph = self.get_graph(func, x_min = 0, x_max = 10).set_color("#14aaeb")
		self.play(ShowCreation(graph), run_time = 1.5)
		lines = []
		dist = 10
		num = 9
		text = TextMobject("\# of lines:").move_to([4, 2.5, 0])
		number = TexMobject(str(1)).next_to(text, RIGHT)
		for i in range(num):
			lines.append([])
			for j in range(2**i):
				COLOR = YELLOW
				wid = 2
				start = ValueTracker(j*(10/(2**i)))
				end = ValueTracker((j+1)*(10/(2**i)))
				lines[i].append(Line(get_graph_point(start), get_graph_point(end)).set_color(COLOR).set_stroke(width = wid))
				lines[i].append(Line(get_graph_point(start), (get_graph_point(start)+get_graph_point(end))/2).set_color(COLOR).set_stroke(width = wid))
				lines[i].append(Line((get_graph_point(start)+get_graph_point(end))/2 ,get_graph_point(end)).set_color(COLOR).set_stroke(width = wid))
		self.play(FadeIn(lines[0][0]), FadeIn(text), FadeIn(number))
		for i in range(num-1):
			temp = TexMobject(str(2**(i+1))).next_to(text, RIGHT)
			for j in range(2**i):
				self.remove(lines[i][3*j])
				self.add(lines[i][3*j+1])
				self.add(lines[i][3*j+2])
			self.play(
				*[ReplacementTransform(lines[i][3*j+1], lines[i+1][6*j]) for j in range(2**i)],
				*[ReplacementTransform(lines[i][3*j+2], lines[i+1][6*j+3]) for j in range(2**i)],
				ReplacementTransform(number, temp),
			)
			self.wait(0.5)
			number = temp
		self.play(*[FadeOut(lines[num-1][3*i]) for i in range(2**(num-1))], run_time = 2)
		self.wait()


class Spiral(Scene):
	def construct(self):
		graph = ParametricFunction(lambda t : t*np.cos(2*PI*t)*RIGHT + t*np.sin(2*PI*t)*UP, t_min = 0, t_max = 3)
		dot = Dot()
		bot = Dot()
		equals = TextMobject("=").move_to([0, 3, 0])
		arc = TextMobject("arc length").scale(2)
		temp = TextMobject("arc length").next_to(equals, LEFT)
		text = DecimalNumber(0, num_decimal_places = 4).next_to(equals, RIGHT)
		group = VGroup(dot, text)
		time = Dot().scale(0.000001)
		def update(group):
			dot.move_to(graph.points[-1])
			value = np.sqrt(2)/2/PI*(time.get_center()[0]**2)
			text = DecimalNumber(value, num_decimal_places = 4).next_to(equals, RIGHT)
			new_group = VGroup(dot, text)
			group.become(new_group)
			return group
		self.play(FadeIn(arc))
		self.wait()
		self.play(arc.move_to, temp, arc.scale, 0.5, FadeIn(equals), FadeIn(text))
		self.wait()
		self.play(FadeIn(bot))
		self.wait()
		self.play(ShowCreation(graph), UpdateFromFunc(group, update), time.shift, 3*2*PI*RIGHT, run_time = 6, rate_func = linear)
		self.wait()


class ThreeDSpiral(ThreeDScene):
	def construct(self):
		self.set_camera_orientation(phi=60*DEGREES, theta = 30*DEGREES)
		def integral(x):
			return (np.log(np.sqrt(2*PI*PI*x*x+1)+np.sqrt(2)*PI*x)/(2*PI))+(x*np.sqrt(2*PI*PI*x*x+1)/np.sqrt(2))
		log = np.sqrt(2*PI*PI+1)-np.sqrt(2)*PI
		constant = np.log(log)/np.log(np.exp(1))/(2*PI)-np.sqrt(2*PI*PI+1)/np.sqrt(2)
		graph = ParametricFunction(lambda t: [t*np.cos(2*PI*t), t*np.sin(2*PI*t), t-3], t_min = -1, t_max = 4)
		equals = TextMobject("=").move_to([0, 3, 0])
		text = TextMobject("arc length").next_to(equals, LEFT)
		time = Dot().scale(0.0000001).move_to([-1, 0, 0])
		decimal = DecimalNumber(0, num_decimal_places = 4).next_to(equals, RIGHT)
		group = VGroup(decimal)
		def update(group):
			value = integral(time.get_center()[0])-integral(-1)
			decimal = DecimalNumber(value, num_decimal_places = 4).next_to(equals, RIGHT)
			new_group = VGroup(decimal)
			group.become(new_group)
			return group
		bot = Dot().move_to([0, 3 ,0])
		self.begin_ambient_camera_rotation(rate = 0.25)
		self.play(ShowCreation(graph), time.shift, 5*RIGHT, 
			run_time = 5, rate_func = linear)
		self.begin_ambient_camera_rotation(rate = 0)
		self.move_camera(phi = 30*DEGREES, rate_func = linear, run_time = 8)
		self.wait()


class Formula(GraphScene, ZoomedScene):
	CONFIG = {
		"zoom_factor": 0.025,
		"zoomed_display_height": 5,
		"zoomed_display_width": 5,
		"image_frame_stroke_width": 50,
		"zoomed_camera_config": {
			"default_frame_stroke_width": 3,
		},
	}
	def construct(self):
		GraphScene.setup(self)
		ZoomedScene.setup(self)
		self.setup_axes()
		def func(x):
			return np.sin(x)+2*np.cos(20/11*x)+4
		def get_x_value(input_tracker):
			return input_tracker.get_value()
		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))
		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))
		graph = self.get_graph(func, x_min = 0, x_max = 10)
		self.add(graph)
		self.wait()
		dot = Dot().scale(0.0000001).move_to([2, 1, 0])
		zoomed_camera = self.zoomed_camera
		zoomed_display = self.zoomed_display
		frame = zoomed_camera.frame
		zoomed_display_frame = zoomed_display.display_frame
		frame.move_to(get_graph_point(ValueTracker(dot.get_center()[0])))
		frame.set_color(PURPLE)
		zoomed_display_frame.set_color(RED)
		zoomed_display.shift(DOWN)
		zd_rect = BackgroundRectangle(
			zoomed_display,
			fill_opacity=0,
			buff=MED_SMALL_BUFF,
		)
		self.add_foreground_mobject(zd_rect)
		unfold_camera = UpdateFromFunc(
			zd_rect,
			lambda rect: rect.replace(zoomed_display)
		)
		self.play(ShowCreation(frame))
		self.wait()
		self.activate_zooming()
		self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
		self.wait()
		group = VGroup(frame)
		def update(group):
			frame.move_to(get_graph_point(ValueTracker(dot.get_center()[0])))
			new_group = VGroup(frame)
			group.become(new_group)
			return group
		self.play(dot.shift, RIGHT, UpdateFromFunc(group, update), run_time = 3)
		self.wait(3)
		self.play(
			self.get_zoomed_display_pop_out_animation(),
			unfold_camera,
			rate_func=lambda t: smooth(1-t),
		)
		self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
		self.wait()



class Formula2(GraphScene, ZoomedScene):
	CONFIG = {
		"zoom_factor": 0.025,
		"zoomed_display_height": 5,
		"zoomed_display_width": 5,
		"image_frame_stroke_width": 50,
		"zoomed_camera_config": {
			"default_frame_stroke_width": 3,
		},
	}
	def construct(self):
		GraphScene.setup(self)
		ZoomedScene.setup(self)
		self.setup_axes()
		def func(x):
			return np.sin(x)+2*np.cos(20/11*x)+4
		def get_x_value(input_tracker):
			return input_tracker.get_value()
		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))
		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))
		graph = self.get_graph(func, x_min = 0, x_max = 10)
		self.add(graph)
		self.wait()
		lines = []
		num = 100
		for i in range(num):
			lines.append(Line(get_graph_point(ValueTracker(10*i/num)), get_graph_point(ValueTracker((i+1)*10/num))))
		for i in range(num):
			self.play(ShowCreation(lines[i]), run_time = 0.05)
		self.wait()
		zoomed_camera = self.zoomed_camera
		zoomed_display = self.zoomed_display
		frame = zoomed_camera.frame
		zoomed_display_frame = zoomed_display.display_frame
		frame.move_to(get_graph_point(ValueTracker(5)))
		frame.set_color(PURPLE)
		zoomed_display_frame.set_color(RED)
		zoomed_display.shift(DOWN)
		zd_rect = BackgroundRectangle(
			zoomed_display,
			fill_opacity=0,
			buff=MED_SMALL_BUFF,
		)
		self.add_foreground_mobject(zd_rect)
		unfold_camera = UpdateFromFunc(
			zd_rect,
			lambda rect: rect.replace(zoomed_display)
		)
		self.play(ShowCreation(frame))
		self.wait()
		self.activate_zooming()
		self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
		self.wait()
		dot = Dot().scale(0.00001).move_to([5, 0, 0])
		group = VGroup(frame)
		def update(group):
			frame.move_to(get_graph_point(ValueTracker(dot.get_center()[0])))
			new_group = VGroup(frame)
			group.become(new_group)
			return group
		self.play(dot.shift, 2*LEFT, UpdateFromFunc(group, update), run_time = 10, rate_func = linear)
		self.wait()
		self.play(
			self.get_zoomed_display_pop_out_animation(),
			unfold_camera,
			rate_func=lambda t: smooth(1-t),
		)
		self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
		self.wait()



class Formula3(GraphScene):
	def construct(self):
		GraphScene.setup(self)
		self.setup_axes()
		def func(x):
			return np.sin(x)+2*np.cos(20/11*x)+4
		def get_x_value(input_tracker):
			return input_tracker.get_value()
		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))
		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))
		graph = self.get_graph(func, x_min = 0, x_max = 10)
		self.add(graph)
		lines = []
		num = 100
		for i in range(num):
			lines.append(Line(get_graph_point(ValueTracker(10*i/num)), get_graph_point(ValueTracker((i+1)*10/num))))
		for i in range(num):
			self.add(lines[i])
		self.wait()
		anchor = TexMobject("=").move_to([-0.5, 0, 0])
		equations = [
			TexMobject("s", "=", "\\sum_{i=1}^{n}", "L").move_to([0, 2.5, 0]),
			TexMobject("s", "=", "\\sum_{i=1}^{n}", "\\sqrt{(\\Delta x)^2+(\\Delta y)^2}"),
			TexMobject("s", "=", "\\lim_{n\\to\\infty}", "\\sum_{i=1}^{n}", "\\sqrt{(\\Delta x)^2+(\\Delta y)^2}"),
			TexMobject("s", "=", "\\int", "\\sqrt{(dx)^2+(dy)^2", "}"),
			TexMobject("s", "=", "\\int", "\\sqrt{", "(", "dx", ")", "^2", "+", "(", "dy", ")", "^2", ".}"),
			TexMobject("s", "=", "\\int", "\\sqrt{", "(", "dx", ")", "^2", "\\left(", "1", "+", "\\left(", "\\frac{dy}{dx}", "\\right)", "^2", "\\right)", "....}"),
			TexMobject("s", "=", "\\int", "\\sqrt{", "1", "+", "\\left(", "{", "dy", "\\over", "dx", "}", "\\right)", "^2", "}", "dx."),
			TexMobject("s", "=", "\\int_a^b", "\\sqrt{", "1", "+", "\\left(", "{", "dy", "\\over", "dx", "}", "\\right)", "^2", "}", "dx."),
		]
		equals = [1, 1, 1, 1, 1, 1, 1, 1]
		changes = [
			[0, 1, 2, 3], [0, 1, 3, 4],
			[0, 1, 3, 4], [0, 1, 2, 3],
		]
		for i in range(1, len(equations)):
			equations[i].move_to(equations[0])
		for i in range(len(equations)):
			equations[i].shift((equations[i][equals[i]].get_center()[0]-anchor.get_center()[0])*LEFT)
		for i in range(len(equations[0])):
			self.play(FadeIn(equations[0][i]))
			self.wait(0.5)
		self.wait()
		self.play(*[ReplacementTransform(equations[0][i], equations[1][i]) for i in range(len(equations[0]))], run_time = 2)
		self.wait()
		self.play(*[ReplacementTransform(equations[1][changes[0][i]], equations[2][changes[1][i]]) for i in range(len(changes[0]))],
			FadeInFrom(equations[2][2], LEFT))
		self.wait(2)
		self.play(*[ReplacementTransform(equations[2][changes[2][i]], equations[3][changes[3][i]]) for i in range(len(changes[2]))],
			FadeOut(equations[2][2]),
			*[FadeOut(lines[i]) for i in range(len(lines))])
		self.add(equations[3])
		self.remove(equations[3])
		self.add(equations[4])
		self.wait()
		self.play(ReplacementTransform(equations[4], equations[5]), run_time = 1.5)
		self.wait()
		self.play(ReplacementTransform(equations[5], equations[6]), run_time = 1.5)
		self.wait()
		group = VGroup()
		for mob in self.mobjects:
			group.add(mob)
		self.play(*[ReplacementTransform(equations[6][i], equations[7][i]) for i in range(len(equations[6]))])
		box = SurroundingRectangle(equations[7], color = YELLOW)
		self.play(ShowCreation(box))
		self.wait()
		self.play(FadeOut(group))
		self.play(equations[7].move_to, [0, 0, 0], box.move_to, [0, 0, 0])
		self.wait()



class LineLength(Scene):
	def construct(self):
		start = [-2, -1, 0]
		end = [2, 1, 0]
		line = Line(start, end)
		self.play(ShowCreation(line))
		self.wait()
		self.play(line.shift, 3*LEFT)
		text = TexMobject("c", "^2", "=", "a", "^2", "+", "b", "^2").move_to([3.5, 0, 0])
		sub = TexMobject("L", "^2", "=", "(", "\\Delta x", ")", "^2", "+", "(", "\\Delta y", ")", "^2").move_to(text)
		sqrt = TexMobject("L", "=", "\\sqrt{(", "\\Delta x", ")", "^2", "+", "(", "\\Delta y", ")", "^2", "}").move_to(text)
		sqrt[3].set_color(RED)
		sqrt[8].set_color(GREEN)
		sub[4].set_color(RED)
		sub[9].set_color(GREEN)
		start = line.points[0]
		end = line.points[-1]
		red = Line(start, [end[0], start[1], 0], color = RED)
		green = Line(end, [end[0], start[1], 0], color = GREEN)
		self.play(Write(text))
		deltax = TexMobject("\\Delta x", color = RED).next_to(red, DOWN)
		deltay = TexMobject("\\Delta y", color = GREEN).next_to(green, RIGHT)
		dist = TexMobject("L").next_to(line.get_center(), UL)
		redcopy = deltax.copy()
		greencopy = deltay.copy()
		distcopy = dist.copy()
		self.play(ShowCreation(red), ShowCreation(green), FadeInFrom(deltax, LEFT), FadeInFrom(deltay, UP), FadeInFrom(dist, UL))
		arr = [[4, 5, 7, 1, 2], [6, 7, 11, 1, 2], [3, 5, 8, 10], 
		[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11], [0, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10]]
		self.wait()
		self.play(*[ReplacementTransform(text[arr[0][i]], sub[arr[1][i]]) for i in range(5)], 
			*[FadeIn(sub[arr[2][i]]) for i in range(4)], 
			FadeOut(text[0]), FadeOut(text[3]), FadeOut(text[6]),
			redcopy.move_to, sub[4], greencopy.move_to, sub[9], distcopy.move_to, sub[0],
			run_time = 2)
		self.remove(redcopy, greencopy, distcopy)
		self.add(sub[0], sub[4], sub[9])
		self.wait()
		self.play(*[ReplacementTransform(sub[arr[3][i]], sqrt[arr[4][i]]) for i in range(len(arr[4]))], FadeOut(sub[3]),
			run_time = 2)
		box = SurroundingRectangle(sqrt, color = YELLOW)
		self.wait()
		self.play(ShowCreation(box))
		self.wait()


class Parametric(ThreeDScene):
	def construct(self):
		line = Line([-2, -1, 0], [2, 1, 0])
		self.wait()
		self.play(ShowCreation(line))
		self.wait()
		self.play(line.scale, 0.25, line.move_to, [-4, 2.5, 0])
		graph = ParametricFunction(lambda t : t/2*RIGHT + ((t**2)/4-1.5)*UP, t_min = -4, t_max = 4)
		self.play(ShowCreation(graph))
		self.wait()
		self.play(graph.scale, 0.25, graph.move_to, [-0, 2.5, 0])
		self.wait()
		arc = Arc(start_angle = PI, angle = -PI, radius = 2.5).shift(DOWN)
		self.play(ShowCreation(arc))
		self.wait()
		self.play(arc.scale, 0.25, arc.move_to, [4, 2.5, 0])
		self.wait()
		ellipse=Ellipse(width=3, height=1)
		self.play(ShowCreation(ellipse))
		self.play(FadeOut(ellipse), FadeOut(line), FadeOut(graph), FadeOut(arc))
		graph = ParametricFunction(lambda t: [2*np.cos(t), 2*np.sin(t), t/6], t_min = -6*PI, t_max = 6*PI)
		self.play(ShowCreation(graph), run_time = 3)
		self.move_camera(phi = 90*DEGREES, rate_func = smooth, run_time = 3)


class Parametrization(Scene):
	def construct(self):
		text = TextMobject("parametrization").scale(2)
		self.play(Write(text))
		self.wait(2)
		self.play(FadeOut(text))
		x = TexMobject("x=x(t)").move_to([0, 1.5, 0]).scale(2)
		y = TexMobject("y=y(t)").scale(2)
		z = TexMobject("z=z(t)").move_to([0, -1.5, 0]).scale(2)
		self.play(Write(x), run_time = 0.5)
		self.play(Write(y), run_time = 0.5)
		self.play(Write(z), run_time = 0.5)
		self.wait(2)
		self.play(WiggleOutThenIn(x), run_time = 2)
		self.play(WiggleOutThenIn(y), run_time = 2)
		self.play(WiggleOutThenIn(z), run_time = 2)
		self.wait()


class Pythag(ThreeDScene):
	def construct(self):
		self.set_camera_orientation(phi=75*DEGREES, theta = 300*DEGREES)
		line = Line([-3, -2, -1], [3, 2, 1])
		start = line.points[0]
		end = line.points[-1]
		arr = [[start[0], end[0]], [start[1], end[1]], [start[2], end[2]]]
		lines = []
		for i in range(2):
			for j in range(2):
				lines.append(Line([arr[0][0], arr[1][i], arr[2][j]], [arr[0][1], arr[1][i], arr[2][j]]).set_color(RED))
				lines.append(Line([arr[0][i], arr[1][0], arr[2][j]], [arr[0][i], arr[1][1], arr[2][j]]).set_color(GREEN))
				lines.append(Line([arr[0][i], arr[1][j], arr[2][0]], [arr[0][i], arr[1][j], arr[2][1]]).set_color(BLUE))
		self.play(ShowCreation(line))
		self.wait()
		self.play(*[ShowCreation(lines[i]) for i in range(len(lines))])
		self.begin_ambient_camera_rotation()
		self.wait(5)
		equations = [
			TexMobject("L", "=", "\\sqrt{", "(", "\\Delta", "x", ")", "^2", "+", "(", "\\Delta", "y", ")", "^2", "+", "(", "\\Delta", "z", ")", "^2", ".}").move_to([0, 3, 0]),
			TexMobject("L", "=", "\\sum", "\\sqrt{", "(", "\\Delta", "x", ")", "^2", "+", "(", "\\Delta", "y", ")", "^2", "+", "(", "\\Delta", "z", ")", "^2", ".}").move_to([0, 3, 0]),
			TexMobject("L", "=", "\\int", "\\sqrt{", "(", "d", "x", ")", "^2", "+", "(", "d", "y", ")", "^2", "+", "(", "d", "z", ")", "^2", ".}"),
		]
		equations[0][5].set_color(RED)
		equations[0][6].set_color(RED)
		equations[0][11].set_color(GREEN)
		equations[0][12].set_color(GREEN)
		equations[0][17].set_color(BLUE)
		equations[0][18].set_color(BLUE)
		changes = [
			[], []
		]
		for i in range(len(equations[0])):
			changes[0].append(i)
			if i < 2:
				changes[1].append(i)
			else:
				changes[1].append(i+1)
		self.add_fixed_in_frame_mobjects(equations[0])
		self.play(Write(equations[0]))
		self.wait(5)
		self.play(*[FadeOut(lines[i]) for i in range(len(lines))])
		self.stop_ambient_camera_rotation()
		self.wait()
		self.play(line.scale, 5)
		self.wait()
		self.play(*[FadeIn(lines[i]) for i in range(len(lines))])
		self.wait()
		self.play(*[FadeOut(lines[i]) for i in range(len(lines))], FadeOut(line))
		self.wait()



class Integrate(Scene):
	def construct(self):
		equations = [
			TexMobject("s", "=", "\\sqrt{", "(", "\\Delta", "x", ")", "^2", "+", "(", "\\Delta", "y", ")", "^2", "+", "(", "\\Delta", "z", ")", "^2", "}", ".").move_to([0, 3, 0]),
			TexMobject("s", "=", "\\sum", "\\sqrt{", "(", "\\Delta", "x", ")", "^2", "+", "(", "\\Delta", "y", ")", "^2", "+", "(", "\\Delta", "z", ")", "^2", "}", "."),
			TexMobject("s", "=", "\\int", "\\sqrt{", "(", "d", "x", ")", "^2", "+", "(", "d", "y", ")", "^2", "+", "(", "d", "z", ")", "^2", "}", "."),
			TexMobject("s", "=", "\\int", "\\sqrt{", "(", "d", "x", ")", "^2", "+", "(", "d", "y", ")", "^2", "+", "(", "d", "z", ")", "^2", "}", "{", "dt", "\\over", "dt", "}", "."),
			TexMobject("s", "=", "\\int", "\\sqrt{", "\\left(", "{" "d", "x", "\\over", "d", "t", "}", "\\right)", "^2", "+", "\\left(", "{" "d", "y", "\\over", "d", "t", "}", "\\right)", "^2", "+", "\\left(", "{" "d", "z", "\\over", "d", "t", "}", "\\right)", "^2", "}", "dt", "."),
			TexMobject("s", "=", "\\int_a^b", "\\sqrt{", "\\left(", "{" "d", "x", "\\over", "d", "t", "}", "\\right)", "^2", "+", "\\left(", "{" "d", "y", "\\over", "d", "t", "}", "\\right)", "^2", "+", "\\left(", "{" "d", "z", "\\over", "d", "t", "}", "\\right)", "^2", "}", "dt", "."),
		]
		equations[0][5].set_color(RED)
		equations[0][6].set_color(RED)
		equations[0][11].set_color(GREEN)
		equations[0][12].set_color(GREEN)
		equations[0][17].set_color(BLUE)
		equations[0][18].set_color(BLUE)
		changes = [
			[], [],
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24], 
			[0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25, 26, 27, 32, 33, 34, 35],
			[25, 26, 27], [8, 18, 28],
			[5, 6, 11, 12, 17, 18, 6, 7, 12, 13, 18, 19, 6, 7, 12, 13, 18, 19, 6, 7, 12, 13, 18, 19, 6, 7, 16, 17, 26, 27, 6, 7, 16, 17, 26, 27],
		]
		for i in range(6):
			equations[i][changes[6][6*i]].set_color(RED)
			equations[i][changes[6][6*i+1]].set_color(RED)
			equations[i][changes[6][6*i+2]].set_color(GREEN)
			equations[i][changes[6][6*i+3]].set_color(GREEN)
			equations[i][changes[6][6*i+4]].set_color(BLUE)
			equations[i][changes[6][6*i+5]].set_color(BLUE)
		for i in range(len(equations[0])):
			changes[0].append(i)
			if i < 2:
				changes[1].append(i)
			else:
				changes[1].append(i+1)
		self.add(equations[0])
		self.wait()
		self.play(equations[0].move_to, [0, 0, 0])
		self.wait()
		self.play(*[ReplacementTransform(equations[0][changes[0][i]], equations[1][changes[1][i]]) for i in range(len(changes[0]))], FadeInFrom(equations[1][2], LEFT))
		self.wait()
		self.play(*[ReplacementTransform(equations[1][i], equations[2][i]) for i in range(len(equations[1]))])
		self.wait()
		self.play(*[ReplacementTransform(equations[2][i], equations[3][i]) for i in range(len(equations[2]))], *[FadeIn(equations[3][i]) for i in range(len(equations[3])-6, len(equations[3]))])
		self.wait()
		self.play(*[ReplacementTransform(equations[3][changes[2][i]], equations[4][changes[3][i]]) for i in range(len(changes[2]))],
			*[FadeOut(equations[3][changes[4][i]]) for i in range(len(changes[4]))],
			*[FadeIn(equations[4][changes[5][i]]) for i in range(len(changes[5]))],
			*[FadeIn(equations[4][9+10*i]) for i in range(3)],
			*[FadeIn(equations[4][11+10*i]) for i in range(3)],
			)
		self.wait()
		self.play(ReplacementTransform(equations[4], equations[5]))
		box = SurroundingRectangle(equations[5], color = YELLOW)
		self.play(ShowCreation(box))
		self.wait()


class Simple(Scene):
	def construct(self):
		self.wait()
		circle = Circle(color = WHITE, radius = 2)
		self.play(ShowCreation(circle))
		self.wait()
		line = Line([-2, 0, 0], [2, 0, 0]).set_color(YELLOW)
		square = Square().scale(2).set_color(BLUE)
		self.play(ReplacementTransform(circle, line))
		self.wait()
		self.play(ReplacementTransform(line, square))
		triangle = RegularPolygon(3, start_angle = -PI/2).scale(-2)
		self.wait()
		self.play(ReplacementTransform(square, triangle))
		self.wait()
		graph = ParametricFunction(lambda t : 2*np.sin(3*PI*t)*RIGHT - 2*np.cos(4*PI*t)*UP, t_min = 0, t_max = 2).set_color("#8B4513").set_stroke(width = 8)
		self.play(ReplacementTransform(triangle, graph))
		self.wait()
		self.play(FadeOut(graph))
		self.wait()


class Projectile(Scene):
	def construct(self):
		graph = ParametricFunction(lambda t : t*RIGHT+ (-t*t/4+3)*UP, t_min = -3, t_max = 3)
		self.play(ShowCreation(graph))


class Transitions(Scene):
	def construct(self):
		arr = [TextMobject("Parameterization"), TextMobject("Applications"), TextMobject("Arc Length in 3D"),
			TextMobject("Curvature"), TextMobject("Line Integrals"),
		]
		for i in range(len(arr)):
			arr[i].scale(3)
		self.wait()
		for i in range(len(arr)):
			self.play(FadeIn(arr[i]))
			self.wait()
			self.play(FadeOut(arr[i]))
			self.wait()
		self.wait()


POINTS = np.array([
	[-FRAME_WIDTH/4, FRAME_HEIGHT/4, 0],
	[FRAME_WIDTH/4, FRAME_HEIGHT/4, 0],
	[FRAME_WIDTH/4, -FRAME_HEIGHT/4, 0],
	[-FRAME_WIDTH/4, -FRAME_HEIGHT/4, 0],
])

class RealWorld(Scene):
	def construct(self):
		self.wait()
		image = []
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image000.jpeg"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image001.jpg"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image002.png"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image003.jpg"))
		first = 2.5
		second = 0.6
		question = TextMobject("?").scale(first)
		for i in range(4):
			image[i].scale(first)
			self.play(FadeIn(image[i]))
			self.wait()
			self.play(image[i].move_to, POINTS[i], image[i].scale, second)
			self.wait()
		self.play(FadeIn(question))
		self.wait()
		text = TextMobject("Arc Length").scale(2)
		self.play(ReplacementTransform(question, text))
		self.wait()
		self.play(*[FadeOut(image[i]) for i in range(4)], text.scale, 1.5)
		self.wait()
		self.play(FadeOut(text))
		self.wait()


class Algebra(Scene):
	def construct(self):
		equations = [
			TexMobject("f", "(", "x", ")", "=", "{", "1", "\\over", "3", "}", "x", "^", "{", "{", "3", "\\over", "2", "}", "}", "-", "x", "^", "{", "{", "1", "\\over", "2", "}", "}"),
			TexMobject("f", "'", "(", "x", ")", "=", "{", "1", "\\over", "2", "}", "x", "^", "{", "{", "1", "\\over", "2", "}", "}", "-", "{", "1", "\\over", "2", "}", "x", "^", "{", "-", "{", "1", "\\over", "2", "}", "}"),
			TexMobject("\\sqrt{", "1", "+", "f", "'", "(", "x", ")", "^", "2", "}", "=", "{", "1", "\\over", "2", "}", "x", "^", "{", "{", "1", "\\over", "2", "}", "}", "+", "{", "1", "\\over", "2", "}", "x", "^", "{", "-", "{", "1", "\\over", "2", "}", ".}"),
			TexMobject("s", "=", "\\int_0^4", "\\sqrt{", "1", "+", "f", "'", "(", "x", ")", "^", "2", "}", "d", "x", "=", "\\int_0^4" "{", "1", "\\over", "2", "}", "x", "^", "{", "{", "1", "\\over", "2", "}", "}", "+", "{", "1", "\\over", "2", "}", "x", "^", "{", "-", "{", "1", "\\over", "2", "}", "}", "d", "x", "."),
			TexMobject("s", "=", "\\left(", "{", "1", "\\over", "3", "}", "x", "^", "{", "{", "3", "\\over", "2", "}", "}", "+", "x", "^", "{", "{", "1", "\\over", "2", "}", "}", "\\right)", "\\bigg\\vert_0^4"),
			TexMobject("s", "=", "{", "14", "\\over", "3")
		]
		self.wait()
		for i in range(len(equations)):
			equations[i].shift((2.5-i)*UP).scale(0.8)
			self.play(Write(equations[i]), run_time = 0.5)
			self.wait(0.2)
		self.wait()
		obj = []
		for i in range(len(equations)):
			for j in range(len(equations[i])):
				obj.append(equations[i][j])
		self.play(*[FadeOutAndShift(mob, (mob.get_center())/3) for mob in obj])
		self.wait()
		image = []
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image000.jpeg"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image001.jpg"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image002.png"))
		image.append(ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/image003.jpg"))
		for i in range(4):
			image[i].move_to(POINTS[i]).scale(1.5)
		self.play(*[FadeIn(image[i]) for i in range(4)])
		self.wait()
		self.play(WiggleOutThenIn(image[0]), WiggleOutThenIn(image[2]), run_time = 2)
		self.wait()
		self.play(*[FadeOut(image[i]) for i in range(4)])
		self.wait()


class Curvature(Scene):
	def construct(self):
		self.wait()
		graph = ParametricFunction(lambda t : t*np.cos(2*PI*t)*RIGHT + (t*np.sin(2*PI*t)-0.5)*UP, t_min = 0, t_max = 3).set_color("#02E8FD")
		self.play(ShowCreation(graph), run_time = 3)
		self.wait()
		def x_func(t):
			return t*np.cos(2*PI*t)
		def y_func(t):
			return t*np.sin(2*PI*t)-0.5
		def x_val(t):
			return np.cos(2*PI*t)-2*PI*t*np.sin(2*PI*t)
		def y_val(t):
			return np.sin(2*PI*t)+2*PI*t*np.cos(2*PI*t)
		def magnitude(t):
			return (((1+4*PI*PI*t*t))**0.5)/1.25
		def arc(t):
			return np.sqrt(2)/4/PI*(time.get_center()[0]**2)
		equation = TexMobject("\\kappa", "=", "\\bigg\\vert", "{", "d", "T", "\\over", "d", "s", "}", "\\bigg\\vert").move_to([0, 2.75, 0])
		color = ["#EDE712", "#FD1702"]
		equation[5].set_color(color[0])
		equation[8].set_color(color[1])
		arrow = Vector([x_val(1)/magnitude(1), y_val(1)/magnitude(1), 0], color = color[0]).shift([x_func(1), y_func(1), 0])
		curve = ParametricFunction(lambda t : t*np.cos(2*PI*t)*RIGHT + (t*np.sin(2*PI*t)-0.5)*UP, t_min = 1, t_max = 1.1).set_color(color[1])
		dec = DecimalNumber()
		dot = Dot().scale(0.00001).move_to([1, 0, 0])
		self.play(Write(equation))
		self.wait()
		self.play(GrowArrow(arrow), ShowCreation(curve))
		group = VGroup(arrow, curve)
		def update(group):
			t = dot.get_center()[0]
			arrow = Vector([x_val(t)/magnitude(t), y_val(t)/magnitude(t), 0], color = color[0]).shift([x_func(t), y_func(t), 0])
			curve = ParametricFunction(lambda t : t*np.cos(2*PI*t)*RIGHT + (t*np.sin(2*PI*t)-0.5)*UP, t_min = t, t_max = t+ 0.1).set_color(color[1])
			new_group = VGroup(arrow, curve)
			group.become(new_group)
			return group
		self.wait()
		self.play(dot.shift, RIGHT, UpdateFromFunc(group, update), run_time = 6, rate_func = linear)
		self.wait()
		fade = VGroup()
		for mob in self.mobjects:
			fade.add(mob)
		self.play(FadeOut(fade))
		self.wait()
		circle1 = Circle(color = YELLOW, radius = 1).move_to([-3, -1, 0])
		circle2 = Circle(color = BLUE, radius = 2).move_to([3, -1, 0])
		more = TextMobject("more curvature", color = YELLOW).move_to([-3, 2, 0])
		less = TextMobject("less curvature", color = BLUE).move_to([3, 2, 0])
		self.play(ShowCreation(circle1))
		self.play(ShowCreation(circle2))
		self.wait()
		self.play(FadeIn(more), FadeIn(less))
		self.wait()
		fade = VGroup()
		for mob in self.mobjects:
			fade.add(mob)
		self.play(*[FadeOutAndShift(mob, (mob.get_center())/3) for mob in fade])
		self.wait()


class CurvatureExample(Scene):
	def construct(self):
		image = ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/road.jpg").scale(3).move_to([0, -0.5, 0])
		text = TextMobject("Speed Limits").move_to([0, 3, 0])
		self.wait()
		self.play(GrowFromCenter(image))
		self.wait()
		self.play(Write(text), run_time = 1)
		self.wait()


class LineIntegral(ThreeDScene):
	def construct(self):
		self.wait()
		plane = NumberPlane(x_unit_size = 1, y_unit_size = 1).scale(2)
		graph = ParametricFunction(lambda t : [t, t*(t-2)*(t+2)/5, 1.5*(1+np.cos(t))], t_min = -2.5, t_max = 2.5).set_color("#FD1702")
		surface = ParametricSurface(
			lambda u, v: np.array([
				u/2,
				(u/2)*(u/2-2)*(u/2+2)/5,
				1.5*(1+np.cos(u/2))*v/10
			]),v_min=0,v_max=10,u_min=-5,u_max=5, checkerboard_colors=["#1ae576", "#1de22d"],
			resolution=(25, 15)).fade(0.5)
		self.play(ShowCreation(plane))
		self.wait()
		self.play(ShowCreation(graph))
		self.wait()
		self.move_camera(phi=60*DEGREES,theta=-60*DEGREES,distance = 12, run_time = 2.5) 
		self.wait()
		self.play(ShowCreation(surface))
		self.wait()
		transgraph = ParametricFunction(lambda t : [t, np.sin(t), t*t/4+1.8], t_min = -2.5, t_max = 2.5).set_color("#FD1702")
		transsurface = ParametricSurface(
			lambda u, v: np.array([
				u/2,
				np.sin(u/2),
				((u*u/4/4)+1.8)*v/10
			]),v_min=0,v_max=10,u_min=-5,u_max=5, checkerboard_colors=["#1ae576", "#1de22d"],
			resolution=(25, 15)).fade(0.5)
		bot = ParametricFunction(lambda t : [t, np.cos(t), 1.5**t+1], t_min = -2.5, t_max = 2.5).set_color("#FD1702")
		botsurface = ParametricSurface(
			lambda u, v: np.array([
				u/2,
				np.cos(u/2),
				(1.5**(u/2)+1)*v/10
			]),v_min=0,v_max=10,u_min=-5,u_max=5, checkerboard_colors=["#1ae576", "#1de22d"],
			resolution=(25, 15)).fade(0.5)
		self.play(ReplacementTransform(graph, transgraph), ReplacementTransform(surface, transsurface))
		self.wait()
		self.play(ReplacementTransform(transgraph, bot), ReplacementTransform(transsurface, botsurface))
		self.wait()
		self.play(FadeOut(plane), FadeOut(bot), FadeOut(botsurface))
		self.wait()


class LineIntegralExample(Scene):
	def construct(self):
		self.wait()
		rocket = ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/rocket.jpg").scale(4)
		wire = ImageMobject("/Users/richardwu/Documents/Manim/manim_3feb/images/wires.jpg").scale(4)
		self.play(GrowFromCenter(rocket))
		self.wait()
		self.play(rocket.move_to, [-3, 0, 0], rocket.scale, 0.5)
		self.wait()
		self.play(GrowFromCenter(wire))
		self.wait()
		self.play(wire.move_to, [3, 0, 0], wire.scale, 0.5)
		self.wait()



class Closing(Scene):
	def construct(self):
		self.wait()



class Introduction(Scene):
	def construct(self):
		text = TextMobject("Arc Length").scale(2)
		self.play(Write(text))
		self.wait()





