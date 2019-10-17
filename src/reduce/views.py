from django.shortcuts import render

from reduce.form import AddUrlForm
from reduce.models import MinUrl


def add(request):
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
        	url = form['url'].value()
        	min_url = MinUrl.create(url)
        	return render(request, 'min_url.html', {'min_url': min_url.token})

    else:
        form = AddUrlForm()

    return render(request, 'add_url.html', {'form': form})