from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# READ - list students
def student_list(request):
    query = request.GET.get('search')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/list.html', {'students': students})

# CREATE - add student
def student_add(request):
    if request.method == 'POST':
        age = int(request.POST['age'])

        if age < 16 or age > 60:
            return render(request, 'students/add.html', {
                'error': 'Age must be between 16 and 60'
            })

        Student.objects.create(
            name=request.POST['name'],
            age=age,
            department=request.POST['department'],
            email=request.POST['email']
        )
        return redirect('student_list')

    return render(request, 'students/add.html')


# UPDATE - edit student
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        age = int(request.POST['age'])

        if age < 16 or age > 60:
            return render(request, 'students/edit.html', {
                'student': student,
                'error': 'Age must be between 16 and 60'
            })

        student.name = request.POST['name']
        student.age = age
        student.department = request.POST['department']
        student.email = request.POST['email']
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit.html', {'student': student})


# DELETE - remove student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')