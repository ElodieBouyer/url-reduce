from django.shortcuts import render

from reduce.form import AddUrlForm
from reduce.models import MinUrl


def add(request):
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = AddUrlForm()

    return render(request, 'add_url.html', {'form': form})