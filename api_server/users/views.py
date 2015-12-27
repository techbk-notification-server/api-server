from django.contrib.auth import authenticate, login
from django.views import generic
from django.shortcuts import redirect

class LogInView(generic.TemplateView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LogInView, self).get_context_data(**kwargs)
        return context


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/admin/')
        else:
            return super(LogInView, self).get(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/admin/')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return redirect('/login/')
        else:
            # Return an 'invalid login' error message.
            return redirect('/login/')