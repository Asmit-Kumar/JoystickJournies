from . import views as v
from django.urls import path

urlpatterns = [
    path('newpost/', v.NewBlogForm, name= 'New Blog'),
    path('genre/shooter/', v.ShooterView, name='Shooter'),
    path('blogs/<str:slug>/', v.DynamicBlogView, name='Blog'),
    path('genre/strategy/', v.strategy_view, name='Strategy'),
    path('genre/choices_matter/', v.choice_matters_view, name='Choice Matters'),
    path('genre/adventure/', v.adventure_view, name='Adventure'),
    path('blogs/', v.BlogsView, name='Blogs'),
    path('blogs/<int:post_id>/update/', v.UpdateBlogView, name='update blog'),
    path('blogs/<str:slug>/delete/', v.BlogDeleteView, name='Blog'),
]
