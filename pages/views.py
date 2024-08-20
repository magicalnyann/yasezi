from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Lounge
from .forms import LoungeForm

def commu(request):
    lounges = Lounge.objects.all().order_by('-pub_date')
    paginator = Paginator(lounges, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/commu.html', {'page_obj': page_obj})


def add_lounge(request):
    if request.method == 'POST':
        form = LoungeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('commu')
    else:
        form = LoungeForm()

    return render(request, 'pages/add_lounge.html', {'form': form})


def lounge_detail(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)

    return render(request, 'lounge_detail.html', {'lounge': lounge})


def event(request):
    return render(request,'pages/event.html')
