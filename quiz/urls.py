'''from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user
from django.urls import path


urlpatterns = [         url(regex=r'^$', view=index, name='index'),
                        url(regex=r'^login/$', view=login_user, name='login'),
                        url(regex=r'^logout/$', view=logout_user, name='logout'),
                       url(regex=r'^quizzes/$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),
]'''

from django.urls import path
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('quizzes/', QuizListView.as_view(), name='quiz_index'),
    path('category/', CategoriesListView.as_view(), name='quiz_category_list_all'),
    path('category/<str:category_name>/', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    path('progress/', QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/', QuizMarkingList.as_view(), name='quiz_marking'),
    path('marking/<int:pk>/', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    path('<slug:slug>/', QuizDetailView.as_view(), name='quiz_start_page'),
    path('<str:quiz_name>/take/', QuizTake.as_view(), name='quiz_question'),
]
