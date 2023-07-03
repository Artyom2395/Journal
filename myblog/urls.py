from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, FeedbackView, AboutView, SearchResultsView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedbackView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]