from django.shortcuts import render
from django.http import JsonResponse

def chat_view(request):
    return render(request, 'chatbot/chat.html')

def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Process the message and generate a response
        response_message = process_message(user_message)
        return JsonResponse({'response': response_message})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def process_message(message):
    # Here, you can integrate a chatbot framework or use simple logic
    if message.lower() == 'hello':
        return 'Hello! How can I help you today?'
    else:
        return 'I am not sure how to respond to that.'
