from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BookAPIMixins, BooksAPIMixins, BooksAPIGenerics, BookAPIGenerics

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()), # CBV 부터는 as_view
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path('mixin/books/', BooksAPIMixins.as_view()), # mixin도 as_view
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
    path('generic/books/', BooksAPIGenerics.as_view()), # generics도 동일 as_view
    path('generic/book/<int:bid>/', BookAPIGenerics.as_view()),
]

# 뷰셋
from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)
urlpatterns = router.urls