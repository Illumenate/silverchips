"""Staff dashboard URL Configuration.

Included directly under /staff. Currently, the index view redirects
manually to the dashboard view.
"""


# Django imports
from django.conf.urls import url

# Local imports
from . import views


# Custom URL patterns
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^dashboard$", views.dashboard, name="dashboard"),
    url(r"^login$", views.login, name="login"),
    url(r"^logout$", views.logout, name="logout"),
    url(r"^story/create$", views.create_story, name="create_story"),
    url(r"^story/edit/([0-9])+$", views.edit_story, name="edit_story"),
    url(r"^upload/image$", views.upload_image, name="upload_image")
]