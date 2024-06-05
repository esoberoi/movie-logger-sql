from django.shortcuts import render, redirect
from .models import Movie, MovieLog
from .forms import MovieForm, ReportForm, UpdateMovieLogForm
from django.db import transaction

# SATISFIES REQUIREMENT 1   

def search(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        movies = Movie.objects.filter(title__icontains=keyword)
    else:
        movies = []
    all_movies = Movie.objects.all()
    return render(request, 'movieapp/search.html', {'movies': movies, 'all_movies': all_movies})

def add_movie(request): # DYNAMIC addition of movies
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_movie')
    else:
        form = MovieForm()
    return render(request, 'movieapp/add_movie.html', {'form': form})


def view_logs(request):
    logs = MovieLog.objects.order_by('-date_watched')
    return render(request, 'movieapp/view_logs.html', {'logs': logs})

def add_log(request): #dynamic addition of movieLog
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        movie_title = request.POST.get('movie')
        date_watched = request.POST.get('date_watched')
        rating = request.POST.get('rating')
        try:
            movie = Movie.objects.get(title=movie_title)
        except Movie.DoesNotExist:
            error_message = f"Movie with title '{movie_title}' does not exist."
            return render(request, 'movieapp/error.html', {'error_message': error_message})
        log = MovieLog.objects.create(user_id=user_id, movie=movie, date_watched=date_watched, rating=rating)
        return redirect('view_logs')
    else:
        return render(request, 'movieapp/add_log.html')

def delete_movie(request, movie_id): # Dynamic deletion of movies
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        return redirect('search') # REFRESH search page after deletion
    else:
        return redirect('search')

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            #movie = form.cleaned_data['movie_name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            sort_by = form.cleaned_data['sort_by']

            if sort_by == 'release_year_asc':
                movie_logs = MovieLog.objects.filter(user_id=user_id, date_watched__range=[start_date, end_date]).order_by('movie__year')
            elif sort_by == 'release_year_desc':
                movie_logs = MovieLog.objects.filter(user_id=user_id, date_watched__range=[start_date, end_date]).order_by('-movie__year')
            else:
                movie_logs = MovieLog.objects.filter(user_id=user_id, date_watched__range=[start_date, end_date]).order_by(sort_by)
            return render(request, 'movieapp/report_form.html', {'movie_logs': movie_logs})
    else:
        form = ReportForm()
    return render(request, 'movieapp/report_form.html', {'form': form})

@transaction.atomic
def update_movie_log(request):
    if request.method == 'POST':
        form = UpdateMovieLogForm(request.POST)
        if form.is_valid():
            log_id = form.cleaned_data['log_id']
            new_rating = form.cleaned_data['new_rating']
            try:
                movie_log = MovieLog.objects.get(id=log_id)
                movie_log.rating = new_rating
                movie_log.save()
                return redirect('view_logs')
            except MovieLog.DoesNotExist:
                return render(request, 'error.html', {'message': 'MovieLog not found'})
            except Exception as e:
                return render(request, 'error.html', {'message': str(e)})
    else:
        form = UpdateMovieLogForm()
    return render(request, 'movieapp/update_movie_log.html', {'form': form})