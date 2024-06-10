from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64
import os
from pandas.errors import EmptyDataError


# For handling upload file:
def handle_uploaded_file(f):
    file_path = 'uploaded_file.csv'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    if os.path.getsize(file_path) == 0:
        raise ValueError("Uploaded file is empty")
    
    return file_path

# For Analysing Data:

def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError("The uploaded file is empty or invalid.")
    except EmptyDataError:
        return {
            'error': 'The uploaded file is empty or invalid. Please upload a valid CSV file.'
        }
    
    head = data.head()
    summary = data.describe()
    missing_values = data.isnull().sum().to_frame(name='Missing Values')

    # Create plots
    fig, ax = plt.subplots()
    sns.histplot(data, ax=ax)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    context = {
        'head': head.to_html(),
        'summary': summary.to_html(),
        'missing_values': missing_values.to_html(),
        'plot': uri,
    }
    return context


from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file_path = handle_uploaded_file(request.FILES['file'])
                context = analyze_data(file_path)
                return render(request, 'analysis.html', context)
            except ValueError as e:
                context = {'error': str(e)}
                return render(request, 'analysis.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

