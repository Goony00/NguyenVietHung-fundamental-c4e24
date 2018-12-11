import datetime

tiem = datetime.datetime.now()

from gmail import GMail,Message

html_content = '''
<p>Sếp th&acirc;n mến,</p>
<p>S&aacute;ng nay em bị đi ngo&agrave;i n&ecirc;n e xin ph&eacute;p được <span style="text-decoration: underline;"><strong><em>nghỉ&nbsp;</em></strong></span> ạ.</p>
<p>Th&acirc;n,</p>
<p>Em</p>
'''
gmail=GMail('hung ngt<nguyt226@gmail.com>','7355608.')
msg=Message('em chịu',to='<nguyt226@gmail.com>',html=html_content)

if tiem >7: 
    gmail.send(msg)
else:
    pass
