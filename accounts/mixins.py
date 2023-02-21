class UserQuerySetMixin():
    
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        user = self.request.user
        
        if user.is_authenticated:
            lookup_data['user'] = user
            if user.is_superuser:
                return super().get_queryset()
            return super().get_queryset().filter(**lookup_data)
        return super().get_queryset().filter(public=True)
