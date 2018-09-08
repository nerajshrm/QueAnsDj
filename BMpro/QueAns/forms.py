from django import forms
from QueAns.models import choiceModel,YourchoiceModel


# QuesForm is used in one of the view to display the Questions and its options

class QuesForm(forms.ModelForm):
    class Meta():
        model = choiceModel
        fields = '__all__'

# ChoiceForm is used to let the user give his answer in 'your ans ' field
# which then will be used to check against the 'ans' field

class ChoiceForm(forms.ModelForm):
    class Meta():
        model = YourchoiceModel
        fields = {'choice'}
