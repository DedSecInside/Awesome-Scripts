# coding: utf-8
# Marta Laís, 2018. https://github.com/martalais/


# Automatic sending of e-mails with attachments via the terminal.
# After the implementation, just create a routine in the crontab for its execution.

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate
import smtplib


def enviaEmail(servidor, porta, FROM, PASS, TO, subject, texto, anexo=[]):
    """
    Sends an email.

    Args:
        servidor: (str): write your description
        porta: (int): write your description
        FROM: (str): write your description
        PASS: (todo): write your description
        TO: (str): write your description
        subject: (str): write your description
        texto: (str): write your description
        anexo: (todo): write your description
    """
	global saida
	servidor = servidor
	porta = porta
	FROM = FROM
	PASS = PASS
	TO = TO
	subject = subject
	texto = texto
	msg = MIMEMultipart()
	msg['From'] = FROM
	msg['To'] = TO
	msg['Subject'] = subject
	msg.attach(MIMEText(texto))

	  for i in anexo:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(i, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment;filename="%s"'% os.path.basename(i))
		msg.attach(part)

	  try:
		gm = smtplib.SMTP(servidor,porta)
		gm.ehlo()
		gm.starttls()
		gm.ehlo()
		gm.login(FROM, PASS)
		gm.sendmail(FROM, TO, msg.as_string())
		gm.close()

	  except Exception,e:
		mensagemErro = "Erro ao enviar o e-mail." % str(e)
		print '%s' % mensagemErro

# E-mail  addressee.
 addressee = ''

# Subject of the email.
subject = ''

# E-mail message.
message = ''

# Smtp server address that will be used.
# An example is: smtp.gmail.com
server = ''

# SMTP server port.
# An example is: 587 (gmail)
port =

# E-mail address and sender password.
sender = ''
password = ''

# E-mail sending function call.
# Note that in [""] the exact path of the attachment must be referenced.
sendmail (server, port, sender, password,  addressee, subject, message, [""])