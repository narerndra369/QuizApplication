from django.shortcuts import render
from .models import Question
import random

from django.shortcuts import render,redirect
from .models import Question
import random

username=" "
def home(request):
    global username
    if request.method == 'POST':
        username = request.POST.get('uname','guest')
        print(username)
        return redirect('quiz')
    return render(request,'index.html')


def quiz(request):
    global username
    if 'randomQuestions' in request.session:
        randomQuestions = Question.objects.filter(id__in=request.session['randomQuestions'])
    else:
        questionsList = list(Question.objects.all())
        randomQuestions = random.sample(questionsList, len(questionsList))
        request.session['randomQuestions'] = [q.id for q in randomQuestions]

    if request.method == 'POST':
        score,unanswered,answered = 0,0,0
        print(request.POST)
        
        for ques in randomQuestions:
            useranswer = request.POST.get(str(ques.id))  
            print(f"Question ID: {ques.id}, User Answer: {useranswer}, Correct Answer: {ques.answer}")
            if useranswer == ques.answer:
                score += 1
            if useranswer == None:
                unanswered += 1
            else:
                answered += 1
            

        del request.session['randomQuestions']
        print('username',username)
        return render(request, "quizResult.html", {"Score": [score,answered,unanswered,username]})

    return render(request, "quiztemp.html", {"questions": randomQuestions,"uname":username})
