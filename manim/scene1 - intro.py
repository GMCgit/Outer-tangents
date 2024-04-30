from manim import *

'''
TODO:
#* Scene1.1 - problem introduction
    #? Graph
    #? Voiceover (script 1.1)
#* Scene1.2 - problem listing
    #? List all the tasks
    #? Voiceover (script 1.2)
#* Scene 1.3 - introducing the teams
    #? Flesh out characters
        #= Charlie & Ethan, Gabriel & taylor 
    #? Animate
    #? Voiceover (script 1.3)
#* Scene 1.4 - what is the goal
    #? Write a clear goal (formal math)
        #= animate text changing for different tasks
    #? Voiceover (script 1.4)
'''

class Scene1(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        
        