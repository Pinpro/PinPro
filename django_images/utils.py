from contextlib import contextmanager
from io import BytesIO
import PIL
from PIL import Image, ImageDraw, ImageFont
from pinry.settings.base import DOMAIN, WATER_MARK, FONT_PATH

@contextmanager
def open_django_file(fieldfile):
    fieldfile.open()
    try:
        yield fieldfile
    finally:
        fieldfile.close()


def scale_and_crop_iter(image, options):
    """
    Generator which will yield several variations on the input image.
    Resize, crop and/or change quality of image.

    :param image: Source image file
    :param type: :class:`django.core.files.images.ImageFile

    :param`options: List of option dictionaries, See scale_and_crop_single
    argument names for available keys.
    :type options: list of dict
    """
    with open_django_file(image) as img:
        im = Image.open(img)
        # im1 = im.convert('RGB')
        #

        # im = add_text_to_image(im, "aaaaaaaaaaaaaaaaaa")
        # im.format = "JPEG"

        # if im.mode in ("RGBA", "P"):
            # im = im.convert("RGB")

        im.load()

        # print("======================================")
        # im = add_text_to_image(im, "bbbbbbbbbbbbbbbbbbbbbbbb")
        # print(im)

        # if im.mode in ("RGBA", "P"):
        #     im = im.convert("RGB")
        for opts in options:
            # Use already-loaded file when cropping.
            yield scale_and_crop_single(im, **opts)


# this neat function is based on easy-thumbnails
def scale_and_crop_single(image, size, crop=False, upscale=False, quality=None):
    """
    Resize, crop and/or change quality of an image.

    :param image: Source image file
    :param type: :class:`PIL.Image`

    :param size: Size as width & height, zero as either means unrestricted
    :type size: tuple of two int

    :param crop: Truncate image or not
    :type crop: bool

    :param upscale: Enable scale up
    :type upscale: bool

    :param quality: Value between 1 to 95, or None for keep the same
    :type quality: int or NoneType

    :return: Handled image
    :rtype: class:`PIL.Image`
    """
    im = image

    source_x, source_y = [float(v) for v in im.size]
    target_x, target_y = [float(v) for v in size]

    if crop or not target_x or not target_y:
        scale = max(target_x / source_x, target_y / source_y)
    else:
        scale = min(target_x / source_x, target_y / source_y)

    # Handle one-dimensional targets.
    if not target_x:
        target_x = source_x * scale
    elif not target_y:
        target_y = source_y * scale

    if scale < 1.0 or (scale > 1.0 and upscale):
        im = im.resize((int(source_x * scale), int(source_y * scale)),
                       resample=Image.ANTIALIAS)

    if crop:
        # Use integer values now.
        source_x, source_y = im.size
        # Difference between new image size and requested size.
        diff_x = int(source_x - min(source_x, target_x))
        diff_y = int(source_y - min(source_y, target_y))
        if diff_x or diff_y:
            # Center cropping (default).
            halfdiff_x, halfdiff_y = diff_x // 2, diff_y // 2
            box = [halfdiff_x, halfdiff_y,
                   min(source_x, int(target_x) + halfdiff_x),
                   min(source_y, int(target_y) + halfdiff_y)]
            # Finally, crop the image!
            im = im.crop(box)

    # Close image and replace format/metadata, as PIL blows this away.
    # We mutate the quality, but needs to passed into save() to actually
    # do anything.
    info = image.info
    if quality is not None:
        info['quality'] = quality
    im.format, im.info = image.format, info
    return im


def write_image_in_memory(img):
    # save to memory
    buf = BytesIO()
    try:
        img.save(buf, img.format, **img.info)
    except IOError:
        if img.info.get('progression'):
            orig_MAXBLOCK = PIL.ImageFile.MAXBLOCK
            temp_MAXBLOCK = 1048576
            if orig_MAXBLOCK >= temp_MAXBLOCK:
                raise
            PIL.ImageFile.MAXBLOCK = temp_MAXBLOCK
            try:
                img.save(buf, img.format, **img.info)
            finally:
                PIL.ImageFile.MAXBLOCK = orig_MAXBLOCK
        else:
            raise
    return buf


font = ImageFont.truetype(FONT_PATH, 24)


def add_text_to_image(image, text, font=font):
    """
    :param image:
    :param text:
    :param font:
    :return:
    """
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text

