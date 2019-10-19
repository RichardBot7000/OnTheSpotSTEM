from big_ol_pile_of_manim_imports import *


class CS(Scene):
	def construct(self):
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
			FadeOut(circle[0]),
			FadeOut(circle[1]),
			FadeOut(circle[2]),
			FadeOut(circle[3]),
			FadeOut(circle[4]),
			FadeOut(circle[5]),
			FadeOut(circle[6]),
			FadeOut(circle[7]),
			FadeOut(circle[8]),
			FadeOut(circle[9]),
			FadeOut(circle[10]),
			FadeOut(circle[11]),
			FadeOut(circle[12]),
			FadeOut(circle[13]),
			FadeOut(circle[14]),
			FadeOut(line[0]),
			FadeOut(line[1]),
			FadeOut(line[2]),
			FadeOut(line[3]),
			FadeOut(line[4]),
			FadeOut(line[5]),
			FadeOut(line[6]),
			FadeOut(line[7]),
			FadeOut(line[8]),
			FadeOut(line[9]),
			FadeOut(line[10]),
			FadeOut(line[11]),
			FadeOut(line[12]),
			FadeOut(line[13]),
			run_time = 0.5,
		)
		otss = TextMobject("On The Spot STEM").scale(3)
		self.play (
			Transform(text,otss)
		)
		self.wait(1)
