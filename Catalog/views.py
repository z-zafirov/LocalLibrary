from django.shortcuts import render
from Catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    template_name = 'index.html'
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, template_name, context=context)


class BookListView(generic.ListView):
    model = Book
    # ??? template_name = 'Catalog/book_list.html' # Specify your own template name/location
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    # Overriding methods in class-based views
    def get_queryset(self):
        return Book.objects.filter(title__icontains='Thomas')[:5] # Get 5 books containing the title war
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['test_data'] = 'This is just some data'
        return context
    

# That one is not working - template is being rendered, but there is no data shown!
class BookDetailView(generic.ListView):
    model = Book
    template_name = 'Catalog/book_detail.html'


def BookDetailNewView(request, pk):
    template_name = 'Catalog/book_detail_new.html'
    data = Book.objects.filter(id=pk).values()[0]
    title = data['title']
    summary = data['summary']
    author_id = data['author_id']
    author = Author.objects.filter(id=author_id).values()[0]
    author_name = author['first_name']
    author_family = author['last_name']
    author_birth = author['date_of_birth']
    author_death = author['date_of_death']
    
    context = {
        'title': title,
        'summary': summary,
        'author_name': author_name,
        'author_family': author_family,
        'author_birth': author_birth,
        'author_death': author_death,
    }

    return render(request, template_name, context=context)