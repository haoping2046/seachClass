from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # set fields of page
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    # email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "row": 20,
                "cols": 120
            }
        )
    )

    price = forms.DecimalField(initial=199.99)

    # set model, fields
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # set validation(condition)
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        # if not "CFE" in title:
        #     raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endwith("edu"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "row": 20,
                "cols": 120
            }
        )
    )

    price = forms.DecimalField(initial=199.99)


