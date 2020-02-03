from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from libs.bracket import bracket
from .models import FindClosingBracket
from .serializers import FindClosingBracketSerializer


@api_view(["GET", "POST"])
def find_closing_bracket_list(request):
    """
    List  bracket, or create a new bracket.
    """

    if request.method == "GET":
        data = []
        next_page = 1
        previous_page = 1
        closing_bracket = FindClosingBracket.objects.all()
        page = request.GET.get("page", 1)
        paginator = Paginator(closing_bracket, 15)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = FindClosingBracketSerializer(
            data, context={"request": request}, many=True
        )

        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()

        return Response(
            {
                "data": serializer.data,
                "count": paginator.count,
                "numpages": paginator.num_pages,
                "nextlink": "/api/v1/bracket/?page=" + str(next_page),
                "prevlink": "/api/v1/bracket/?page=" + str(previous_page),
            }
        )

    elif request.method == "POST":
        serializer = FindClosingBracketSerializer(data=request.data)

        if serializer.is_valid():
            # Not sure this is the correct way
            serializer.save(
                closing_position_info=bracket(
                    request.data["string"], request.data["index"]
                )
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def find_closing_bracket_detail(request, pk):
    """
    Retrieve, update or delete a bracket by id/pk.
    """
    try:
        closing_bracket = FindClosingBracket.objects.get(pk=pk)
    except closing_bracket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FindClosingBracketSerializer(
            closing_bracket, context={"request": request}
        )
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FindClosingBracketSerializer(
            closing_bracket, data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save(
                closing_position_info=bracket(
                    request.data["string"], request.data["index"]
                )
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        closing_bracket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
