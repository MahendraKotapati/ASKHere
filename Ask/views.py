from django.shortcuts import render
from  .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    
    if request.user.is_authenticated:
        user = UserLogin.objects.get(username=request.user.username)
        topics_id = UserInterest.objects.filter(user_id_id=user.id).values('interest_id_id') 
    else:
        topics_id = UserInterest.objects.all().values('interest_id_id') 

    questions = Question.objects.filter(topic_id_id__in=topics_id)   # in operator in sql 
    answers = dict()  # stores question_object as key and answers_list as value 
    for i in questions:
        answers[i] = Answer.objects.filter(que_id_id=i.id)

    context = {'page':'home','answers':answers,'user':request.user}

    return render(request,'index.html',context)

def filter_view(request,topic_id):

    #topic_id = request.GET['topic_id']
    questions = Question.objects.filter(topic_id_id=topic_id)   # in operator in sql 
    answers = dict()  # stores question_object as key and answers_list as value 
    for i in questions:
        answers[i] = Answer.objects.filter(que_id_id=i.id)
    context = {'page':'home','answers':answers}

    return render(request,'index.html',context)

@login_required(login_url='/login')
def post_question(request):
    
    if(request.method=="POST"):
        form = QuestionForm(request.POST)
        if(form.is_valid()):
            question = form.save(commit=False)
            question.created_date = datetime.now() 
            question.created_by =  UserLogin.objects.get(username=request.user.username)
            question.save()
            return render(request,'index.html',{'user':request.user})
    else:
        form = QuestionForm()
        return render(request,'post_question.html',{'form':form,'user':request.user})

        
@login_required(login_url='/login')
def add_answer(request,que_id):
    
    if(request.method=="POST"):
        form = AnswerForm(request.POST)
        if(form.is_valid()):
            answer = form.save(commit=False)
            answer.que_id = Question.objects.get(pk=que_id)
            answer.answerd_by =  UserLogin.objects.get(username=request.user.username)
            answer.save()
            return render(request,'index.html',{'user':request.user})
    else:
        question_text = Question.objects.get(pk=que_id).question_text
        form = AnswerForm()
        return render(request,'add_answer.html',{'form':form,'question_text':question_text,'user':request.user})

