"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Lanxi Wang.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
hh = rg.SimpleTurtle('turtle')
hh.pen = rg.Pen('black', 2)
hh.speed = 0.001
hh.draw_circle(100)
for k in range(8):
  hh.left(45)
  hh.draw_circle(100)

lanxi=rg.SimpleTurtle('turtle')
lanxi.pen=rg.Pen('red',8)
lanxi.speed=5
lanxi.pen_up()
lanxi.right(90)
lanxi.forward(200)
lanxi.left(90)
lanxi.pen_down()
lanxi.draw_circle(200)

for k in range(5):
    lanxi.pen_up()
    lanxi.right(90)
    lanxi.forward(15)
    lanxi.left(90)
    lanxi.pen_down()
    lanxi.draw_circle(200+15*(k+1))

window.close_on_mouse_click()
