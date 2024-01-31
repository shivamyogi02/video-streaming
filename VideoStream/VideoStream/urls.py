"""VideoStream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryView
from . import ShowView
from . import EpisodeView
from . import AdminView
from . import UserView
urlpatterns = [
    path('admin/', admin.site.urls),
    # UserInterface
    path('userview/', UserView.UserView),
    path('preview/', UserView.Preview),
    path('tvpreview/', UserView.TvPreview),
    path('userdetailssubmit/', UserView.UserDetailsSubmit),
    path('checkmobilenumber/', UserView.CheckMobileNumber),
    path('usersession/', UserView.UserSession),
    path('userlogout/', UserView.UserLogout),
    path('searching/', UserView.Searching),
    # Admin
    path('adminlogin/', AdminView.AdminLogin),
    path('chklogin', AdminView.CheckLogin),
    #Category
    path('categoryinterface/',CategoryView.CategoryInterface),
    path('submitcategory', CategoryView.SubmitCategory),
    path('displayallcategory/',CategoryView.DisplayAll),
    path('categorybyid/',CategoryView.CategoryById),
    path('editdeletecategorydata/',CategoryView.EditDeleteCategoryData),
    path('editicon', CategoryView.EditIcon),
    path('displayallcategoryjson/', CategoryView.DisplayAllJSON),
    # shows
    path('showinterface/', ShowView.ShowInterface),
    path('submitshow', ShowView.SubmitShow),
    path('displayallshow/', ShowView.DisplayAllShow),
    path('showbyid/', ShowView.ShowById),
    path('editdeleteshowdata/', ShowView.EditDeleteShowData),
    path('editposter', ShowView.EditPoster),
    path('edittrailer', ShowView.EditTrailer),
    path('editvideo', ShowView.EditVideo),
    path('displayallshowjson/', ShowView.DisplayAllShowJSON),

    #episode
    path('episodeinterface/',EpisodeView.EpisodeInterface),
    path('submitepisode',EpisodeView.SubmitEpisode),
    path('displayallepisode/',EpisodeView.DisplayAllEpisodes),
    path('episodebyid/',EpisodeView.EpisodeById),
    path('editdeleteepisodedata/',EpisodeView.EditDeleteEpisodeData),
    path('editepisodeposter',EpisodeView.EditEpisodePoster),
    path('editepisodetrailer',EpisodeView.EditEpisodeTrailer),
    path('editepisodevideo',EpisodeView.EditEpisodeVideo),

]
