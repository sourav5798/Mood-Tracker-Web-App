from django.shortcuts import render, redirect
from .models import MoodEntry
from .forms import MoodEntryForm

def get_song_suggestions(mood):
    suggestions = {
        'Happy': [
            {'title': 'Illahi – Pritam, Arijit Singh', 'link': 'https://youtu.be/6w67NOaRe-w?si=NNZ4CoJ5vqposagn'},
            {'title': 'Matargashti – Mohit Chauhan', 'link': 'https://youtu.be/6vKucgAeF_Q?si=TvLDMRxlM3ZYuZRj'},
            {'title': 'Sooraj Dooba Hain – Arijit singh, Aditi Singh Sharma', 'link': 'https://youtu.be/nJZcbidTutE?si=46zPZMX0vfoU4Y9p'},
        ],
        'Sad': [
            {'title': 'Jhol – Maanu, Annural Khalid', 'link': 'https://youtu.be/-2RAq5o5pwc?si=Ci9OSVQme0_JuwEy'},
            {'title': 'Sahiba – Aditya Rikhari, Ankita Chhetri', 'link': 'https://youtu.be/n2dVFdqMYGA?si=DZJDyIyvb7lEKEM5'},
            {'title': 'Afsos – Anuv Jain, AP Dhillon', 'link': 'https://youtu.be/2FhgKp_lfJQ?si=XnqKUHMLNwXhhzMt'},
        ],
        'Angry': [
            {'title': 'Jee Karda – Divya Kumar', 'link': 'https://youtu.be/VAJK04HOLd0?si=muTzkFy0mpcgI0vI'},
            {'title': 'abcdefu – GAYLE', 'link': 'https://youtu.be/NaFd8ucHLuo?si=tzDNuixip8Dy2zi8'},
            {'title': 'Shoorveer – Rapperiya Baalam', 'link': 'https://youtu.be/8h12ccQgnVU?si=SCoZhNWMbtW6OrJQ'},
        ],
        'Relaxed': [
            {'title': 'Namami Shamishan – Religious India', 'link': 'https://youtu.be/081bLdQKX-Q?si=H-UCInD-noWF0xkE'},
            {'title': 'Tum Prem Ho – Mohit Lalwani', 'link': 'https://youtu.be/Feoea8FQTI0?si=Q6N6IHCWIJBxmteE'},
            {'title': 'Namo Namo – Amit Trivedi', 'link': 'https://youtu.be/HFX6AZ5bDDo?si=IvnNOnEIi8katefP'},
        ],
        'Excited': [
            {'title': 'Chalti Hai Kya 9 Se 12 – Anu Malik', 'link': 'https://youtu.be/7vkW5PNBhDU?si=aIaJw0Rz09Qu8x9k'},
            {'title': 'Liggi – Ritviz', 'link': 'https://youtu.be/6BYIKEH0RCQ?si=aoZGSBvGRI1UNXKv'},
            {'title': 'Aasman Ko Chukar Dekha – Daler Mehndi', 'link': 'https://youtu.be/Abk7L9zmbG4?si=IzSwk_NytNJUkHNI'},
        ],
    }
    return suggestions.get(mood, [])

def home(request):
    moods = MoodEntry.objects.order_by('-date')
    return render(request, 'tracker/home.html', {'moods': moods})

def log_mood(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            songs = get_song_suggestions(entry.mood)
            return render(request, 'tracker/suggestions.html', {
                'entry': entry,
                'songs': songs
            })
    else:
        form = MoodEntryForm()
    return render(request, 'tracker/log_mood.html', {'form': form})
