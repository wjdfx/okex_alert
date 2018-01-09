import urllib
import urllib.request
import time
import ssl
import smtplib
from email.mime.text import MIMEText
from email.header import Header

ssl._create_default_https_context = ssl._create_unverified_context

s_smtp_server =  
s_smtp_user = 
s_smtp_pwd = 
r_email = 


while True:


    api_usl = 'https://www.okex.com/api/v1/future_kline.do?symbol=btc_usd&type=5min&contract_type=this_week&size=3'

    req = urllib.request.urlopen(api_usl).read()
    req_str = req.decode(encoding="utf-8")
    req_del_right = req_str.replace(']', '')
    req_del_left = req_del_right.replace('[', '')

    print(req_del_left)
    list2 = req_del_left.split(",")

    print(list2[6])
    print(list2[13])
    print(list2[20])

    o1 = float(list2[6])
    o2 = float(list2[13])
    o3 = float(list2[20])

    if o3/o1 > 6 or o3/o2 > 6 or o2/o1 > 6:
        print('达到条件了')


        def SendEmail(fromAdd, toAdd, subject, attachfile, htmlText):
            strFrom = fromAdd;
            strTo = toAdd;
            msg = MIMEText(htmlText);
            msg['Content-Type'] = 'Text/HTML';
            msg['Subject'] = Header(u'BTC already up to alert', 'utf-8').encode()
            msg['To'] = strTo;
            msg['From'] = strFrom;

            smtp = smtplib.SMTP(s_email_smtp);
            smtp.login(s_smtp_server, s_smtp_user);
            try:
                smtp.sendmail(strFrom, strTo, msg.as_string());
            finally:
                smtp.close;


        if __name__ == "__main__":
            SendEmail(s_smtp_user, r_email, "ETH already up to alert", "hello", "hello world");

        print('已经发邮件了')

        time.sleep(300)

    else:
        print('没有达到条件，继续监控')

    time.sleep(30)

