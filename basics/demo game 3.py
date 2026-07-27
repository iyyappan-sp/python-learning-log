import turtle

scr = turtle.Screen()
scr.title("Game Demo 3")
scr.bgpic("bgpic.gif")


# register shape
scr.register_shape("player.gif")

player = turtle.Turtle()
player.shape("player.gif")
