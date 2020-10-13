from django.shortcuts import render , redirect ,get_object_or_404
from .models import Note
from django.contrib.auth.models import User

# Create your views here.

def notes(request):
    notes = Note.objects.all().filter(owner=request.user)
    context = {
        'notes' : notes
    }
    return render(request,'notes.html',context)

def addnote(request):
    if request.method == 'POST':
        text = request.POST['note']
        owner_id = request.POST['owner']
        owner = get_object_or_404(User,pk=owner_id)
        note = Note(text=text,owner=owner)
        note.save()
        return redirect('notes')
    return render(request,'addnote.html')

def delete(request,note_id):
    Note.objects.filter(id = note_id).delete()
    return redirect('notes')

def edit(request,note_id):
    note =  Note.objects.filter(id = note_id)[0]
    if request.method == 'POST':
        text = request.POST['note']
        note.text = text
        note.save()
        return redirect('notes')

    context = {
        "note": note
    }
    return render(request,'addnote.html',context)