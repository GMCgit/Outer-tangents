from cProfile import label
from manim import *
from numpy import *

'''
TODO:
#* Scene1.1 - problem introduction
    #? Voiceover (script 1.1)
#* Scene1.2 - problem listing
    #? Voiceover (script 1.2)
#* Scene 1.3 - introducing the teams
    #? Voiceover (script 1.3)
#* Scene 1.4 - what is the goal
    #? Voiceover (script 1.4)
'''

class Scene1_1(Scene):
    def construct(self):
            
        # Quadratic 1
        vt = ValueTracker(-2)
        ax = Axes(x_range=[-3,7,1], y_range=[-3,7,1])
        f1 = always_redraw(lambda: ax.plot(lambda x: x**2-4*x+3, color=BLUE, x_range=[-2, vt.get_value()]))
        
        f1_dot = always_redraw(lambda: Dot(
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),
            color=BLUE
        ))
        A_dot = Dot(point=ax.c2p(2, -2), color=YELLOW)
        
        self.play(Write(ax))
        self.wait()
        self.add(f1, f1_dot)
        self.play(vt.animate.set_value(7), run_time=6)
        self.play(FadeOut(f1_dot), FadeIn(A_dot))
        self.play(Write(Tex(r"$f(x)=x^2-4x+3$", color=BLUE).scale(0.75).move_to(LEFT*0.25)))
        self.wait(3)
        
        #tangents
        vt2 = ValueTracker(-5)
        t_1 = always_redraw(lambda: ax.plot(lambda x: -2*x+2, color=RED_C, x_range=[-5, vt2.get_value()]))
        t_2 = always_redraw(lambda: ax.plot(lambda x: 2*x-6, color=RED_C, x_range=[-5, vt2.get_value()]))
        
        self.add(t_1,t_2)
        self.play(vt2.animate.set_value(8), run_time=6)
        self.wait(3)
        
        self.clear()

class Scene1_2(Scene):
    def construct(self):
        qList = BulletedList(
            r"Given that quadratic, where would you say those points should exist?",
            r"Given any polynomial function can you find the region where those points should exist?",
            r"Given any analytic function can you find the region where those points should exist?",
            r"Given a closed curve (circle, ellipse, random blob...) can you find the region where those points should exist?",
            r"Given a $C^2$ curve can you find the region where those points should exist?"
        ).scale(0.75)
        qList.set_color_by_gradient(YELLOW_A, RED_B)
        
        self.play(Write(qList), run_time=5)
        
        self.wait(3)
        self.clear()
        
class Scene1_3(Scene):
    def construct(self):
        dLine = Line(start=[0, 4, 0], end=[0, -4, 0])
        self.play(Create(dLine))
        self.wait()
        
        self.play(Write(Tex(r"Team A!", color=BLUE_C).move_to([-3.5,3,0])))
        self.play(Write(Tex(r"Team B!", color=PINK).move_to([3.5,3,0])))
        
        def charDrawer(x,y, name, colour, scale):
            dx = sin(pi/6)*scale
            dy = cos(pi/6)*scale
            #Legs, body and "skirts" through a shaded polygon, first 4 legs, rest hands
            charBody = Polygon([x,y,0], [x-dx, y-dy, 0], [x+dx, y-dy,0], [x,y,0], [x,y+dy, 0], [x-dx,y+dy/2,0], [x,y+dy, 0], [x+dx,y+dy/2,0], [x,y+dy, 0], color=colour, fill_opacity=0.3)
            charHead = Circle(radius=scale/3, color=colour, fill_opacity=0.3).move_to([x,y+dy+scale/3+0.06,0])
            
            nameL = Tex(name, color=colour).move_to([x, y-2*dy, 0]).scale(0.75)
            char = VGroup(charBody, charHead, nameL)
            return char
        
        self.play(Create(charDrawer(-5, -1, "Charlie", BLUE_C, 1)))
        self.play(Create(charDrawer(-3, -1, "Ethan", BLUE_C, 1)))
        self.play(Create(charDrawer(3, -1, "Gabriel", PINK, 1)))
        self.play(Create(charDrawer(5, -1, "Taylor", PINK, 1)))
        
        self.wait(3)
        self.clear()
        
class Scene1_4(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        tex1 = Tex(r"{Let $f=x^2-4x+3$ and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$}", tex_template=myTemplate, color=YELLOW_B).scale(0.75)
        self.play(Write(tex1))
        self.wait(3)
        
        tex2 = Tex(r"{Let $f$ be a polynomial, $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=YELLOW_E).scale(0.75)
        self.play(ReplacementTransform(tex1, tex2))
        self.wait(3)
        
        tex3 = Tex(r"{Let $f$ be any analytic function, $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=RED_B).scale(0.75)
        self.play(ReplacementTransform(tex2, tex3))
        self.wait(3)
        
        tex4 = Tex(r"{Let $f$ be any smooth closed curve (circle, ellipse...), $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=RED_B).scale(0.75)
        self.play(ReplacementTransform(tex3, tex4))
        self.wait(3)
        
        tex5 = Tex(r"{Let $\Gamma_f$ be a graph of some curve on $\mathbb{R}^2$ (can be a closed curve) which is at least $\mathscr{C}^2$. Find the set $E\subseteq\mathbb{R}^2$ or conditions on said set such that for every point $A(x_A, y_A)\in E$ there exists a tangent on $\Gamma_f$ that also passes through $p$.}", tex_template=myTemplate, color=RED_E).scale(0.75)
        
        self.play(ReplacementTransform(tex4, tex5))
        self.wait(3)
        
        self.clear()


#! Compliation of all the sub scenes
class Scene1(Scene):
    def construct(self):
             
        # Quadratic 1
        vt = ValueTracker(-2)
        ax = Axes(x_range=[-3,7,1], y_range=[-3,7,1])
        f1 = always_redraw(lambda: ax.plot(lambda x: x**2-4*x+3, color=BLUE, x_range=[-2, vt.get_value()]))
        
        f1_dot = always_redraw(lambda: Dot(
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),
            color=BLUE
        ))
        A_dot = Dot(point=ax.c2p(2, -2), color=YELLOW)
        
        self.play(Write(ax))
        self.wait()
        self.add(f1, f1_dot)
        self.play(vt.animate.set_value(7), run_time=6)
        self.play(FadeOut(f1_dot), FadeIn(A_dot))
        self.play(Write(Tex(r"$f(x)=x^2-4x+3$", color=BLUE).scale(0.75).move_to(LEFT*0.25)))
        self.wait(3)
        
        #tangents
        vt2 = ValueTracker(-5)
        t_1 = always_redraw(lambda: ax.plot(lambda x: -2*x+2, color=RED_C, x_range=[-5, vt2.get_value()]))
        t_2 = always_redraw(lambda: ax.plot(lambda x: 2*x-6, color=RED_C, x_range=[-5, vt2.get_value()]))
        
        self.add(t_1,t_2)
        self.play(vt2.animate.set_value(8), run_time=6)
        self.wait(3)
        
        self.clear()
        
        qList = BulletedList(
            r"Given that quadratic, where would you say those points should exist?",
            r"Given any polynomial function can you find the region where those points should exist?",
            r"Given any analytic function can you find the region where those points should exist?",
            r"Given a closed curve (circle, ellipse, random blob...) can you find the region where those points should exist?",
            r"Given a $C^2$ curve can you find the region where those points should exist?"
        ).scale(0.75)
        qList.set_color_by_gradient(YELLOW_A, RED_B)
        
        self.play(Write(qList), run_time=5)
        
        self.wait(3)
        self.clear()
        
        dLine = Line(start=[0, 4, 0], end=[0, -4, 0])
        self.play(Create(dLine))
        self.wait()
        
        self.play(Write(Tex(r"Team A!", color=BLUE_C).move_to([-3.5,3,0])))
        self.play(Write(Tex(r"Team B!", color=PINK).move_to([3.5,3,0])))
        
        def charDrawer(x,y, name, colour, scale):
            dx = sin(pi/6)*scale
            dy = cos(pi/6)*scale
            #Legs, body and "skirts" through a shaded polygon, first 4 legs, rest hands
            charBody = Polygon([x,y,0], [x-dx, y-dy, 0], [x+dx, y-dy,0], [x,y,0], [x,y+dy, 0], [x-dx,y+dy/2,0], [x,y+dy, 0], [x+dx,y+dy/2,0], [x,y+dy, 0], color=colour, fill_opacity=0.3)
            charHead = Circle(radius=scale/3, color=colour, fill_opacity=0.3).move_to([x,y+dy+scale/3+0.06,0])
            
            nameL = Tex(name, color=colour).move_to([x, y-2*dy, 0]).scale(0.75)
            char = VGroup(charBody, charHead, nameL)
            return char
        
        self.play(Create(charDrawer(-5, -1, "Charlie", BLUE_C, 1)))
        self.play(Create(charDrawer(-3, -1, "Ethan", BLUE_C, 1)))
        self.play(Create(charDrawer(3, -1, "Gabriel", PINK, 1)))
        self.play(Create(charDrawer(5, -1, "Taylor", PINK, 1)))
        
        self.wait(3)
        self.clear()
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        tex1 = Tex(r"{Let $f=x^2-4x+3$ and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$}", tex_template=myTemplate, color=YELLOW_B).scale(0.75)
        self.play(Write(tex1))
        self.wait(3)
        
        tex2 = Tex(r"{Let $f$ be a polynomial, $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=YELLOW_E).scale(0.75)
        self.play(ReplacementTransform(tex1, tex2))
        self.wait(3)
        
        tex3 = Tex(r"{Let $f$ be any analytic function, $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=RED_B).scale(0.75)
        self.play(ReplacementTransform(tex2, tex3))
        self.wait(3)
        
        tex4 = Tex(r"{Let $f$ be any smooth closed curve (circle, ellipse...), $f: \mathbb{R}\rightarrow\mathbb{R}$, and let $A(x_A, y_A)$ be some point in the coordinate system. Find all the possible points such that there is a tangent on $f$ that also passes through $A$ }", tex_template=myTemplate, color=RED_B).scale(0.75)
        self.play(ReplacementTransform(tex3, tex4))
        self.wait(3)
        
        tex5 = Tex(r"{Let $\Gamma_f$ be a graph of some curve on $\mathbb{R}^2$ (can be a closed curve) which is at least $\mathscr{C}^2$. Find the set $E\subseteq\mathbb{R}^2$ or conditions on said set such that for every point $A(x_A, y_A)\in E$ there exists a tangent on $\Gamma_f$ that also passes through $p$.}", tex_template=myTemplate, color=RED_E).scale(0.75)
        
        self.play(ReplacementTransform(tex4, tex5))
        self.wait(3)
        
        self.clear()