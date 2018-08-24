from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )

class MainLineForm(forms.Form):
	school_name = forms.CharField(required=True, label="Name")
	contact_email = forms.EmailField(required=True, label="Email")
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	#phone_number = models.CharField(validators=[phone_regex], max_length=17)
	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')