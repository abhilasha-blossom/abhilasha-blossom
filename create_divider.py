from PIL import Image, ImageDraw

def create_divider():
    # Canvas settings - Updated to 600px width as requested (interpreting "earlier was 800" as width)
    # Reduced height to 100px since user said "height is a little big"
    width = 600
    height = 100
    canvas = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Load images
    try:
        boy = Image.open('boy.png').convert('RGBA')
        girl = Image.open('girl.png').convert('RGBA')
    except FileNotFoundError:
        print("Error: Images not found.")
        return

    # Resize images
    # Reduced max height to 90px to fit in 100px canvas
    max_h = 90
    
    def resize_contain(img, max_h):
        ratio = max_h / img.height
        new_w = int(img.width * ratio)
        return img.resize((new_w, max_h), Image.Resampling.NEAREST) # Use NEAREST for pixel art look

    boy = resize_contain(boy, max_h)
    girl = resize_contain(girl, max_h)

    # Positions
    boy_pos = (0, (height - boy.height) // 2)
    canvas.paste(boy, boy_pos, boy)

    girl_pos = (width - girl.width, (height - girl.height) // 2)
    canvas.paste(girl, girl_pos, girl)

    # Heart connection
    start_x = boy.width + 10
    end_x = width - girl.width - 10
    center_y = height // 2

    # Pixel heart pattern (7x6 approx)
    #   XX   XX
    #  XXXX XXXX
    #  XXXXXXXXX
    #   XXXXXXX
    #    XXXXX
    #     XXX
    #      X
    heart_pattern = [
        (1,0), (2,0), (5,0), (6,0),
        (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1),
        (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2),
        (1,3), (2,3), (3,3), (4,3), (5,3), (6,3),
        (2,4), (3,4), (4,4), (5,4),
        (3,5), (4,5)
    ]
    
    heart_color = (255, 0, 0, 255) # Red
    heart_width = 9 # width of the pattern roughly
    spacing = 20 # space between hearts

    current_x = start_x
    while current_x < end_x - heart_width:
        # Draw heart at current_x, center_y
        # Offset y to center the heart (height is approx 6 pixels)
        start_y = center_y - 3
        
        for dx, dy in heart_pattern:
            draw.point((current_x + dx, start_y + dy), fill=heart_color)
        
        current_x += spacing

    # Save as v2 to avoid caching
    canvas.save('custom_divider_v2.png')
    print("Divider created: custom_divider_v2.png")

if __name__ == "__main__":
    create_divider()
