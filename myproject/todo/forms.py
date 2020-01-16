from django import forms



class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

