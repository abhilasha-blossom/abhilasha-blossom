from PIL import Image, ImageDraw

def create_divider():
    # Canvas settings
    # Width remains 600px
    width = 600
    # Height: "half as the committed one" (committed was 100px, so 50px)
    height = 50 
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
    # Character height: fit within 50px (e.g., 45px)
    max_h = 45
    
    def resize_contain(img, max_h):
        ratio = max_h / img.height
        new_w = int(img.width * ratio)
        return img.resize((new_w, max_h), Image.Resampling.NEAREST)

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
    heart_pattern = [
        (1,0), (2,0), (5,0), (6,0),
        (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1),
        (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2),
        (1,3), (2,3), (3,3), (4,3), (5,3), (6,3),
        (2,4), (3,4), (4,4), (5,4),
        (3,5), (4,5)
    ]
    
    # Pink hearts as requested
    heart_color = (255, 105, 180, 255) # HotPink
    heart_width = 9 
    spacing = 20 

    current_x = start_x
    while current_x < end_x - heart_width:
        start_y = center_y - 3
        
        for dx, dy in heart_pattern:
            draw.point((current_x + dx, start_y + dy), fill=heart_color)
        
        current_x += spacing

    # Save as v4
    canvas.save('custom_divider_v4.png')
    print("Divider created: custom_divider_v4.png")

if __name__ == "__main__":
    create_divider()
