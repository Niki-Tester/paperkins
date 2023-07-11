from django import forms
from multiupload.fields import MultiImageField
from .widgets import CustomClearableFileInput
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        widget=CustomClearableFileInput(attrs={"allow_multiple_selected": True}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
