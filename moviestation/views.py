from asyncio.windows_events import NULL
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.db.models import Q
import json

from .models import Movie
from .models import User


def index(request):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        latest_movies_list = Movie.objects.values()
        return render(request, 'movies/index.html', {'latest_movies_list':latest_movies_list,'first_name':request.session['first_name'],'last_name':request.session['last_name']})
    except Exception as e:
        print(e)
        return redirect('/login')

def movie_genre(request,genre):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        latest_movies_list = Movie.objects.filter(genre__icontains=genre)
        return render(request, 'movies/genre.html', {'latest_movies_list':latest_movies_list,'genre':genre,'first_name':request.session['first_name'],'last_name':request.session['last_name']})
    except Exception as e:
        print(e)
        return redirect('/login')
    
def search(request):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        if request.GET['keyword']:
            keyword = request.GET['keyword']
            criterion1 = Q(genre__contains=keyword)
            criterion2 = Q(synopsis__contains=keyword)
            criterion3 = Q(title__contains=keyword)
            criterion4 = Q(main_actors__contains=keyword)
            latest_movies_list = Movie.objects.filter(criterion1 | criterion2 | criterion3 | criterion4).values()
            return render(request, 'movies/search.html', {'latest_movies_list':latest_movies_list,'keyword':keyword,'first_name':request.session['first_name'],'last_name':request.session['last_name']})
        else:
            latest_movies_list = Movie.objects.values()
            return render(request, 'movies/index.html', {'latest_movies_list':latest_movies_list,'first_name':request.session['first_name'],'last_name':request.session['last_name']})
    except Exception as e:
        print(e)
        return redirect('/login')

def movie_detail(request, movie_id):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/movie.html', {'movie': movie,'first_name':request.session['first_name'],'last_name':request.session['last_name']})
    except:
        return redirect('/login')

def addmovie(request):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        if request.method == 'POST':
            title = request.POST['title']
            release_date = request.POST['release_date']
            main_actors = request.POST['main_actors']
            genre = request.POST['genre']
            synopsis = request.POST['synopsis']
            poster = request.FILES['poster']
            trailer = request.POST['trailer']
            created_by = request.session['user_id']
            if Movie.objects.filter(title=title,release_date=release_date).exists():
                messages.info(request, "Movie Already Exist")
                return redirect('')
            try:
                movie = Movie.objects.create(title=title,release_date=release_date,main_actors=main_actors,genre=genre,synopsis=synopsis,poster=poster,trailer=trailer,created_by=created_by)
                movie.save()
                return redirect('/')
            except:
                messages.info(request, "Can't add movie right now")
                return redirect('/addmovie')
        else:
            return render(request, 'movies/addmovie.html', {'first_name':request.session['first_name'],'last_name':request.session['last_name']})
    except:
        return redirect('/login')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender=request.POST.get("gender", "default user")
        date_of_birth = request.POST['date_of_birth']
        profile_image = request.FILES['profile_image']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username taken. choose other")
            return redirect('/signup')
        try:
            user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,gender=gender,date_of_birth=date_of_birth,profile_image=profile_image)
            user.save()
            request.session['is_loggedin'] = True
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/')
        except:
            messages.info(request, "Can't signup right now")
            return redirect('/signup')
    else:
        return render(request, 'movies/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username,password=password)
            request.session['is_loggedin'] = True
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/')
        except:
            messages.info(request, "Invalid Credentials")
            return redirect('/login')
    else:
        return render(request, 'movies/login.html')

def logout(request):
    try:
        if request.session['is_loggedin'] != True:
            return redirect('/login')
        del request.session['is_loggedin']
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
        return redirect('/login')
    except:
        return redirect('/login')
