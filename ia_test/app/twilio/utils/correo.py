from sqlalchemy.sql import text
from app import db


def emailCopy(noti):
	correos=''
	queryto = text(f"call db_usuarios.sp_notificar({noti})")
	response = db.session.execute(queryto).all()
	if response:
		number_emails = len(response)
		for i in response:
			if number_emails !=1:
				correos+=i.correo+','
			else:
				correos+=i.correo
			number_emails=number_emails-1
		print(correos)
		return correos
	else:
		return False