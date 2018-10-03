from rest_framework_jwt.settings import api_settings
#
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

def DecodeToken(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    return jwt_decode_handler(token)