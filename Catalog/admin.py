from django.contrib import admin
from .models import Author, Genre, Translation, Book, BookInstance

# Register your models here.

admin.site.register(Genre)
admin.site.register(Translation)


''' Custom Author-admin list view '''
class BooksInline(admin.TabularInline):
    model = Book

# Define the admin class (override __str__ in Author module)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Define columns that are going to be shown
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'display_books')
    # Define rows (list elements) and cells in a row (dates) when editing
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # Add inlines e.g. additional data to edit below regular Book fields
    inlines = [BooksInline]

    def display_books(self, obj):
        return [b for b in Book.objects.filter(author=obj.id)]
    display_books.short_description = 'Books'


''' Custom Book-admin list view '''
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Data to display in the menu
    list_display = ('title', 'author', 'display_genre')
    # Add inlines e.g. additional data to edit below regular Book fields
    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        return ", ".join([p.name for p in obj.genre.all()])
    
    display_genre.short_description = 'Genre'


''' Custom BookInstance-admin list view '''
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    # Custom list-view
    list_display = ('book', 'status', 'due_back', 'id')
    # Add filter for the listed parameters
    list_filter = ('status', 'due_back')
    # The row below adds 'Availability' separator and no label for the top elements
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

