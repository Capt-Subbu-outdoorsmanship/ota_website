import os

# Path to your gallery folder
gallery_path = r"C:\\Users\\sange\\Desktop\\outdoorsman_website\\Outdoorsman_Final_Version\\outdoorsman_website-main\\gallery"
output_file = "gallery_parse_output.txt"

try:
    # List of common image file extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

    # Get list of image files
    image_files = [f for f in os.listdir(gallery_path) if f.lower().endswith(image_extensions)]

    # Write to the output notepad (text file)
    with open(output_file, 'w', encoding='utf-8') as file:
        for image in image_files:
            # line = f'<img class="gallery_box_photo" src="gallery/{image}" alt="{image}"> \n'
            line = f'<a href="gallery/{image}" target="_blank"><img class="gallery_box_photo" src="gallery/{image}" alt="{image}"> </a> \n'
            file.write(line)

    print(f"Done! Written {len(image_files)} image entries to '{output_file}'.")

except Exception as e:
    print('Gallery Parsing Failed with Exception ' , e)