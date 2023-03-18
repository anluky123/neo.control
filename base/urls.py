from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('matches/', views.matches, name="matches"),
    path('create/', views.create, name="create"),
    path('coliseum/', views.coliseum, name="coliseum"),
    path('open/', views.open, name="open"),
    path('matchmaking/', views.matchmaking, name="matchmaking"),
    path('matchmaking2/', views.matchmaking2, name="matchmaking2"),
    path('matchmaking3/', views.matchmaking3, name="matchmaking3"),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('tournaments-info/', views.tournaments_info_active, name='tournaments-info-active'),
    path('tournaments-info-matches/', views.tournaments_info_active2, name='tournaments-info-active2'),
    path('tournaments-info-bracket/', views.tournaments_info_active3, name='tournaments-info-active3'),
    path('tournaments-info-old/', views.tournaments_info, name='tournaments-info'),
    path('goods/', views.goods, name="goods"),
    path('skins/', views.skins, name="skins"),
    path('client/', views.client, name="client"),
    path('promo/', views.promo, name="promo"),
    path('blog/', views.blog, name="blog"),
    path('terms/', views.terms, name="terms"),
    path('policy/', views.policy, name="policy"),
    path('steam/', views.steam, name="steam"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('skins/<str:pk>/', views.profile_skins, name="skins"),
    path('inventory/<str:pk>/', views.profile_inv, name="inv"),
    path('program/<str:pk>/', views.profile_prog, name="prog"),
    path('settings/<str:pk>/', views.profile_settings, name="settings"),
    path('leagues/', views.ligi, name="ligi"),
    path('leagues-info/', views.ligi_info, name="ligi_info"),
    path('rules/', views.rules, name="rules"),
    path('wallet/', views.wallet, name="wallet"),
    path('', include('profiles.urls')),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
