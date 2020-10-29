from django_filters import rest_framework as filters
from .models import Title, Genre, Categories

class TitlesFilter(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug',
    )
    category = filters.CharFilter(
        field_name='category__slug',
    )
    year = filters.CharFilter(
        field_name='year',
    )
    name = filters.CharFilter(
        lookup_expr="contains",
    )
    class Meta:
        model = Title
        fields = ['genre', 'category', 'year', 'name']


class GenresFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name'
    )
    class Meta:
        model = Genre
        fields = ['name']
        

class CategoriesFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name'
    )
    class Meta:
        model = Categories
        fields = ['name']
