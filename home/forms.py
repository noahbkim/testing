from django import forms


class SubjectForm(forms.Form):
    """Subclass the user creation form for creating a new subject."""

    first_name = forms.CharField(min_length=1)
    last_name = forms.CharField(min_length=1)
    email = forms.EmailField()
    age = forms.IntegerField()  # Kind of arbitrary but whatever
    sex = forms.IntegerField()
    password1 = forms.CharField(strip=False, min_length=8)
    password2 = forms.CharField(strip=True)

    def clean_sex(self):
        """Check if sex is 0 or 1."""

        sex = self.cleaned_data.get("sex")
        if sex not in (0, 1):
            raise forms.ValidationError("sex must be male or female")
        return sex

    def clean_password2(self):
        """Check if the second password is the same as the first."""

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
