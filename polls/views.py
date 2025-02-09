from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here:
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return a HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice inf a user hits the BACK button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # redundant code: return HttpResponse("You're voting on question %s." % question_id)

#
# Old code before using Django Generic Views (up to pt 4 tutorial)#
#
#
# def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list,}
    # return render(request, 'polls/index.html', context)

# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question':question})
    # # Redundant code:
    # #response = "You're looking at the results of question %s."
    # #return HttpResponse(response % question_id)

# def vote(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # try:
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
        # # Redisplay the question voting form.
        # return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.", })
    # else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # # Always return a HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice inf a user hits the BACK button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # # redundant code: return HttpResponse("You're voting on question %s." % question_id)