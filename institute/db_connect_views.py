from django.shortcuts import render
from institute import response_views
import xlwt
from django.http import HttpResponse

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

def table1p1p2and1p2p2(request):
    #Check DB Connectivity
    dict=getWorkbookAndWorksheet('1.1.2 and 1.2.2')
    wb= dict[workbook]
    ws= dict[worksheet]
    response= dict['response']
    ws.write(0,0, 'Programme Code')
    ws.write(0,1, 'Programme name')
    ws.write(0,2, 'Year of Introduction')
    ws.write(0,3, 'Status if implementation of CBCS/ECS')
    ws.write(0,4, 'Year of Implementation of CBCS/ECS')
    ws.write(0,5, 'Year of Revision')
    ws.write(0,6, 'Percent of Content Modified')
    ws.write(0,7, 'Link to Document')
    wb.save(response)
    return response_views.excel_file_report(response)

def table1p1p3and1p2p1(request):
    #check DB Connectivity
    dict = getWorkbookAndWorksheet('1.1.3 and 1.2.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the Course')
    ws.write(0,1, 'Course Code')
    ws.write(0,2, 'Activities/Content with direct bearing on Employability/ Entrepreneurship/ Skill development')
    ws.write(0,3, 'Year of introduction (during the last five years)')
    ws.write(0,4, 'Link to the relevant document')
    wb.save(response)
    return response_views.excel_file_report(response)

def table1p3p2and1p3p3(request):
    #chaeck Databae connectivity
    dict = getWorkbookAndWorksheet('1.3.2 and 1.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,0,0,6,'Year1')
    ws.write(1,0,'Name of the value added courses (with  30 or more contact hours)offered')
    ws.write(1,1, 'Course Code(if any)')
    ws.write(1,2, 'Year of offering')
    ws.write(1,3, 'No. of times offered during the same year')
    ws.write(1,4, 'Duration of Course')
    ws.write(1,5, 'Number of students enrolled in the year')
    ws.write(1,6,'Number of Students completing the course  in the year')
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p1p1(request):
    # chaeck Databae connectivity
    dict = getWorkbookAndWorksheet('2.1.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,0,0,3,'Year1')
    ws.write(1,0,'Programme name')
    ws.write(1,1, 'Programme Code')
    ws.write(1,2, 'Number of seats sanctioned')
    ws.write(1,3, 'Number of students admitted')
    wb.save(response)
    return response_views.excel_file_report(response)


def table2p1p2(request):
    #Check db connection
    dict = getWorkbookAndWorksheet('2.1.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,0,1,6,'Number of  seats earmarked for reserved category as per GOI or State ')
    ws.write_merge(0,0,7,12,'Number of students admitted from the reserved category')
    ws.write(1,1,'SC')
    ws.write(1,2,'ST')
    ws.write(1,3,'OBC')
    ws.write(1,4,'Divyangjan')
    ws.write(1,5,'GEN')
    ws.write(1,6,'Others')
    ws.write(1, 7, 'SC')
    ws.write(1, 8, 'ST')
    ws.write(1, 9, 'OBC')
    ws.write(1, 10, 'Divyangjan')
    ws.write(1, 11, 'GEN')
    ws.write(1, 12, 'Others')
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p4p2and3p2p3and3p4p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('2.4.2 and 3.2.3 and 3.4.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the Research scholar')
    ws.write(0,1,'Year of registration of the scholar ')
    ws.write(0,3, 'Guide allotment letter web link to be provided ')
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p5p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('2.5.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,0,0,4,'Year1')
    ws.write(1,0,'Programme Name')
    ws.write(1,1, 'Programme Code')
    ws.write(1,2, 'Semester/ year')
    ws.write(1,3, 'Last date of the last semester-end/ year- end examination')
    ws.write(1,4, 'Date of declaration of results of semester-end/ year- end examination')
    wb.save(response)
    return response_views.excel_file_report(response)


def table2p6p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('2.6.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Program Code')
    ws.write(0, 1, 'Program Name')
    ws.write(0, 2, 'Number of students appeared in the final year examination')
    ws.write(0, 3, 'Number of students passed in final year examination')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p2p1and3p2p2and3p2p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.2.1 and 3.2.2 and 3.2.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Sl.no.')
    ws.write(0, 1, 'Name of the Principal Investigator/ Co Investigator (if applicable)')
    ws.write(0, 2, 'Name of the Funding agency ')
    ws.write(0, 3, 'Type (Government/Non-Government)')
    ws.write(0, 4, 'Department of Principal Investigator/ Co Investigator')
    ws.write(0, 5, 'Year of Award')
    ws.write(0, 6, 'Funds provided (INR in lakhs) ')
    ws.write(0, 7, 'Duration of the project')
    wb.save(response)
    return response_views.excel_file_report(response)


def table3p3p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.3.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Name of the workshop/ seminar')
    ws.write(0,2, 'Number of Participants')
    ws.write(0,3, 'Date From – To')
    ws.write(0,4, 'Link to the Activity report on the website')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p4p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.4.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Sl. No.')
    ws.write(0,1, 'Name of the teacher')
    ws.write(0,2, 'Title of the book/chapters  published')
    ws.write(0,3, 'Title of the paper')
    ws.write(0,4, 'Title of the proceedings of the conference')
    ws.write(0,5, 'Year of publication')
    ws.write(0,6,'ISBN/ISSN number of the proceeding')
    ws.write(0,7,'Whether at the time of publication Affiliating Institution  Was same Yes/NO')
    ws.write(0,8, 'Name of the publisher')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p6p2and3p6p2p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.6.2 and 3.6.2.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the activity')
    ws.write(0,1, 'Name of the Award/recognition')
    ws.write(0,2, 'Name of the Awarding government/ government recognised bodies')
    ws.write(0,3, 'Year of Award')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p6p3and3p6p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.6.3 and 3.6.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the activity')
    ws.write(0,1, 'Organising unit/ agency/ collaborating agency')
    ws.write(0,2, 'Name of the scheme')
    ws.write(0,3, 'Year of the activity ')
    ws.write(0,4, 'Number of students participated in such activities')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p7p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.7.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Sl. No.')
    ws.write(0,1, 'Title of the collaborative activity')
    ws.write(0,2, 'Name of the collaborating agency with contact details')
    ws.write(0,3, 'Name of the participant ')
    ws.write(0,4, 'Year of collaboration')
    ws.write(0,5, 'Duration')
    ws.write(0,6,'Nature of the activity')
    ws.write(0,7,'Link to the relavant document')
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p7p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.7.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Organisation with which MoU is signed')
    ws.write(0,1, 'Name of the institution/ industry/ corporate house')
    ws.write(0,2, 'Year of signing MoU')
    ws.write(0,3, 'Duration')
    ws.write(0,4, 'List the  actual  activities under each MOU year-wise')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p1p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('4.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Room number or Name  of classrooms/Seminar Hall with LCD / wifi/LAN facilities with room numbers')
    ws.write(0,1, 'Type of ICT facility')
    ws.write(0,2, 'Link to geo tagged photos and master time table')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p1p4and4p4p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('4.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Budget allocated for infrastructure augmentation')
    ws.write(0, 2, 'Expenditure for infrastructure augmentation')
    ws.write(0, 3, 'Total expenditure excluding Salary')
    ws.write(0, 4, 'Expenditure on maintenace of academic facilities (excluding salary for human resources) ')
    ws.write(0, 5, 'Expenditure on maintenance of physical facilities (excluding salary for human resources) ')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p2p2and4p2p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('4.2.2 and 4.2.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,0,0,4, 'Year1')
    ws.write(1,0,'Library resources')
    ws.write(1,1, 'If yes, details of memberships/subscriptions ')
    ws.write(1,2, 'Expenditure on subscription to e-journals,  e-books (INR in lakhs)')
    ws.write(1,3, 'Total Library Expenditure')
    ws.write(1,4, 'Link to the relevant document')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p3p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('4.3.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the teacher')
    ws.write(0,1, 'Name of the module developed')
    ws.write(0,2, 'Platform on which module is developed')
    ws.write(0,3, 'Date of launching e content')
    ws.write(0,4, 'Link to the relevant document and facility available in the institution')
    ws.write(0,5, 'List of the e-content development facility available ')
    ws.write(0,6, 'Provide link to videos of the media centre and recording facility')
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p1p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the capability enhancement program')
    ws.write(0,1, 'Date of implementation (DD-MM-YYYY)')
    ws.write(0,2, 'Number of students enrolled')
    ws.write(0,3, 'Name of the agencies/consultants involved with contact details (if any)')
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p1p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.1.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,0,1,2,'Name of the Activity conducted by the HEI  to offer guidance for  competitive examinations offered by the institution during the last five years ')
    ws.write(1,1, 'Name of the Activity conducted by the HEI  to offer guidance for  competitive examinations/ career counselling offered by the institution during the last five years ')
    ws.write(1,2, 'Number of students attended / participated')
    ws.write_merge(0, 1, 3, 3, 'Number of students placed  through campus placement')
    ws.write_merge(0, 1, 4, 4, 'Link to the relevant document')
    wb.save(response)
    return response_views.excel_file_report(response)


def table5p3p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Date of event/competition (DD-MM-YYYY)')
    ws.write(0,2, 'Name  of the event/competition')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p2p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.2.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Areas of e governance')
    ws.write(0, 1, 'Year of implementation')
    ws.write(0, 2, 'Link to relevant website/ document')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Dates (from-to) (DD-MM-YYYY)')
    ws.write(0, 1, 'Title of the professional development/ administrative training programs organised for teaching staff(Professional development / administrative training programs)')
    ws.write(0, 2, 'No. of participants')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p4p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.4.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Name of the non government funding agencies/ individuals')
    ws.write(0, 2, 'Purpose of the Grant')
    ws.write(0, 3, 'Funds/ Grants received (INR in lakhs)')
    ws.write(0, 4, 'Link to Audited Statement of Accounts reflecting the receipts')
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p5p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.5.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Conferences, Seminars, Workshops on quality conducted ')
    ws.write(0, 2, 'Academic Administrative Audit (AAA) and initiation of follow up action')
    ws.write(0, 3, 'Participation in NIRF along with Status. ')
    ws.write(0, 4, 'ISO Certification.  and nature and validity period')
    ws.write(0, 5, 'NBA or any other certification received with program specifications.')
    ws.write(0, 6, 'Collaborative quality initiatives with other institution(s) (Provide name of the institution and activity')
    ws.write(0, 7, 'Orientation programme on quality issues for teachers and students organised by the institution, Date (From-To) (DD-MM-YYYY)')
    wb.save(response)
    return response_views.excel_file_report(response)


def displayhome(request):
    return response_views.htmlpage(request,'institute/home.html', {})


