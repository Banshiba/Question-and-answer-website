from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import questions,Comment
from django.views.generic import ListView,DetailView,CreateView
from .forms import CommentForm
from django.http import JsonResponse
from django.urls import reverse_lazy,reverse

# Create your views here.

# def index(request):
#     context={'questions':questions.objects.all()}
#     return render(request,'index.html',context)

# def about(request):

#     return render(request,'about.html',{'titles':'About'})
def question(request):
    return render(request,'Create.html',{"titles":"Questions"})

#CRUD operations





class questionsListView(ListView):
    model=questions
    template_name='index.html'
    context_object_name='questions'
    ordering=['-date']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context
class questionsDetailView(DetailView):
    model=questions
    template_name='questions_detail.html'

class questionsCreateView(CreateView):
    model=questions
    fields=['title','Content']
    template_name='questions_from.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().save()

# class CommentListView(ListView):
#     model = Comment
#     context_object_name='asnwers'
#     template_name = 'questions_detail.html'
    

class CommentDetailView (CreateView):
    model=Comment
    form_class=CommentForm
    template_name="questions_detail.html"

    

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name="questions_answer.html"

    def form_valid(self,form):
        form.instance.question_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('qs-index')



    

    






