from django.shortcuts import render, redirect, get_object_or_404
from .models import VoleyPlayer
from .forms import VoleyPlayerForm

def index(request):
	return render(request,'index.html')

def view_players(request):
    players = VoleyPlayer.objects.all()
    return render(request, 'player_list.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST)
        if form.is_valid():
            playerform = form.cleaned_data
            name = playerform['name']
            date_joined = playerform['date_joined']
            position = playerform['position']
            salary = playerform['salary']
            contact_person = playerform['contact_person']
            VoleyPlayer.objects.create(
                name=name,
                date_joined=date_joined,
                position=position,
                salary=salary,
                contact_person=contact_person
            )
            return redirect('index')
        
    else:
        form = VoleyPlayerForm()

    voley_player=VoleyPlayer.objects.all()
    return render(request, 'add_player.html', {'form': form,'voley_player':voley_player})

def update_player(request, player_id):
    player = get_object_or_404(VoleyPlayer, id=player_id)

    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            playerform = form.cleaned_data
            player.name = playerform['name']
            player.date_joined = playerform['date_joined']
            player.position = playerform['position']
            player.salary = playerform['salary']
            player.contact_person = playerform['contact_person']
            player.save()
            return redirect('index')
    else:
        form = VoleyPlayerForm(instance=player)

    return render(request, 'update_player.html', {'form': form, 'player': player})

def delete_player(request, player_id):
    player = get_object_or_404(VoleyPlayer, id=player_id)

    if request.method=='POST':
        player.delete()
        return redirect('index')

    return render(request, 'delete_player.html', {'player': player})
