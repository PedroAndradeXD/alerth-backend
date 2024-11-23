from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Client, Event, Like
from .serializers import ClientSerializer, ClientLoginSerializer, EventSerializer
from django.contrib.auth.models import User



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    serializer = ClientLoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data
        tokens = get_tokens_for_user(user)
        return Response({
            "message": "Login bem-sucedido!",
            "user": {
                "email": user.email,
                "username": user.username,
            },
            "tokens": tokens,
        })

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email já cadastrado."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=email,
        email=email,
        password=make_password(password)
    )

    client = Client.objects.create(
        name=name,
        email=email
    )

    user.client = client
    user.save()

    tokens = get_tokens_for_user(user)

    return Response({
        "message": "Usuário criado com sucesso!",
        "client": ClientSerializer(client).data,
        "tokens": tokens,
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def test_token(request):
    return Response({"message": f"Acesso liberado para {request.user.email}"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_event(request):
    client = get_object_or_404(Client, email=request.user.email)
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(client=client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_events(request):
    client = get_object_or_404(Client, email=request.user.email)
    events = Event.objects.filter(client=client)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_event(request, event_id):
    client = get_object_or_404(Client, email=request.user.email)
    event = get_object_or_404(Event, pk=event_id)

    # Verifica se o cliente já curtiu o evento
    if event.user_liked(client):
        return JsonResponse({"message": "Você já curtiu este evento!"}, status=400)

    # Adiciona a curtida ao evento
    Like.objects.create(client=client, event=event)
    return JsonResponse({"message": "Evento curtido com sucesso!"}, status=201)