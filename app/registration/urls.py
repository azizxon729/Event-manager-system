from django.urls import path
from .views import RegistrationViewSet

urlpatterns = [
    # 3. Tadbirga ro'yxatdan o'tish: POST /registration/
    path('', RegistrationViewSet.as_view({'post': 'create'}), name='registration-create'),
    
    # 4. Mening tadbirlarim: GET /registration/my-events/
    path('my-events/', RegistrationViewSet.as_view({'get': 'list'}), name='my-events'),
    
    # 5. Ro'yxatdan o'tishni bekor qilish: DELETE /registration/{id}/
    path('<int:pk>/', RegistrationViewSet.as_view({'delete': 'destroy'}), name='registration-delete'),
]