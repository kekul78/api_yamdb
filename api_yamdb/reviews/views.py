from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from permissions import IsAuthorModeratorAadminOrReadOnly
from .serializers import CommentSerializer, ReviewSerializer
from api.models import Title
from .models import Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAadminOrReadOnly)

    def get_review_obj(self):
        return get_object_or_404(Review, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_review_obj().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=self.get_review_obj()
        )


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAadminOrReadOnly)

    def get_title_obj(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title_obj().reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=self.get_title_obj()
        )
