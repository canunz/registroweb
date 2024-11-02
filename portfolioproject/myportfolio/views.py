import qrcode
from io import BytesIO
from django.shortcuts import render

def index(request):
    # Aquí puedes agregar cualquier lógica que necesites para la vista 'index'
    return render(request, 'index.html')

def evento(request):
    if request.method == "POST":
        # Capturar los datos del formulario si es necesario
        nombre_evento = request.POST.get("nombre_evento")
        tipo_evento = request.POST.get("tipo_evento")
        
        # URL que se va a codificar en el QR
        data = "https://docs.google.com/forms/d/e/1FAIpQLSd9tvN0cObQOOxErUnM4mEkgM7lZ-rSioOc_u9GERgnS7S3BQ/viewform?usp=sharing"
        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        
        # Codificar la imagen QR en formato base64 para enviar al HTML
        import base64
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

        context = {
            'qr_code_url': img_str  # Pasar la imagen codificada al template
        }

        return render(request, 'evento.html', context)

    return render(request, 'evento.html')

def registro(request, nombre_evento, tipo_evento):
    # Capturar los datos del evento y tipo de evento desde la URL y mostrarlos
    context = {
        'nombre_evento': nombre_evento,
        'tipo_evento': tipo_evento
    }
    return render(request, 'registro.html', context)

# Puedes agregar más vistas si las necesitas más adelante
