from PIL import Image, ImageDraw, ImageFont
import time
import random

font_path = "Fonts\BebasNeue-Regular.ttf"  
font_size = 50
text_color = (255, 255, 0)  
background_color = (0, 0, 50)  
frame_duration = 0.1  
sparkle_chars = " ? ?"

def create_text_frame(text, width, height):
    """Creates a single frame with the text centered"""
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)
    x_pos = (width - text_width) // 2
    y_pos = (height - text_height) // 2

    draw.text((x_pos, y_pos), text, text_color, font=font)
    return image

def add_sparkles(image, sparkle_chars):
    """Adds random sparkles to the image"""
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.truetype(font_path, font_size // 2) 

    for _ in range(15):  
        x_pos = random.randint(0, width)
        y_pos = random.randint(0, height)
        sparkle_char = random.choice(sparkle_chars)
        draw.text((x_pos, y_pos), sparkle_char, text_color, font=font)
    return image

message_parts = [
    "H.R.'s !",
    "Why aren't you hiring me ?",
    "LinkedIn : thekartikeyamishra",
]

frames = []
for part in message_parts:
    text_frames = [create_text_frame(part, 800, 300) for _ in range(10)]  
    sparkle_frames = [add_sparkles(frame.copy(), sparkle_chars) for frame in text_frames]
    frames.extend(sparkle_frames)

frames[0].save('animated_message.gif', save_all=True, append_images=frames[1:], duration=frame_duration * 1000, loop=0)