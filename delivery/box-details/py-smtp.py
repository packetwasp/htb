import smtpd
import pymysql
import re
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))

        data = data.decode()
        search = re.compile("do_verify_email((.|\n)*) \)", re.MULTILINE)
        token = re.findall(search, data)[0][0]
        token = token.replace('=\n','')
        token = token.replace('=3D','=')
        token = token.replace('3D=','')
        data = f"""
        ----
        Registration Successful
        ----

        Please activate your email by going to: http://delivery.htb:8065/do_verify_email{token}
        """
        rcpttos = rcpttos[0]

        if re.search(r'^[0-9]*@delivery.htb$', rcpttos):
            ticket = rcpttos.split('@')[0]
            db = pymysql.connect("localhost","ost_user","!H3lpD3sk123!", "osticket" )
            cursor = db.cursor()
            cursor.execute(f"SELECT ticket_id from ost_ticket where number = '{ticket}'")
            result = cursor.fetchone()[0]
            if result:
                cursor.execute(f"UPDATE ost_thread_entry SET body = '{data}' WHERE thread_id = '{result}'")
                db.commit()
            db.close()
        
        
        return

server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
