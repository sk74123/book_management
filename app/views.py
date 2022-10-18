from rest_framework.response import Response
from app.models import Book, Author,Borrow_book, Reader
from .serializers import Borrow_book_serializer
from rest_framework.views import APIView
import json


class authorAPI(APIView):
    def get(self,request):
        authors= [Author.objects.values()]
        print(type(authors))
        return Response(authors)


class bookAPI(APIView): 
    def get(self,request):
        books = Book.objects.values()
        elements = Book.objects.all()
        collection=[]
        for e in elements:
            collection.append({'id': e.id, 'Name':e.Name, 'Author': e.Author.Name})    
        print(collection)
        return Response(collection)

class borrowAPI(APIView):
    def get(self, request):
        borrowed= Borrow_book.objects.all()
        collection= []
        for b in borrowed: 
            collection.append({'Reader': str(b.Reader), 'Book': str(b.Book.all()), 
            'Issued_on': b.Issued_on, 'Submit_by': b.Submit_by, 'Returned': b.Returned})
        print(collection)
        return Response(collection)


class borrowbookAPI(APIView):
    def post(self,request):
        
        example= {"Reader": "Reader Name", "Book": "Book Name", "Submit_by": '2022-10-19'}
        data = request.body
        #print(data)
        #print(type(data))
        data = json.loads(data)
        #print(data)
        #print(type(data))

        readers = Reader.objects.all()
        books= Book.objects.all()
        reader= data['Reader']
        book= data['Book']
        rdr= None
        bk = None
        def check():
            nonlocal rdr
            nonlocal bk
            for r in readers:
                if r.Name==reader:
                    print('success')
                    #print(rdr)
                    rdr = r
                    break
                else:
                    print('Reader name is wrong')
            for b in books:
                if b.Name==book:
                    print(b)
                    bk= b
                    break
                else:
                    print("Book name is wrong")
        check()
        print(rdr)
        print(bk)
        
        try:
            instance= Borrow_book.objects.get(Reader=rdr)
            instance.Book.add(bk)
            borrowed= Borrow_book.objects.all()
            
            #print(collection)
            return Response('Data Added')
        except:
            return Response('Data is invalid')


        

        
