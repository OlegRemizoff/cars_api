from rest_framework import filters


class PriceRangeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        if min_price and max_price:
            return queryset.filter(price__range=(min_price, max_price))
        elif min_price:
            return queryset.filter(price__gte=min_price)
        elif max_price:
            return queryset.filter(price__lte=max_price)

        return queryset


class MileageRangeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_mileage = request.query_params.get('min_mileage')
        max_mileage = request.query_params.get('max_mileage')

        if min_mileage and max_mileage:
            return queryset.filter(mileage__range=(min_mileage, max_mileage))
        elif min_mileage:
            return queryset.filter(mileage__gte=min_mileage)
        elif max_mileage:
            return queryset.filter(mileage__lte=max_mileage)

        return queryset