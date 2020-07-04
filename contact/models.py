from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField   
)

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    

    contact_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6")
            ]),
            FieldPanel("Subject"),
        ], heading="Email Settings"),
        
    ]
