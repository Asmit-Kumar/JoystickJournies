from django import forms

class Feedback(forms.Form):
    Email = forms.EmailField()
    
    def _str_(self):
        return self.Email