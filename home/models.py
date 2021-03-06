from django.db import models
from django.shortcuts import render

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

from streams import blocks


class HomePageCarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")

    carousel_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_image"),
    ]


class HomePage(RoutablePageMixin, Page):
    templates = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    content = StreamField([("cta", blocks.CTABlock()), ("table", TableBlock()),], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image"),], heading="Carousel Images"
        ),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "HOME PAGE"
        verbose_name_plural = "HOME PAGES"

    @route(r"^subscribe/$")
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(self, request, *args, **kwargs)
        return render(request, "home/subscribe.html", context)
