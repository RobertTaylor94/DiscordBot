import PIL.Image as Image
import PIL.ImageOps as ImageOps
import os

def stitch_dice_images(dice_rolls, user_id):
    images = []
    for roll in dice_rolls:
        dice_type = roll[1]
        dice_result = roll[0]
        # Load the appropriate dice image
        dice_image = Image.open(f"/Users/robert/Desktop/DiscordBot/assets/d{dice_type}/d{dice_type}s{dice_result}.png")
        # Resize the dice image to a consistent size
        resized_dice_image = dice_image.resize((100, 100))
        # Convert the dice image to RGBA format to preserve transparency
        if dice_image.mode != "RGBA":
            resized_dice_image = resized_dice_image.convert("RGBA")
        images.append(resized_dice_image)
    # Stitch the dice images together
    stitched_image = Image.new("RGBA", (len(images) * 100, 100))
    for i, image in enumerate(images):
        stitched_image.paste(image, (i * 100, 0))
    user_assets_dir = f"/Users/robert/Desktop/DiscordBot/assets/{user_id}"
    if not os.path.exists(user_assets_dir):
        os.makedirs(user_assets_dir)

    stitched_image.save(f"/Users/robert/Desktop/DiscordBot/assets/{user_id}/stitched_image.png")