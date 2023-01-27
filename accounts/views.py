from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.forms import SignupForm


# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, '회원가입 환영합니다.')
            signed_user.send_welcome_email() # FIXME : Celary(비동기)로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
