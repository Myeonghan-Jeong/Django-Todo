from django import forms


class Step1Form(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class Step2Form(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[("M", "Male"), ("F", "Female")])


class Step3Form(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea)
