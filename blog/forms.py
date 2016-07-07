from django.forms import ModelForm, Textarea
from blog.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'message':Textarea(attrs={'cols':46,'rows':5}),
		}

	

