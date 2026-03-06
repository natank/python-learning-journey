"""Create placeholder GIF files for the guess the number game."""
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_gif(filename, text, color):
    """Create a simple placeholder GIF with text."""
    width, height = 400, 300
    
    # Convert hex color to RGB tuple
    color = color.lstrip('#')
    rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    
    # Create image with solid background
    img = Image.new('RGB', (width, height), color=rgb_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a system font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 50)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 50)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text in white
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save as GIF with optimization
    output_path = os.path.join('src', 'static', filename)
    img.save(output_path, 'GIF', optimize=True)
    print(f"Created {output_path}")

if __name__ == '__main__':
    os.makedirs('src/static', exist_ok=True)
    
    create_placeholder_gif('counter.gif', 'Welcome!', '#667eea')
    create_placeholder_gif('lower.gif', 'Too Low', '#e74c3c')
    create_placeholder_gif('higher.gif', 'Too High', '#f39c12')
    create_placeholder_gif('success.gif', 'Success!', '#27ae60')
    
    print("\nAll placeholder GIFs created successfully!")
