from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import FileUploadForm
from .models import uploadFile
import csv
import json
from io import StringIO, TextIOWrapper
import os

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            return render(request, 'success.html', {
                'message': f'{uploaded_file.file.name} uploaded successfully!',
                'file_id': uploaded_file.id
            })
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def download_file_as_json(request, file_id):
    uploaded_file = get_object_or_404(uploadFile, id=file_id)
    file_path = uploaded_file.file.path
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.csv':
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    elif file_ext == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        return HttpResponse(status=400)  # Bad request

    response = JsonResponse(data, safe=False)
    response['Content-Disposition'] = f'attachment; filename="{os.path.splitext(uploaded_file.file.name)[0]}.json"'
    return response
