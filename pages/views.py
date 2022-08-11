from cgitb import html
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
#from .models import Images
from . models import Page
from . forms import ContactForm
from django.template.loader import render_to_string
from django.conf import settings

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list': Page.objects.all(),
    }
    #assert False
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            #con = get_connection('django.core.mail.backends.console.EmailBackend')

            subject = cd['subject']
            message = cd['message']

            html = render_to_string('pages/email.html',{
                'subject': subject,
                'message': message
            })

            send_mail(
                subject,
                message,
                cd.get('email', 'noreply@example.com'),
                [settings.EMAIL_HOST_USER],
                html_message=html,
                #connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'pages/contact.html', 
    {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})
