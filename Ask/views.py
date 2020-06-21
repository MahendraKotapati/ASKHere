from django.shortcuts import render
from  .models import *
from .forms import *
from datetime import datetime

# Create your views here.
def index(request): 
    topics_id = UserInterest.objects.filter(user_id_id=1).values('interest_id_id') 
    questions = Question.objects.filter(topic_id_id__in=topics_id)   # in operator in sql 
    answers = dict()  # stores question_object as key and answers_list as value 
    for i in questions:
        answers[i] = Answer.objects.filter(que_id_id=i.id)

    context = {'page':'home','answers':answers}

    return render(request,'index.html',context)

def filter_view(request,topic_id):

    #topic_id = request.GET['topic_id']
    questions = Question.objects.filter(topic_id_id=topic_id)   # in operator in sql 
    answers = dict()  # stores question_object as key and answers_list as value 
    for i in questions:
        answers[i] = Answer.objects.filter(que_id_id=i.id)
    context = {'page':'home','answers':answers}

    return render(request,'index.html',context)


def post_question(request):
    if(request.method=="POST"):
        form = QuestionForm(request.POST)
        if(form.is_valid()):
            question = form.save(commit=False)
            question.created_date = datetime.now()
            if request.user.is_anonymous:
                question.created_by = UserLogin.objects.get(pk=1)
            else:
                question.created_by =  request.user
            question.save()
            return render(request,'index.html')
    else:
        form = QuestionForm()
        return render(request,'post_question.html',{'form':form})

        

def add_answer(request,que_id):
    if(request.method=="POST"):
        form = AnswerForm(request.POST)
        if(form.is_valid()):
            answer = form.save(commit=False)
            answer.que_id = Question.objects.get(pk=que_id)
            if request.user.is_anonymous:
                answer.answerd_by = UserLogin.objects.get(pk=1)
            else:
                answer.answerd_by =  UserLogin.objects.get(pk=request.user.pk)
            answer.save()
            return render(request,'index.html')
    else:
        form = AnswerForm()
        return render(request,'add_answer.html',{'form':form})

