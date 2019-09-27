from django.shortcuts import render

import reduce.identifier
from reduce.form import AddUrlForm
from reduce.models import MinUrl


def add(request):
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
        	min_url = reduce.identifier.get_new_identifier()
        	return render(request, 'min_url.html', {'min_url': min_url})

    else:
        form = AddUrlForm()

    return render(request, 'add_url.html', {'form': form})