import textwrap
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from PIL import Image, ImageDraw, ImageFont


def generate_thumbnail(job):
    font_path = "{}Montserrat/Montserrat-Medium.ttf".format(
        settings.THUMBNAILS_BASE_FOLDER
    )
    font_bold_path = "{}Montserrat/Montserrat-Bold.ttf".format(
        settings.THUMBNAILS_BASE_FOLDER
    )

    font_med_cntr = ImageFont.truetype(font_path, 60)
    font_bold_cntr = ImageFont.truetype(font_bold_path, 60)

    im = Image.open("{}thumb_base.png".format(settings.THUMBNAILS_BASE_FOLDER))
    im = im.resize((1280, 720))

    image_overlay = Image.new("RGB", (1280, 720), color=0)

    image_overlay.putalpha(175)

    im.paste(image_overlay, (0, 0), image_overlay)

    draw = ImageDraw.Draw(im)

    w, nothing = draw.textsize(str(_("Nova Oportunidade:")), font=font_med_cntr)
    draw.text(
        ((1280 - w) / 2, 90),
        text=str(_("Nova Oportunidade:")),
        fill="white",
        font=font_med_cntr,
    )

    offset = 225
    for line in textwrap.wrap(job.title, width=25):
        w, nothing = draw.textsize(line, font=font_bold_cntr)
        draw.text(((1280 - w) / 2, offset), line, font=font_bold_cntr)
        offset += font_bold_cntr.getsize(line)[1]

    w, nothing = draw.textsize(
        " ".join([str(_("Via")), settings.WEBSITE_NAME]), font=font_med_cntr
    )
    draw.text(
        ((1280 - w) / 2, 500),
        text=" ".join([str(_("Via")), settings.WEBSITE_NAME]),
        fill="white",
        font=font_med_cntr,
    )

    return im


def generate_thumbnail_quiz(quiz):
    font_path = "{}Montserrat/Montserrat-Medium.ttf".format(
        settings.THUMBNAILS_BASE_FOLDER
    )
    font_bold_path = "{}Montserrat/Montserrat-Bold.ttf".format(
        settings.THUMBNAILS_BASE_FOLDER
    )

    font_med_cntr = ImageFont.truetype(font_path, 60)
    font_bold_cntr = ImageFont.truetype(font_bold_path, 60)

    im = Image.open("{}thumb_quiz.jpg".format(settings.THUMBNAILS_BASE_FOLDER))
    im = im.resize((1280, 720))

    image_overlay = Image.new("RGB", (1280, 720), color=0)

    image_overlay.putalpha(175)

    im.paste(image_overlay, (0, 0), image_overlay)

    draw = ImageDraw.Draw(im)

    w, nothing = draw.textsize(str(_("Quiz:")), font=font_med_cntr)
    draw.text(
        ((1280 - w) / 2, 90),
        text=str(_("Quiz:")),
        fill="white",
        font=font_med_cntr,
    )

    offset = 225
    for line in textwrap.wrap(quiz.name, width=25):
        w, nothing = draw.textsize(line, font=font_bold_cntr)
        draw.text(((1280 - w) / 2, offset), line, font=font_bold_cntr)
        offset += font_bold_cntr.getsize(line)[1]

    w, nothing = draw.textsize(
        " ".join([str(_("Via")), settings.WEBSITE_NAME]), font=font_med_cntr
    )
    draw.text(
        ((1280 - w) / 2, 500),
        text=" ".join([str(_("Via")), settings.WEBSITE_NAME]),
        fill="white",
        font=font_med_cntr,
    )

    return im
