from django.shortcuts import render, redirect
from .models import Job, Application
from .forms import ApplicationForm

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.applicant = request.user
            app.job = job
            app.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply.html', {'form': form})

# Create your views here.
