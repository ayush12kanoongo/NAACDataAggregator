from django.shortcuts import render
from student import response_views
import xlwt
from django.http import HttpResponse
from loginandregister.models import Alluser
from student.models import *
from django.contrib.auth.models import User
from django.db.models import Model
#-------------

workbook='wb'
worksheet='ws'
#-----------
def getWorkbookAndWorksheet(filename):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="'+filename+'.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('New Sheet')
    return {workbook:wb,worksheet:ws,'response':response}

def table1p3p4and1p3p4p1(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('1.3.4 and 1.3.4.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Program name')
    ws.write(0,1, 'Program Code')
    ws.write(0,2, 'Name of students undertaking field projects /internships/student projects')
    ws.write(0,3, 'Link to the relevant document')

    placement_list= Placement_internship_project.objects.raw("SELECT * FROM public.student_placement_internship_project WHERE internship_project_name IS NOT NULL;")
    row=1
    for obj in placement_list:
        ws.write(row, 0, obj.student.prog.prog_name)
        ws.write(row, 1, obj.student.prog.prog_code)
        ws.write(row, 2, obj.student.student.user.first_name+' '+obj.student.student.user.last_name)
        ws.write(row, 3, obj.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)




def table2p7p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('2.7.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0,'Name of the student')
    ws.write(0, 1, 'Gender')
    ws.write(0, 2, 'Category')
    ws.write(0, 3, 'State of Domicile')
    ws.write(0, 4, 'Nationality if othern than Indian')
    ws.write(0, 5, 'Email ID')
    ws.write(0, 6, 'Programme name')
    ws.write(0, 7, 'Student Unique Enrolment ID ')
    ws.write(0, 8, 'Mobile Number')
    ws.write(0, 9, 'Year of joining')

    Student_info= student.objects.raw(
        "SELECT * FROM public.student_Student WHERE enroll_num IS NOT NULL;")
    row = 1
    for obj in Student_info:
        ws.write(row, 0, obj.student.Student.student)
        ws.write(row, 1, obj.student.Student.gender)
        ws.write(row, 2, obj.student.Student.category)
        ws.write(row, 3, obj.student.Student.state_of_domicile)
        ws.write(row, 4, obj.student.Student.nationality)
        ws.write(row, 5, obj.student.Student.email_id)
        ws.write(row, 6, obj.student.prog.prog_name)
        ws.write(row, 7, obj.student.Student.enroll_num)
        ws.write(row, 8, obj.student.Student.contact_number)
        ws.write(row, 9, obj.student.Student.year_of_admission)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p1p1and5p1p2(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.1.1 and 5.1.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,1,1,1, 'Name of Scheme')
    ws.write_merge(0,0,2,3, 'Number of students benefited by government scheme and amount')
    ws.write(1,2,'Number of Students')
    ws.write(1,3,'Amount')
    ws.write_merge(0,1,5,5,'Link to Relevant Documnet')
    row=2
    gov_objs= Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='government' GROUP BY year,scheme_name,scheme_type;")
    for obj in gov_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        row=row+1
    row=row+3
    ws.write_merge(row,row+1,0,0,'Year')
    ws.write_merge(row,row+1, 1, 1, 'Name of Scheme')
    ws.write_merge(row, row, 2, 3, "Number of students benefited by intitution's scheme and amount")
    ws.write(row+1, 2, 'Number of Students')
    ws.write(row+1, 3, 'Amount')
    ws.write_merge(row, row+1, 5, 5, 'Link to Relevant Documnet')
    row=row+2
    inst_objs = Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='institute' GROUP BY year,scheme_name,scheme_type;")
    for obj in inst_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        row = row + 1
    row = row + 3
    ws.write_merge(row, row + 1, 0, 0, 'Year')
    ws.write_merge(row, row + 1, 1, 1, 'Name of Scheme')
    ws.write_merge(row, row, 2, 4, "Number of students benefited by non-government scheme and amount")
    ws.write(row + 1, 2, 'Number of Students')
    ws.write(row + 1, 3, 'Amount')
    ws.write(row + 1, 4, 'Agency name')
    ws.write_merge(row, row + 1, 5, 5, 'Link to Relevant Documnent')
    row = row + 2
    non_gov_objs = Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,scholarship_provider,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='non-government' GROUP BY year,scheme_name,scheme_type,scholarship_provider;")
    for obj in non_gov_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        ws.write(row, 4, obj.scholarship_provider)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p1(request):
    #check database connectivity
    dict = getWorkbookAndWorksheet('5.2.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1,'Name of student placed')
    ws.write(0,2,'Program graduated from')
    ws.write(0,3,'Name of the employer')
    ws.write(0,4,'Pay package at appointment')

    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p2(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.2.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of student enrolling into higher education')
    ws.write(0,1, 'Program graduated from')
    ws.write(0,2, 'Name of institution joined')
    ws.write(0,3, 'Name of programme admitted to')
    row=1
    student_objs= Student.objects.raw("SELECT * FROM PUBLIC.student_student WHERE higher_edu_inst_joined_name IS NOT null")
    for obj in student_objs:
        ws.write(row,0, obj.student.user.first_name+' '+obj.student.user.last_name)
        ws.write(row,1, obj.prog.prog_name)
        ws.write(row,2, obj.higher_edu_inst_joined_name)
        ws.write(row,3, obj.higher_edu_prog_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p3(request): #Doubt
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.2.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,1,1,1,'Registration number/roll number for the exam')
    ws.write_merge(0,1,2,2, 'Names of students selected/ qualified')
    ws.write_merge(0, 0, 3, 14, 'Examination Qualified')
    ws.write(1, 3, 'NET')
    ws.write(1, 4, 'SLET')
    ws.write(1, 5, 'GATE')
    ws.write(1, 6, 'GMAT')
    ws.write(1, 7, 'CAT')
    ws.write(1, 8, 'GRE')
    ws.write(1, 9, 'JAM')
    ws.write(1, 10, 'IELTS')
    ws.write(1, 11, 'TOEFL')
    ws.write(1, 12, 'Civil Services')
    ws.write(1, 13, 'State government examinations')
    ws.write(1, 14, 'Other examinations conducted by the State / Central Government Agencies (Specify)')

    sports_objs = Sports_cultural_award.objects.all()
    row = 1
    for obj in sports_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.award_name)
        ws.write(row, 2, obj.team_name)
        ws.write(row, 3, obj.competition_type)
        ws.write(row, 4, obj.event_name)
        ws.write(row, 5, obj.student.student.user.first_name + ' ' + obj.student.student.user.first_name)
        row = row + 1


    wb.save(response)
    return response_views.excel_file_report(response)

def table5p3p1(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.3.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Name of the award/ medal')
    ws.write(0,2, 'Team / Individual')
    ws.write(0,3, 'inter-university / state /  National/ International')
    ws.write(0,4, 'Name of the event')
    ws.write(0,5, 'Name of the student')
    sports_objs= Sports_cultural_award.objects.all()
    row=1
    for obj in sports_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.award_name)
        ws.write(row, 2, obj.team_name)
        ws.write(row, 3, obj.competition_type)
        ws.write(row, 4, obj.event_name)
        ws.write(row, 5, obj.student.student.user.first_name+' '+obj.student.student.user.first_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)


def displayhome(request):
    #Database connectivity and data fetch
    user = request.user
    alluser = Alluser.objects.get(user=user)
    student = Student.objects.get(student=alluser)
    return response_views.htmlpage(request, 'student/home.html', {'alluser':alluser, 'student':student})


def displayacademicinfo(request):
    #Database connectivity and data fetch
    return response_views.htmlpage(request, 'student/details.html', {})
