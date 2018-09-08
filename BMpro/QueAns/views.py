from django.shortcuts import render,redirect
from QueAns.models import choiceModel,QuesModel,YourchoiceModel
from django.views.generic import TemplateView,DetailView,ListView
from QueAns.forms import ChoiceForm
# Create your views here.

def Index(request):
    return render(request,'index.html',{})


def QuesView(request,pk):

    question=choiceModel.objects.get(pk=pk)
    data_dict = {'stmt': question,}
    form = ChoiceForm()

    if request.method=='POST':
        form=ChoiceForm(request.POST)
        if form.is_valid:
            f=form.save(commit=False)
            qstmt=question.q
            f.stmt=qstmt
            f.ans_c=question                    # here i want to link the 'YourchoiceModel' to 'QuesModel'
            f.save()
                                                 # redirect to the next Question
        else:
            print("PLEASE SELECT THE VALID CHOICE")

    # context = super().get_context_data(**kwargs)
    context={'form':form ,'question':question}
    return render(request,'question.html',context)

def ScoreView(request):
    #find how many of the choices matche with  answers in 'YourchoiceModel'
    score=0
    pk=6
    att=YourchoiceModel.objects.all().count()
    if pk<9:
        obj_c=YourchoiceModel.objects.all().filter(pk=pk).get()
        score = score+YourchoiceModel.score(obj_c)
        pk=pk+1
    context = {'score':score}

    return render(request,'score.html',context)
