import random
from django.shortcuts import render
from django.views import generic

# Create your views here.

class indexView(generic.TemplateView):
    template_name = "index.html"

def gameView(request):
    if request.GET.get('choice'):
        option = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(option)
        user_choice = request.GET.get('choice')
        score = 0
        msg1 = f"computer_choice: {computer_choice}"
        msg2 = f"Your choice: {user_choice}"

        if computer_choice == user_choice:
            msg3 = 'A tie'
            context = {
                'computer_choice': msg1,
                'user_choice': msg2,
                'decision': msg3
            }
            return render(request, 'game.html', context)


        else:
            # here three things can occur as follows:
            # 1: the user choose rock and computer choose either paper or scissors
            # 2: or the user choose paper and computer choose either rock or scissors
            # 3: or finally the user choose scissors and computer choose either rock or paper
            # in order words the user and computer will not choose the samething 

            # 1: the user choose rock and computer choose either paper or scissors
            if user_choice == 'rock':
                if computer_choice == 'paper':
                    msg3 = 'paper wraps rock, you lose!!!'
                else: # then computer choice will be scissors
                    msg3 = 'rock breaks scissors, you win!!!'

            # 2: the user choose paper and computer choose either rock or scissors
            elif user_choice == 'paper':
                if computer_choice == 'rock':
                    msg3 = 'you win your paper wraps the computer\'s rock '
                else: # then the computer choice will be scissors
                    msg3 = 'your lose computer scissor\'s cut your paper'
            
            # 3: the user choose scissors and computer choose either rock or paper
            elif user_choice == 'scissors':
                if computer_choice == 'rock':
                    msg3 = 'you lose computer\'s rock break your scissors'
                else: # then the computer choice will paper
                    msg3 = 'you win, your scissors\' cut computer\'s paper'
            else:
                msg3 = 'unknown user choice'
            context = {
                'computer_choice': msg1,
                'user_choice': msg2,
                'decision': msg3
            }
            return render(request, 'game.html', context)
            
    return render(request, 'game.html')

  
