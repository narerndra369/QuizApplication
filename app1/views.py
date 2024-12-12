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
    # Retrieve random questions from the session, if they exist
    global username
    if 'randomQuestions' in request.session:
        # Retrieve the questions from the session
        randomQuestions = Question.objects.filter(id__in=request.session['randomQuestions'])
    else:
        # Select random questions and store their IDs in the session
        questionsList = list(Question.objects.all())
        randomQuestions = random.sample(questionsList, len(questionsList))
        request.session['randomQuestions'] = [q.id for q in randomQuestions]

    if request.method == 'POST':
        score,unanswered,answered = 0,0,0
        print(request.POST)
        
        # Check user answers
        for ques in randomQuestions:
            useranswer = request.POST.get(str(ques.id))  # Access by question ID
            print(f"Question ID: {ques.id}, User Answer: {useranswer}, Correct Answer: {ques.answer}")
            if useranswer == ques.answer:
                score += 1
            if useranswer == None:
                unanswered += 1
            else:
                answered += 1
            

        
        # Clear the session data after the quiz is submitted
        del request.session['randomQuestions']
        print('username',username)
        return render(request, "quizResult.html", {"Score": [score,answered,unanswered,username]})

    # If it's a GET request, render the quiz with the selected questions
    return render(request, "quiztemp.html", {"questions": randomQuestions,"uname":username})
