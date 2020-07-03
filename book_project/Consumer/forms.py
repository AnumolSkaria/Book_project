from django.forms import ModelForm
from Consumer.models import Consumer

class ConsumerRegForm(ModelForm):
    class Meta:
        model=Consumer
        fields="__all__"

        def clean(self):
            pass
class ConsumerLogin(ModelForm):
    class Meta:
        model=Consumer
        fields=["username","password"]

        def clean(self):
            # print("inside clean")
            pass