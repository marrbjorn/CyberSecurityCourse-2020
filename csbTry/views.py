from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def formPageView(request):
    signups = request.session.get('signups', [])	
    if len(signups) == 0:
        signups.append('Bjorn Arnleifsson')
        signups.append('Torvald Algeirsson')
        signups.append('Dagbjort og FlokR')
        signups.append('Teppa Pekkanen')
        signups.append('Duck Donald')
    if request.method == 'POST':
        signup = request.POST.get('name', '')
        if len(signup) > 0:
            signups.append(signup)
            request.session['signups'] = signups
            return render(request, 'pages/done.html')
    return render(request, 'pages/form.html')

def donePageView(request):
    return render(request, 'pages/done.html')

def fylkrPageView(request):
    signups = request.session.get('signups', [])

    if int(request.GET.get('doTheTrick', '0')) == 1:
        return render(request, 'pages/fylkr.html', {'signups' : signups})
    else:
        return render(request, 'pages/done.html')

def hiddenPageView(request):
    return render(request, 'pages/hidden.html')

def csrfinerPageView(request):
    return render(request, 'pages/CSRFiner.html')

def previewPageView(request):
    return render(request, 'pages/preview.html')
