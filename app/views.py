from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator


def search_book(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort', 'title')

    books = Book.objects.all()
    
    # Filter by status
    if status:
        books = books.filter(status=status)
    else:
        books = books.filter(status__iexact='available')

    # Search query
    if query:
        terms = [term for term in query.split() if term]
        for term in terms:
            books = books.filter(
                Q(title__icontains=term) |
                Q(author__icontains=term) |
                Q(isbn__icontains=term)
            )

    # Filter by category
    if category:
        books = books.filter(category__iexact=category)

    # Sorting
    sort_options = {
        'title': 'title',
        'author': 'author',
        'category': 'category',
        'newest': '-added_date',
        'oldest': 'added_date',
    }
    books = books.order_by(sort_options.get(sort_by, 'title'))

    # Pagination
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = Book.objects.values_list('category', flat=True).distinct()
    status_choices = Book.STATUS_CHOICES

    context = {
        'page_obj': page_obj,
        'books': page_obj,
        'total_books': books.count(),
        'categories': categories,
        'status_choices': status_choices,
        'query': query if query else '',
        'selected_category': category if category else '',
        'selected_status': status if status else '',
        'selected_sort': sort_by,
    }

    return render(request, 'search.html', context)
