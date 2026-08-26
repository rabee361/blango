from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    # leave other attributes as is