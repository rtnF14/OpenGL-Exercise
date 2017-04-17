import pyglet
from pyglet.gl import *

win = pyglet.window.Window()
win.set_fullscreen(True)


@win.event
def on_draw():
	#Clear buffer
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_LINE_STRIP)
	glColor3f(1.0, 0, 0);
	glVertex2i(80,435)
	glVertex2i(108,449)
	glVertex2i(103,457)
	glVertex2i(133,466)
	glVertex2i(239,475)
	glVertex2i(263,525)
	glVertex2i(227,543)
	glVertex2i(188,571)
	glVertex2i(149,586)
	glVertex2i(133,607)
	glVertex2i(133,615)
	glVertex2i(157,606)
	glVertex2i(179,631)
	glVertex2i(203,627)
	glVertex2i(218,663)
	glVertex2i(234,675)
	glVertex2i(247,675)
	glVertex2i(247,709)
	glVertex2i(259,735)
	glVertex2i(287,749)
	glVertex2i(207,742)
	glVertex2i(131,713)
	glVertex2i(123,723)
	glVertex2i(120,705)
	glVertex2i(137,669)
	glVertex2i(129,636)
	glVertex2i(122,626)
	glVertex2i(109,672)
	glVertex2i(122,674)
	glVertex2i(116,679)
	glVertex2i(121,694)
	glVertex2i(107,703)
	glVertex2i(104,691)
	glVertex2i(89,698)
	glVertex2i(71,698)
	glVertex2i(57,708)
	glVertex2i(44,704)
	glVertex2i(51,701)
	glVertex2i(49,694)
	glVertex2i(54,700)
	glVertex2i(64,693)
	glVertex2i(70,683)
	glVertex2i(60,679)
	glVertex2i(44,679)
	glVertex2i(52,673)
	glVertex2i(68,672)
	glVertex2i(90,662)
	glVertex2i(91,649)
	glVertex2i(77,593)
	glVertex2i(82,580)
	glVertex2i(95,556)
	glVertex2i(95,535)
	glVertex2i(88,521)
	glVertex2i(82,514)
	glVertex2i(67,511)
	glVertex2i(59,499)
	glVertex2i(66,505)
	glVertex2i(96,506)
	glVertex2i(103,500)
	glVertex2i(113,559)
	glVertex2i(123,551)
	glVertex2i(124,534)
	glVertex2i(145,517)
	glVertex2i(113,510)
	glVertex2i(108,498)
	glVertex2i(114,501)
	glVertex2i(122,497)
	glVertex2i(123,489)
	glVertex2i(156,507)
	glVertex2i(169,519)
	glVertex2i(212,521)
	glVertex2i(232,506)
	glVertex2i(210,487)
	glVertex2i(122,471)
	glVertex2i(101,462)
	glVertex2i(88,463)
	glVertex2i(81,432)
	glEnd()

	
pyglet.app.run()