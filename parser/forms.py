from django import forms
from . import parser, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('WINTER_TIRES', "WINTER_TIRES"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == "WINTER_TIRES":
            tires_parser = parser.parser()
            for i in tires_parser:
                models.TvParser.objects.create(**i)