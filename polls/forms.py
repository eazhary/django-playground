from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, TabHolder,Tab
from django_countries.fields import LazyTypedChoiceField

from .models import Album
from django_countries  import countries

class EmailForm(forms.Form):
    name = forms.CharField()
    check = forms.BooleanField()
    address = forms.CharField(widget=forms.Textarea)
    address2 = forms.ChoiceField(choices=(('BT-J1KND-A', 'BT-J1KND-A'),('BT-J1KND-B', 'BT-J1KND-B'),))
#    image = forms.ImageField()
    time = forms.TimeField(required=False)
    email = forms.EmailField(label="Enter Email", max_length=50)
    country = LazyTypedChoiceField(choices=countries)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'POST'
        #self.helper.form_action = 'index2'
        self.helper.layout = Layout(
            'address','time','email','check','country',
           #  StrictButton('Sign in', css_class='btn-default'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
#            #Submit('cancel', 'Cancel'),
            Button('cancel', 'Cancel',css_class="btn-primary", onclick='history.go(-1);')
        )
        )
        #self.helper.add_input(Submit('submit', 'Submit'))


