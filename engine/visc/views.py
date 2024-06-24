from django.shortcuts import render
from .predict_viscosity_function import predict_viscosity
import os

def home(request):
    predicted_viscosity = 'None'
    if request.method == 'POST':
        # Get the path of the current directory where views.py resides
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Join the current directory path with the filename to get the absolute path of the joblib file
        model_path = os.path.join(current_directory, 'forest_model_v3_local.joblib')

        total_fat = float(request.POST.get('total_fat'))
        fineness = float(request.POST.get('fineness'))
        emulsifier = float(request.POST.get('emulsifier'))
        pgpr = float(request.POST.get('pgpr'))
        predicted_viscosity = predict_viscosity(
                          total_fat,
                          fineness,
                          emulsifier,
                          pgpr,
                          model_path)

        # Return a response
        # return HttpResponse(f"Predicted Viscosity is: {prediction}")
    return render(request, 'visc/home.html', {'predicted_viscosity': predicted_viscosity})



