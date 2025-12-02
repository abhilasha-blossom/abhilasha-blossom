from PIL import Image, ImageDraw, ImageFilter

def create_divider():
    # Canvas settings
    width = 800
    height = 130
    canvas = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Load images
    try:
        # Assuming typical ordering, but we might need to swap if user feedback indicates
        # User said: "boy at extreme leftmost and the girl at rightmost"
        # I'll map 'boy.png' to left and 'girl.png' to right
        boy = Image.open('boy.png').convert('RGBA')
        girl = Image.open('girl.png').convert('RGBA')
    except FileNotFoundError:
        print("Error: Images not found.")
        return

    # Resize images to fit height if necessary (keeping aspect ratio)
    # Let's say max height is 120px to leave some padding
    max_h = 120
    
    def resize_contain(img, max_h):
        ratio = max_h / img.height
        new_w = int(img.width * ratio)
        return img.resize((new_w, max_h), Image.Resampling.LANCZOS)

    boy = resize_contain(boy, max_h)
    girl = resize_contain(girl, max_h)

    # Positions
    # Boy on left (x=0)
    boy_pos = (0, (height - boy.height) // 2)
    canvas.paste(boy, boy_pos, boy)

    # Girl on right (x=width-girl.width)
    girl_pos = (width - girl.width, (height - girl.height) // 2)
    canvas.paste(girl, girl_pos, girl)

    # Line settings
    line_y = height // 2
    start_x = boy.width + 10 # padding
    end_x = width - girl.width - 10 # padding
    
    # Neon effect: Draw multiple lines with decreasing width and increasing opacity
    # Color: Neon Pink #FF6EC7 (HotPink) or #FF1493 (DeepPink)
    # Let's use a bright neon pink
    neon_color = (255, 20, 147) # DeepPink
    
    # Glow (wider, transparent)
    draw.line([(start_x, line_y), (end_x, line_y)], fill=(255, 105, 180, 100), width=8) # HotPink low alpha
    draw.line([(start_x, line_y), (end_x, line_y)], fill=(255, 20, 147, 150), width=5)
    # Core (thin, solid)
    draw.line([(start_x, line_y), (end_x, line_y)], fill=(255, 255, 255, 255), width=2) # White core for "neon" look
    
    # Save
    canvas.save('custom_divider.png')
    print("Divider created: custom_divider.png")

if __name__ == "__main__":
    create_divider()
