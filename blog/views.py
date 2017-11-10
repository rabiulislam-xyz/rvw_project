from concurrent.futures import ThreadPoolExecutor

from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail

from blog.models import Post
from .forms import MessageForm


executor = ThreadPoolExecutor(10)


class HomePageTemplate(TemplateView):
    template_name = 'blog/home_page.html'


class PostList(ListView):
    model = Post
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        sent = False
        if form.is_valid():

            kwargs = {}
            kwargs['subject'] = "MESSAGE FROM MY WEBSITE"
            kwargs['message']  = form.cleaned_data.get('body','no message body found')
            kwargs['from_email'] = 'o1935926686@gmail.com'
            kwargs['recipient_list'] = ['rb60041@gmail.com']
            kwargs['fail_silently'] = False

            sent = executor.submit(send_mail, **kwargs)

            if sent:
                sent=True
        return render(request, 'blog/contact_page.html', {'sent':sent, 'form':form})

    else:
        form = MessageForm()
    return render(request, 'blog/contact_page.html', {'form':form})