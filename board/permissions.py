from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS
import jwt

class AllowAny(BasePermission):
    """
    모든 유저 가능
    """
    def has_permission(self, request, view):
        return True

class IsAuthenticated(BasePermission):
    """
    로그인한 유저만 접근 가능
    """
    def has_permission(self, request, view):
        # print("IsAuthenticated_has_permsiion", request) # PROCESS CHEK
        
        return bool(request.user and request.user.is_authenticated)


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    로그인한 유저만 읽기 가능
    """

    message = "[Access Denied: ERR01] 접근 권한이 없습니다."

    def has_permission(self, request, view):
        # print("IsAuthenticatedOrReadOnly_has_permsiion", request) # PROCESS CHEK

        return bool(
            request.method in SAFE_METHODS or 
            request.user and 
            request.user.is_authenticated
        )

class IsAuthorOrReadOnly(BasePermission):
    """
    인증되지 않은 사용자는 읽기만 가능
    JWT 토큰을 decode, obj의 user와 해당 user가 일치하는지 확인
    """

    message = "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            token = request.header.get('Authorization').split(" ")[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            token_user = payload.get('user_id')

            return obj.user.id == token_user

class IsStaffOrReadOnly(BasePermission):
    """
    스텝만 허용
    """

    message = "[Acess Denied: ERR03] 카테고리 등록, 수정, 삭제 권한이 없습니다."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user_is_staff)

class IsAuthorOrStaffOrReadOnly(BasePermission):
    """
    SAFE_METHODS 만 허용
    작성자와 스텝만 허용
    """

    message = "[Access Denied: ERR03] 작성자와 스텝 외 게시글 수정, 삭제 권한이 없습니다."

    def has_object_permission(self, request, view, obj):
        # print("IsAuthorOrStaff_has_object_permission") # PROCESS CHECK
        if request.method in SAFE_METHODS:
            return True    
        else:        
            return bool((request.user.id == obj.author_id) or request.user.is_staff)
