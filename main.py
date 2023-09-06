import os
from PIL import Image


class ImageResizer:
    def __init__(self):
        project_path = os.path.abspath(os.curdir)
        folder_path = "train"
        self.dataset_path = os.path.join(project_path, f"input/{folder_path}")
        self.output_path = os.path.join(project_path, f"output/{folder_path}")
        self.targeted_size = (800, 600)
        self.targeted_extension = [".JPG", ".jpg"]

    def get_files_in_dataset(self):
        folder_path = self.dataset_path

        file_paths = []
        if not os.path.isdir(folder_path):
            return file_paths

        for file in sorted(os.listdir(folder_path)):
            file_name, extension = os.path.splitext(file)
            if extension not in self.targeted_extension:
                continue

            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
        return file_paths

    def resize_image(self, file_path):
        file_name = os.path.basename(file_path)
        save_file_path = os.path.join(self.output_path, file_name)

        with Image.open(file_path) as img:
            img.load()
            image = img.resize(self.targeted_size, Image.LANCZOS)  # Image.Resampling.LANCZOS
            image.save(save_file_path, quality=100)

            print(image.size)

    def resize_image_with_crop(self, file_path):
        file_name = os.path.basename(file_path)
        save_file_path = os.path.join(self.output_path, file_name)

        with Image.open(file_path) as img:
            img.load()

            width, height = img.size
            new_width, new_height = self.targeted_size

            width_precision = 0
            height_precision = 0
            if width % 2 == 1:
                width -= 1
                width_precision = 1
            if height % 2 == 1:
                height -= 1
                height_precision = 1
            # precision will be for odd pixels, add one pixel only one side

            left_right_px = (width - new_width) // 2
            up_bottom_px = (height - new_height) // 2

            left = 0 + left_right_px + width_precision
            upper = 0 + up_bottom_px
            right = width - left_right_px
            lower = height - up_bottom_px + height_precision

            image = img.crop((left, upper, right, lower))
            image.save(save_file_path, quality=100)

            # new_size = (800, 600)
            # image = img.resize(new_size, Image.LANCZOS) # Image.Resampling.LANCZOS
            # image.save(save_file_path, quality=100)

            print(image.size)

    def process_folder(self):
        image_files = self.get_files_in_dataset()
        for file in image_files:
            self.resize_image_with_crop(file)


if __name__ == '__main__':
    image_resizer = ImageResizer()
    image_resizer.process_folder()
