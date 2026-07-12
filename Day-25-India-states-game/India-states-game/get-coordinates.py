import turtle

# 1. Set up the screen
screen = turtle.Screen()
screen.title("Click to Get Map Coordinates")

# 2. Load your India map image
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

# 3. Define the click event function
def get_mouse_click_coor(x, y):
    print(f"Clicked coordinates: X = {x}, Y = {y}")

# 4. Listen for mouse clicks on the screen
turtle.onscreenclick(get_mouse_click_coor)

# 5. Keep the window open
turtle.mainloop()
