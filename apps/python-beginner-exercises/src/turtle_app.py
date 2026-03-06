import turtle

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("🐢 Native Turtle Graphics App")
    screen.bgcolor("lightblue")
    screen.setup(width=800, height=600)
    
    # Create a turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.speed(5)  # Moderate speed (1-10, where 10 is fastest)
    t.pensize(2)
    
    # Make the turtle move forward continuously
    def move_forward():
        """Move turtle forward and repeat"""
        t.forward(2)
        screen.ontimer(move_forward, 50)  # Repeat every 50ms
    
    # Add some visual enhancements
    t.penup()
    t.goto(-300, 0)  # Start from left side
    t.pendown()
    
    # Start the movement
    print("🐢 Turtle is moving forward...")
    print("Close the window to stop the program")
    move_forward()
    
    # Keep the window open
    screen.mainloop()

if __name__ == "__main__":
    main()
