from django.http import HttpResponse

def record_list(request):
    '''書籍の一覧'''
    return HttpResponse(u'List')

def record_edit(request, record_id=None):
    '''書籍の編集'''
    return HttpResponse(u'Edit')

def record_del(request, record_id):
    '''書籍の削除'''
    return HttpResponse(u'Delete')