from django.shortcuts import render


def main_view(request):
    return render(request, 'portfolio/index.html')

def persian_view(request):
    return render(request, 'portfolio/index-fa.html')
