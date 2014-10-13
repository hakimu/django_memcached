from django.shortcuts import render
import datetime
from records.models import Album, Artist

def today_is(request):
	now = datetime.datetime.now()
	return render(request, 'listing.html', {'current_time': now})


# def show_album(request):
# 	entries = Album.objects.all()
# 	t = get_template('listing.html')
# 	html = t.render(Context({'entries'}))
# 	return HttpResponse(entries)

def show_album(request):
	entries = Album.objects.all()
	return render(request, 'listing.html', {'album_listing': entries})

def show_artist(request):
	artist_list = Artist.objects.all()
	return render(request, 'listing.html', {'artist_listing': artist_list})