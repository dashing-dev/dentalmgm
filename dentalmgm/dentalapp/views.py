from urllib import request
from django.shortcuts import render ,  HttpResponse , redirect
from .models import Patient, Doctor
from .forms import PatientForm
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse , reverse_lazy


# Create your views here.
def index(response):
    return render(response, "index.html", {})



def patient_list(response):
    patients = Patient.objects.all()

    return render(response, 'patientlist.html', {'patients':patients})


def patient_detail(request, pk):
    """
    View to display details of a specific patient.
    """
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})


# def add_patient(request):
#     """
#     View to handle adding a new patient.
#     """
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('patient_view')  # Redirect to the patient list view
#     else:
#         form = PatientForm()

#     # You can also pass a list of doctors to the template if needed
#     doctors = Doctor.objects.all()
   

#     return render(request, 'input.html', {'form': form, 'doctors': doctors})
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_view')
    else:
        form = PatientForm()
    doctors = Doctor.objects.all()
    return render(request, 'input.html', {'form': form, 'doctors': doctors})


def patient_view(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        
        return HttpResponse("Patient not found", status=404)

    
    context = {'patient': patient}
    return render(request, 'patient.html', context)


def patient_redirect_view(request, pk):
    patient = Patient.objects.get(pk=pk)
    return redirect(reverse_lazy('patient', args=[patient.pk]))



def view_patient(request):
 patients = Patient.objects.all()

 return render(request, 'records.html',{'patients':patients})



def patients_view(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patients.html', context)


# def search_patients(response):
#     query = request.GET.get('q', '')
#     alldetails = Patient.objects.filter(title__icontains=query)
#     output = {'alldetails':alldetails}
#     return render(response,'search.html', output)

def search_patients(request):
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST.get('search_query', '')

        # Filter the Patients model by the search query
        patients = Patient.objects.filter(name__icontains=search_query)

        return render(request, 'search.html', {'query': search_query, 'patients': patients})
    else:
        return render(request, 'search.html', {})
