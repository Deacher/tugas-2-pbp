from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Andhika Reihan Hervito',
        'class': 'PBP B',
        'app': 'Item Collection',
    }

    return render(request, "main.html", context)