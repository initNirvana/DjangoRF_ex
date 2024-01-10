from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.generics import get_object_or_404 # object_4040
from .models import Book # 모델
from .serializers import BookSerializer # 시리얼라이저

from rest_framework import generics
from rest_framework import mixins

from rest_framework import viewsets

#함수형 뷰
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world")

# 함수형 뷰 FBV   
@api_view(["GET", "POST"])
def booksAPI(request):
    if request.method == "GET":
        books       = Book.objects.all() # 모델로부터 전체 데이터 가져오기
        serializer  = BookSerializer(books, many=True) # 직렬화 many=True
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer  = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def bookAPI(request, bid): # /book/bid/
    book        = get_object_or_404(Book, bid=bid)
    serializer  = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


# # 클래스 뷰
# class HelloAPI(APIView):
#     def get(self,request):
#         return Response("hello world")

# 클래스 뷰
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer  = BookSerializer(books, many=True) # 직렬화 many=True
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer  = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class BookAPI(APIView):
    def get(self, request, bid):
        book        = get_object_or_404(Book, bid=id)
        serializer  = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 믹스인 (generics, mixixs import 하자)
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # 리스트 전체 조회
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # 생성
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer
    lookup_field        = 'bid'
    # Django 기본 모델의 pk를 사용하는 것이 아닌 bid를 사용하고 있으므로 lookup_field 사용
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) # 리스트 전체 조회
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # 생성
    
    def delete(self, request, *args, **kwargs): # 삭제
        return self.destroy(request, *args, **kwargs)
    
# 제네릭스
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer
    lookup_field        = 'bid'
    
# 뷰셋 viewsets
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer