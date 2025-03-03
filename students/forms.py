from django import forms


class NameForm(forms.Form):
    sem = forms.IntegerField(label="Semester")
    usn = forms.CharField(label="USN")


