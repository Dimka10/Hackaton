from django.core.mail import send_mail


def send_activation_mail(email, activation_code):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}/'
    message = f'''
    Thank you for registration.
    Please activate your account: {activation_url}
    '''

    send_mail(
        'Activate your account',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False
    )