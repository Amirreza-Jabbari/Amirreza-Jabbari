from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
from .forms import ContactForm

def persian_index_view(request):
    form = ContactForm()
    return render(request, 'index-fa.html', {'form': form})

def english_index_view(request):
    form = ContactForm()
    return render(request, 'index-en.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST"])
def contact_view(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Validate data
            if not all([name, email, subject, message]):
                return JsonResponse({
                    'success': False, 
                    'message': 'All fields are required'
                }, status=400)

            # Save message
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            return JsonResponse({
                'success': True, 
                'message': 'Your message has been sent successfully!'
            })
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False, 
        'message': 'Invalid request'
    }, status=400)