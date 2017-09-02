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
# TODO: 2.
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

lanxi = rg.SimpleTurtle('turtle')
lanxi.pen = rg.Pen('red', 1)
lanxi.speed = 5
size = 300
for k in range(20):
    lanxi.draw_square(size)
    lanxi.pen_up()
    lanxi.right(45)
    lanxi.forward(10)
    lanxi.left(45+k)
    lanxi.pen_down()
    size = size - 12


chen = rg.SimpleTurtle('turtle')
chen.pen = rg.Pen('yellow', 1)
chen.speed = 5
size = 300
for t in range(20):
    chen.draw_square(size)
    chen.pen_up()
    chen.left(45)
    chen.backward(10)
    chen.right(45+t)
    chen.pen_down()
    size = size - 12
window.close_on_mouse_click()
