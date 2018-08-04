import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(0, 1, 0),
	(-1, 0, -1),
	(1, 0, -1), 
	(1, 0, 1),
	(-1, 0, 1)
	)

edges = (
	(0, 1),
	(0, 2),
	(0, 3),
	(0, 4), 
	(1, 2), 
	(2, 3), 
	(3, 4), 
	(4, 1)
	)

def Pyramid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -5)
	glRotate(45, 1, 1, 0)
	while True:
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Pyramid()
		pygame.display.flip()
		pygame.time.wait(10)

main()