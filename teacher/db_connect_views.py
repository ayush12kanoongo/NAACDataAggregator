from django.shortcuts import render
from teacher import response_views
import xlwt
from django.http import HttpResponse
from loginandregister.models import Alluser
from teacher.models import *
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

def table2p4p1and2p4p3(request):
    #connect to DB
    dict = getWorkbookAndWorksheet('2.4.1 and 2.4.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of the Full-time teacher')
    ws.write(0, 1, ' PAN')
    ws.write(0, 2, ' Designation ')
    ws.write(0, 3, ' Year of  appointment ')
    ws.write(0, 4, 'Nature of appointment (Against Sanctioned post, temporary, permanent)')
    ws.write(0, 5, ' Name of the Department')
    ws.write(0, 6, ' Total years of Experience in the same institution')
    ws.write(0, 7, ' Is the teacher still serving the institution/If not last year of the service of Faculty to the Institution')
    teacher_objs= Teacher.objects.all()
    row=1
    for obj in teacher_objs:
        ws.write(row, 0, obj.teacher.user.first_name+' '+obj.teacher.user.last_name)
        ws.write(row, 1, obj.pan_no)
        ws.write(row, 2, obj.designation)
        ws.write(row, 3, obj.appointment_year)
        ws.write(row, 4, obj.nature_of_appointment)
        ws.write(row, 5, obj.prog.prog_name)
        ws.write(row, 6, obj.experience)
        ws.write(row, 7, obj.present_status)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p1p2and3p1p2p1(request): #teacher
    # connect to DB
    dict = getWorkbookAndWorksheet('3.1.2 and 3.1.2.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher provided with seed money')
    ws.write(0,1, 'The amount of seed money (INR in Lakhs)')
    ws.write(0,2, 'Year of receiving')
    ws.write(0,3, 'Link to the policy documents for Sanction of seed money / grants for research from the institution')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p1p3(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.1.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher awarded national/ international fellowship/financial support')
    ws.write(0,1, 'Name of the award/fellowship')
    ws.write(0,2, 'Year of Award')
    ws.write(0,3, 'Awarding Agency')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p4p3(request): #teacher
    # connect to DB
    dict = getWorkbookAndWorksheet('3.4.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0, 'Title of paper')
    ws.write_merge(0,1,1,1, 'Name of the author')
    ws.write_merge(0,1,2,2, 'Department of teacher')
    ws.write_merge(0,1,3,3, 'Name of journal')
    ws.write_merge(0,1,4,4, 'Year of publication')
    ws.write_merge(0,1,5,5, 'ISSN number')
    ws.write_merge(0,0,6,8, 'Link to the recognition in UGC enlistment of the Journal')
    ws.write(1,6,'Link to Website')
    ws.write(1,7, 'Link to article')
    ws.write(1,8, 'Is listed in UGC Care')
    papers_objs= Book_research_published.objects.raw("SELECT * FROM public.teacher_book_research_published WHERE type_of_publish='research paper'")
    row=2;
    for obj in papers_objs:
        ws.write(row, 0, obj.publish_title)
        ws.write(row, 1, obj.author_name)
        ws.write(row, 2, obj.teacher.prog.prog_name)
        ws.write(row, 3, obj.publisher_journal_name)
        ws.write(row, 4, obj.publication_year)
        ws.write(row, 5, obj.isbn_issn_number)
        ws.write(row, 6, obj.journal_website_link)
        ws.write(row, 7, obj.doc_link)
        ws.write(row, 8, obj.is_listed_in_ugc_care_scopus)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p4p4(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.4.4')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Sl.No')
    ws.write(0,1,'Name of the teacher')
    ws.write(0,2, 'Title of the book/chapters  published')
    ws.write(0,3,'Title of the paper')
    ws.write(0,4,'Title of the proceedings of the conference')
    ws.write(0,5,'Year of publication')
    ws.write(0,6,'ISBN/ISSN number of the proceeding')
    ws.write(0,7,'Whether at the time of publication Affiliating Institution  Was same Yes/NO')
    ws.write(0,8,'Name of the publisher')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p5p1(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.5.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher-consultants')
    ws.write(0,1, 'Name of consultancy project/corporate training program')
    ws.write(0,2, 'Consulting/Sponsoring agency with contact details')
    ws.write(0,3, 'Year')
    ws.write(0,4, 'Revenue generated (INR in Lakhs)')
    ws.write(0,5, 'Number of trainees')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p5p2(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.5.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teachers/staff')
    ws.write(0,1, 'Name of the facilities developed and department')
    ws.write(0,2, 'Agency seeking training with contact details')
    ws.write(0,3, 'Year')
    ws.write(0,4, 'Name of consultancy')
    ws.write(0,5, 'Total amount spent (INR in Lakhs)')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p3p4(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.5.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of the teacher ')
    ws.write(0, 1, 'Name of the module developed')
    ws.write(0, 2, 'Platform on which module is developed ')
    ws.write(0, 3, 'Date of launching e content ')
    ws.write(0, 4, 'Link to the relevant document and facility available in the institution ')
    ws.write(0, 5, 'List of the e-content development facility available ')
    ws.write(0, 6, 'Provide link to videos of the media centre and recording facility')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p2(request): #teacher
    # connect to DB
    dict = getWorkbookAndWorksheet('6.3.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Name of teacher')
    ws.write(0, 2, 'Name of conference/ workshop attended for which financial support provided')
    ws.write(0, 3, 'Name of the professional body for which membership fee is provided')
    ws.write(0, 4, 'Amount of support')
    ws.write(0, 5, 'Amount of support (in INR)')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p4(request): #teacher
    # connect to DB
    dict = getWorkbookAndWorksheet('6.3.4')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of teacher who attended the program')
    ws.write(0, 1, 'Title of the program')
    ws.write(0, 2, 'Duration (from – to) (DD-MM-YYYY)')
    wb.save(response)
    return response_views.excel_file_report(response)

def displayhome(request):
    # Database connectivity and data fetch
    user = request.user
    alluser = Alluser.objects.get(user=user)
    teacher= Teacher.objects.get(teacher=alluser)
    return response_views.htmlpage(request, 'teacher/home.html', {'alluser': alluser, 'teacher': teacher})

def display_criteria_page(request):
    #Database and all
    return response_views.htmlpage(request, 'teacher/criteriapage.html',{})


