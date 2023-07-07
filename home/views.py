from django.shortcuts import render

def transfer_view(request):
    if request.method == 'POST':
        # Обработка данных формы перевода средств
        sender = request.POST['sender']
        recipient = request.POST['recipient']
        amount = request.POST['amount']

        # Ваш код для выполнения перевода средств

        # Отправка данных в шаблон
        context = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            # Дополнительные данные, которые вы хотите передать в шаблон
        }

        return render(request, 'transfer_success.html', context)
    else:
        return render(request, 'index.html')
