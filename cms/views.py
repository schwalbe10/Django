from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import RecordForm, ReviewForm
from cms.models import Record, Review

def record_list(request):
    records = Record.objects.all().order_by('id')
    return render_to_response('cms/record_list.html',
                              {'records': records},
                              context_instance=RequestContext(request))  # Pass the data to the template

def record_edit(request, record_id=None):
    if record_id:   # Edit if record_id exists
        record = get_object_or_404(Record, pk=record_id)
    else:         # Add if record_id doesn't exist
        record = Record()
    
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)  # Create a form from posted request
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('cms:record_list')
    else:
        form = RecordForm(instance=record)  # Create a form from record instance
        
    return render_to_response('cms/record_edit.html',
                              dict(form=form, record_id=record_id),
                              context_instance=RequestContext(request))

def record_del(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    return redirect('cms:record_list')

class ReviewList(ListView):
    context_object_name='reviews'
    template_name='cms/review_list.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=kwargs['record_id'])
        reviews = record.reviews.all().order_by('id')
        self.object_list = reviews
        
        context = self.get_context_data(object_list=self.object_list, record=record)    
        return self.render_to_response(context)

def review_edit(request, record_id, review_id=None):
    record = get_object_or_404(Record, pk=record_id)
    if review_id:   # Edit if record_id exists
        review = get_object_or_404(Review, pk=review_id)
    else:               # Add if record_id doesn't exist
        review = Review()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)  # Create a form from posted request
        if form.is_valid():
            review = form.save(commit=False)
            review.record = record
            review.save()
            return redirect('cms:review_list', record_id=record_id)
    else:    # GET の時
        form = ReviewForm(instance=review)  # Create a form from record instance
        
    return render_to_response('cms/review_edit.html',
                              dict(form=form, record_id=record_id, review_id=review_id),
                              context_instance=RequestContext(request))

def review_del(request, record_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('cms:review_list', record_id=record_id)