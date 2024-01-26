from django.shortcuts import render
from .models import StudentInfo

# Create your views here.
def student_list(request):
    students = StudentInfo.objects.all()
    students_with_start_date = None
    male_students = None
    female_students = None
    students_by_currency = None

    filters_applied = 'start_date' in request.GET or 'genero' in request.GET or 'moneda' in request.GET

    if filters_applied:
        if 'start_date' in request.GET:
            students_with_start_date = students.exclude(fecha_inicio_ucamp__isnull=True)

        genero_filter = request.GET.get('genero')
        if genero_filter == 'Masculino':
            male_students = students.filter(genero='Masculino')
        elif genero_filter == 'Femenino':
            female_students = students.filter(genero='Femenino')

        moneda_filter = request.GET.get('moneda')
        if moneda_filter:
            students_by_currency = students.filter(moneda=moneda_filter)

    total_students = students.count()

    return render(request, 'student_list.html', {
        'students': students,
        'total_students': total_students,
        'students_with_start_date': students_with_start_date,
        'male_students': male_students,
        'female_students': female_students,
        'students_by_currency': students_by_currency,
        'filters_applied': filters_applied
    })
