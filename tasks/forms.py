from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Add new task',
                                                                          'class': 'input'}))
    class Meta:
        model = Task
        fields = '__all__'