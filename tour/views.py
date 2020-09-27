from django.shortcuts import render, redirect
from .models import Tour, Story
from . forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def tour(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours.html', context)


def story(request):
    stories = Story.objects.all()
    context = {'stories': stories}
    return render(request, 'stories.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            message_name = cd['full_name']
            message = cd['message']
            message_email = cd['email']

            send_mail(
                message_name,
                message,
                message_email,
                ['dorothyvic24@gmail.com']
            )
            context = {'message_name': message_name}
            return render(request, 'contact.html', context)

    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)

