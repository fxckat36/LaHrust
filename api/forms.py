from .models import feedback
from django.forms import ModelForm, TextInput, Textarea

class feedbackform(ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'comment', 'rate']

        widgets = {
            "name": TextInput(attrs= {
                "class": "form-control",
                "placeholder": "Ваше имя: "
            }),
            "comment": Textarea(attrs= {
                "class": "form-control",
                "placeholder": "Ваш комментарий: "
            }),
            "rate": TextInput(attrs= {
                "class": "form-control",
                "placeholder": "Ваша оценка: "
            })
        }