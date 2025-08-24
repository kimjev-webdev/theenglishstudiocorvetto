from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Flyer


class FlyerForm(forms.ModelForm):
    description_en = forms.CharField(
        widget=CKEditorWidget()
    )
    description_it = forms.CharField(
        widget=CKEditorWidget()
    )
    extra_info_en = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )
    extra_info_it = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )

    class Meta:
        model = Flyer
        fields = [
            'title_en', 'title_it',
            'description_en', 'description_it',
            'extra_info_en', 'extra_info_it',
            'event_date',
            'image'
        ]
