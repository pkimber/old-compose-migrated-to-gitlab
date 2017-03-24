# -*- encoding: utf-8 -*-
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from block.models import (
    Page,
    PageSection,
    Section,
    Template,
    TemplateSection,
    PaginatedSection,
    HeaderFooter,
    Url,
    Image,
    Link,
    Wizard,
    Menu,
    MenuItem,
)
from compose.models import *
from imakedata.imakedata import IMakeData
from imakedata.model.int import in_3
from imakedata.model.marketing import tweet, description, short_blurb, news_title
from imakedata.model.business import business_model

maker = IMakeData(1)
biz = maker.get_dataset(business_model + [tweet])[0]

heading_level = {
    'name': 'heading_level',
    'class': 'quicklist',
    'data': [H1, H2, H3, H4,],
}
css_width = {
    'name': 'css_width',
    'class': 'quicklist',
    'data': [a[0] for a in settings.CSS_WIDTHS],
}
text_position = {
    'name': 'text_position',
    'class': 'quicklist',
    'data': [a[0] for a in settings.CSS_TEXT_POSITION],
}
image_size = {
    'name': 'image_size',
    'class': 'quicklist',
    'data': [a[0] for a in settings.CSS_IMAGE_SIZES],
}

def quicklist(name, list):
    return  {'name': name, 'class': 'quicklist', 'sort': 'asc', 'data': list}


self_dir = os.path.dirname(os.path.realpath(__file__))
app_path = os.sep.join(self_dir.split(os.sep)[:-2])


staff_user = None
users = User.objects.filter(is_staff=True)
if users.count() > 0:
    staff_user = users[0]
    print(
        "using '{}' for setting up the pages".format(staff_user)
    )
else:
    raise CommandError("Cannot find any members of staff")


class Command(BaseCommand):

    help = "create a menu for example_compose app"

    def create_section(self, block_name, model_name):
        return Section.objects.init_section(
            block_name,
            block_name.capitalize(),
            'compose',
            model_name,
            'compose.{}.create'.format(model_name.lower()),
            )

    def init_template(self, name, file_name, sections):
        template = Template.objects.init_template(name, file_name)
        for section in sections:
            TemplateSection.objects.init_template_section(template, section)
        return template

    def init_page(self, slug_page, slug_menu, name, order, template, **kwargs):
        return Page.objects.init_page(slug_page, slug_menu, name, order, template, **kwargs)

    def init_featurestyle(self, name, class_name):
        style, created = FeatureStyle.objects.get_or_create(name=name, css_class_name=class_name)
        return style

    def init_headerstyle(self, name, class_name):
        style, created = HeaderStyle.objects.get_or_create(name=name, css_class_name=class_name)
        return style

    def add_gallery_images(self, content_obj, images):
        order = 1
        for image in images:
            order = order + 1
            obj = content_obj.slideshow.through(
                content=content_obj,
                image=image,
                order=order,
            )
            obj.save()
        content_obj.save()

    def save_image(self, src_file, title):
        return self.save_image_dir('theme/resources/img/', src_file, title)

    def save_image_dir(self, src_dir, src_file, title):
        # stop duplicate Image records and files
        search = Image.objects.filter(
            original_file_name=src_file, deleted=False)
        if search:
            return search[0]
        src_path = os.path.join(app_path, src_dir, src_file)
        f = open(src_path, 'rb')
        img_file = File(f)
        img = Image(title=title)
        img.image.save(name=src_file, content=img_file, save=False)
        img.save()
        if not f.closed:
            f.close()
        return img


    def handle(self, *args, **options):
        print ("Creating Content...")

        images = {}
        img_path = os.path.join(app_path, 'theme/resources/img')
        for root, subs, files in os.walk(img_path):
            for sub in subs:
                images[sub] = []
            for foto in files:
                sub = os.path.basename(root)
                title = os.path.splitext(foto)[0]
                title = title.replace('_', ' ').title()
                img = self.save_image(os.path.join(sub, foto), title)
                images[sub].append(img)

        people_image = {
            'name': 'people_image',
            'class': 'quicklist',
            'splutter': 20,
            'data': images['people'],
        }
        bg_image = {
            'name': 'bg_image',
            'class': 'quicklist',
            'data': images['bg'],
        }
        iconic_image = {
            'name': 'iconic_image',
            'class': 'quicklist',
            'splutter': 20,
            'data': images['iconic'],
        }
        inspirational_image = {
            'name': 'inspirational_image',
            'class': 'quicklist',
            'splutter': 30,
            'data': images['inspirational'] + images['people'],
        }
        print("Images imported")

        body_section = self.create_section(SECTION_BODY, 'Article')
        card_section = self.create_section(SECTION_CARD, 'Feature')
        header_a_section = self.create_section(Header.SECTION_A, 'Header')
        feature_a_section = self.create_section(Feature.SECTION_A, 'Feature')
        gallery_section = self.create_section(SECTION_GALLERY, 'Slideshow')
        slideshow_section = self.create_section(SECTION_SLIDESHOW, 'Slideshow')
        brochure_section = self.create_section(Feature.SECTION_E, 'Feature')

        article_template = self.init_template('Article', 'compose/page_article.html', [slideshow_section, body_section, card_section])
        feature_template = self.init_template('Plans', 'compose/page_feature.html', [header_a_section, feature_a_section])
        gallery_template = self.init_template('Gallery', 'compose/page_gallery.html', [gallery_section])
        brochure_template = self.init_template('Brochure', 'compose/page_brochure.html', [brochure_section])

        page_home = self.init_page(Page.HOME, '', 'Home', 1, article_template, is_home=True)
        page_feature = self.init_page('plans', '', 'Plans', 2, feature_template)
        page_gallery = self.init_page('gallery', '', 'Gallery', 3, gallery_template)
        page_brochure = self.init_page('brochure', '', 'Brochure', 4, brochure_template)

        page_home_body_section = PageSection.objects.init_page_section(page_home, body_section)
        page_home_card_section = PageSection.objects.init_page_section(page_home, card_section)
        page_home_slideshow_section = PageSection.objects.init_page_section(page_home, slideshow_section)
        page_feature_header_a_section = PageSection.objects.init_page_section(page_feature, header_a_section)
        page_feature_feature_a_section = PageSection.objects.init_page_section(page_feature, feature_a_section)
        page_gallery_gallery_section = PageSection.objects.init_page_section(page_gallery, gallery_section)
        page_brochure_brochure_section = PageSection.objects.init_page_section(page_brochure, brochure_section)


        print("Pages created")

        # Link wizard
        Url.objects.init_pages()
        home_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_home)
            )
        feature_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_feature)
            )
        gallery_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_gallery)
            )
        brochure_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_brochure)
            )

        page_link = {
            'name': 'page_link',
            'class': 'quicklist',
            'splutter': 20,
            'data': [feature_link, gallery_link, brochure_link],
        }
        print("Links created")


        maker = IMakeData(12)
        my_data_set = maker.get_dataset([
                                        heading_level,
                                        news_title,
                                        short_blurb,
                                        css_width,
                                        text_position,
                                        image_size,
                                        iconic_image,
                                        page_link,
                                        ])
        cnt = 1

        menu = Menu(slug='main', title=biz['company_name'], navigation=True)
        menu.save()
        feature_item = MenuItem(menu=menu, slug='feature_link',
                            title='Chart', order=1, link=feature_link)
        feature_item.save()
        gallery_item = MenuItem(menu=menu, slug='gallery_link',
                            title='Gallery', order=2, link=feature_link)
        gallery_item.save()
        brochure_item = MenuItem(menu=menu, slug='brochure_link',
                            title='Brochure', order=3, link=feature_link)
        brochure_item.save()
        # menu_item = MenuItem(menu=menu, slug='demos', title='Demos', order=2)
        # menu_item.save()
        # sub_menu_item = MenuItem(
        #     menu=menu, slug='feature-demo', parent=menu_item,
        #     title='Feature Demo', order=1, link=feature_link
        #)
        # sub_menu_item.save()
        # sub_menu_item = MenuItem(
        #     menu=menu, slug='header-demo', parent=menu_item,
        #     title='Header Demo', order=2, link=header_link
        #)
        # sub_menu_item.save()
        print("Menu created")


        row_break_style = self.init_featurestyle('row_break', 'col-12 w-100')
        jumbotron_style = self.init_featurestyle('jumbotron', 'jumbotron')
        print("Styles created")


        maker = IMakeData(12)
        my_data_set = maker.get_dataset([
                                        heading_level,
                                        news_title,
                                        short_blurb,
                                        css_width,
                                        text_position,
                                        image_size,
                                        iconic_image,
                                        page_link,
                                        ])
        cnt = 1
        for ds in my_data_set:
            art = Article.objects.create_article(
                                        page_home_body_section,
                                        ds['heading_level'],
                                        ds['news_title'],
                                        ds['short_blurb'],
                                        css_width=settings.CSS_WIDTH_THIRDS if cnt < 7 else ds['css_width'],
                                        article_type=ds['text_position'],
                                        image_size=ds['image_size'],
                                        )
            art.picture = ds['iconic_image'] if ds['iconic_image'] else None
            art.link = ds['page_link'] if ds['page_link'] else None
            art.save()
            art.block.publish(staff_user)
            cnt += 1
            #next article

        card_style = self.init_featurestyle('card', 'card')
        card_light_img_overlay_style = self.init_featurestyle('card light img overlay', 'card img-overlay')
        card_dark_img_overlay_style = self.init_featurestyle('card dark img overlay', 'card img-overlay card-inverse')
        card_primary_style = self.init_featurestyle('card primary', 'card card-inverse card-primary')
        card_success_style = self.init_featurestyle('card success', 'card card-inverse card-success')
        card_info_style = self.init_featurestyle('card info', 'card card-info')
        card_warning_style = self.init_featurestyle('card warning', 'card card-warning')
        card_danger_style = self.init_featurestyle('card danger', 'card card-inverse card-danger')

        card_style = {
            'name': 'card_style',
            'class': 'quicklist',
            'data': [card_primary_style, card_success_style, card_info_style,
                    card_warning_style, card_danger_style, card_style,],
        }
        overlay_style = {
            'name': 'overlay_style',
            'class': 'quicklist',
            'data': [card_light_img_overlay_style, card_dark_img_overlay_style,],
        }
        overlay_style = {
            'name': 'overlay_style',
            'class': 'quicklist',
            'data': [card_light_img_overlay_style, card_dark_img_overlay_style,],
        }
        maker = IMakeData(9)
        panel_count = 0
        my_data_set = maker.get_dataset([
                                        heading_level,
                                        news_title,
                                        description,
                                        inspirational_image,
                                        page_link,
                                        card_style,
                                        overlay_style,
                                        in_3,
                                        ])

        for ds in my_data_set:
            art = Feature.objects.create_feature(
                                        page_home_card_section,
                                        ds['heading_level'],
                                        ds['news_title'],
                                        ds['description'],
                                        css_width=settings.CSS_WIDTH_THIRDS,
                                        style=ds['card_style'],
                                        )
            if ds['inspirational_image']:
                art.picture = ds['inspirational_image']
                if ds['in_3'] == 1:
                    art.style = ds['overlay_style']
            art.link = ds['page_link'] if ds['page_link'] else None
            art.save()
            art.block.publish(staff_user)

        maker = IMakeData(1)
        panel_count = 0
        my_data_set = maker.get_dataset([
                                        heading_level,
                                        news_title,
                                        tweet,
                                        css_width,
                                        ])

        for ds in my_data_set:
            art = Slideshow.objects.create_slideshow(
                                        page_home_slideshow_section,
                                        ds['heading_level'],
                                        ds['news_title'],
                                        ds['tweet'],
                                        css_width=ds['css_width'],
                                        )
            art.save()
            slides = [images['bg'][0], images['bg'][1], images['bg'][2]]
            self.add_gallery_images(art, slides)
            art.block.publish(staff_user)

        print("Home Page created")

        plan_style = self.init_featurestyle('plan item', 'card text-center')
        plan_row_head_style = self.init_featurestyle('plan row header', 'card card-info text-center')
        plan_corner_style = self.init_headerstyle('plan corner', 'col card text-center')
        plan_column_head_style = self.init_headerstyle('plan column header', 'col card card-primary text-center')

        plan = {
            'headings': ['Compare plans', 'Free', 'Bronze', 'Silver', 'Golden', 'Diamond',],
            'options': {
                'disk_space': ['100 GB', '250 GB', '500 GB', '1 TB', '2 TB',],
                'ghz': ['2.8 GHz','3 GHz', '3.2 GHz', '3.5 GHz', '3.8 GHz',],
                'data_speed': ['500 kbps', '1 mbps', '5 mbps', '20 mbps', '50 mbps',],
                'support':['None', 'Help Desk', 'Support', 'Technical Support', 'Development',],
                'users': ['1 User', '5 Users', '30 Users', 'Site', 'Institution',],
                'price': ['$0 per month', '$5 per month', '$300 per year', '$1500 per year', '$2500 per year',],
                }
        }

        # write column heading
        is_first = True
        for heading in plan['headings']:
            art = Header.objects.create_header(
                                        page_feature_header_a_section,
                                        heading,
                                        style=plan_corner_style if is_first else plan_column_head_style,
                                        )
            art.block.publish(staff_user)
            is_first = False

        for k, v in plan['options'].items():

            # write row heading
            heading = k.replace('_', ' ').title()
            art = Feature.objects.create_feature(
                                        page_feature_feature_a_section,
                                        H5,
                                        heading,
                                        '',
                                        css_width=settings.CSS_WIDTH_AUTO,
                                        style=plan_row_head_style,
                                        )
            art.block.publish(staff_user)

            # write row values
            for comp in v:
                art = Feature.objects.create_feature(
                                        page_feature_feature_a_section,
                                        '',
                                        '',
                                        comp,
                                        css_width=settings.CSS_WIDTH_AUTO,
                                        style=plan_style,
                                        )
                art.block.publish(staff_user)

            # Force a new row
            art = Feature.objects.create_feature(
                                    page_feature_feature_a_section,
                                    '',
                                    '',
                                    '',
                                    css_width=settings.CSS_WIDTH_AUTO,
                                    style=row_break_style,
                                    )
            art.block.publish(staff_user)
            #next option k, v

        print("Plans Page created")


        maker = IMakeData(1)
        panel_count = 0

        for gallery_name, gallery in images.items():
            title = gallery_name.replace('_', ' ').title()
            art = Slideshow.objects.create_slideshow(
                                        page_gallery_gallery_section,
                                        H2,
                                        title,
                                        'Images from {}:'.format(title),
                                        css_width=settings.CSS_WIDTH_FULL,
                                        )
            art.save()
            self.add_gallery_images(art, gallery)
            art.block.publish(staff_user)

        print("Gallery Page created")


        brochure_style = self.init_featurestyle('brochure image', 'card img-overlay card-inverse align-middle')
        brochure_primary = self.init_featurestyle('brochure primary', 'card card-primary card-inverse align-middle')
        brochure_success = self.init_featurestyle('brochure success', 'card card-success card-inverse align-middle')
        brochure_info = self.init_featurestyle('brochure info', 'card card-info align-middle')
        brochure_white = self.init_featurestyle('brochure white', 'card align-middle')


        brochure_image = {
            'name': 'brochure_image',
            'class': 'quicklist',
            'splutter': 70,
            'data': images['bg'],
        }

        coloured_brochure_style = {
                        'name': 'coloured_brochure_style',
                        'class': 'quicklist',
                        'data': [brochure_primary, brochure_white,
                                brochure_success, brochure_info],
        }

        maker = IMakeData(12)
        my_data_set = maker.get_dataset([
                                        news_title,
                                        short_blurb,
                                        brochure_image,
                                        coloured_brochure_style,
                                        page_link,
                                        ])
        cnt = 1
        for ds in my_data_set:
            art = Feature.objects.create_feature(
                                        page_brochure_brochure_section,
                                        H2,
                                        ds['news_title'],
                                        ds['short_blurb'],
                                        css_width=settings.CSS_WIDTH_FULL,
                                        style=ds['coloured_brochure_style'],
                                        )
            if ds['brochure_image']:
                art.style = brochure_style
                art.picture = ds['brochure_image']
            art.link = ds['page_link'] if ds['page_link'] else None
            art.save()
            art.block.publish(staff_user)
            cnt += 1
            #next article

        print("Brochure Page created")


        ft = HeaderFooter.load()
        ft.company_name = biz['company_name']
        ft.footer_left_header = 'VAT'
        ft.footer_left = """
            <p> No GB 111 2323 99</p>
            """
        ft.footer_right_header = 'Mission'
        ft.footer_right = biz['tweet']
        ft.company_address =  '{}, {}, {}, {}, {} {}'.format(
                                                            biz['company_address1'],
                                                            biz['company_address2'],
                                                            biz['company_geo_location']['city'],
                                                            biz['company_geo_location']['region'],
                                                            biz['company_geo_location']['country'],
                                                            biz['company_post_code'],
                                                        )
        ft.company_phone = biz['company_phone']
        ft.company_fax = biz['company_fax']
        ft.company_email = biz['company_email']
        ft.company_hours = 'Mon - Thur 9am - 5pm (excl Bank Holidays) & Fri 9am - 4pm.'
        ft.google_verification_code = ''
        ft.google_analytics_code = 'UA-12345678-1'
        ft.google_map_long = biz['company_geo_location']['long']
        ft.google_map_lat = biz['company_geo_location']['lat']
        ft.google_map_zoom = 15
        ft.url_twitter = 'http://twitter.com/{}'.format(biz['company_slug'])
        ft.url_linkedin = 'http://linkedin.com/{}'.format(biz['company_slug'])
        ft.url_facebook = 'http://facebook.com/{}'.format(biz['company_slug'])
        ft.save()

        print("Content created")
