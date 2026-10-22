
import math

def setup():
    size(1920, 1080)
    colorMode(HSB, 360, 100, 100)
    noFill()
    strokeWeight(2)
    background(0)

# Make the motion blur
def draw():
    fill(0, 0, 0, 30) 
    rect(0, 0, width, height)
    noFill()
    
    # Move the origin (0,0) to the center of the canvas
    translate(width / 2, height / 2)
    
    # Calculate a changing hue base over time using the frame count
    hue_base = (frameCount * 0.5) % 360
    
    # Dynamic variables based on mouse position to make it interactive
    num_layers = int(map(mouseX, 0, width, 5, 25))
    symmetry = int(map(mouseY, 0, height, 4, 12))
    
    # Loop to draw multiple layers of expanding shapes
    for i in range(num_layers):
        # Calculate a pulse factor using a sine wave for expanding/contracting motion
        pulse = sin(frameCount * 0.02 + i * 0.5) * 50
        radius = (i * 25) + pulse
        
        # Cycle colors across the layers
        current_hue = (hue_base + (i * 15)) % 360
        stroke(current_hue, 90, 200)
        
        # Transformation or movement
        pushMatrix()
        # Rotate the line 
        rotate(radians(frameCount * (0.5 + (i * 0.1))))
        
        # Draw the repeated pattern around the circle
        for s in range(symmetry):
            rotate(TWO_PI / symmetry)
            
            # Psychedelic morphing shapes (alternating waveforms)
            if i % 2 == 0:
                # Waveform 1: Modulated Ellipses
                ellipse(radius / 2, 0, radius * 0.8, radius * 0.5)
            else:
                # Waveform 2: Interlocking Triangles
                triangle(-radius/3, radius/2, radius/3, radius/2, 0, -radius/3)
                
        popMatrix()
