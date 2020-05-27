from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=50)
    telefone = forms.CharField(label='Assunto', max_length=50)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        #Monta o conteúdo da mensagem do formulário
        conteudo = f'Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}'

        mail = EmailMessage(
            #Corpo do e-mail
            body=conteudo,
            #Quem manda o e-mail
            from_email='contato@fusion.com.br',
            #Lista de quem recebe o e-mail
            to=['contato2@fusion.com',],
            #A quem responde o e-mail
            headers={'Reply-To': email}
        )
        mail.send()#Envia