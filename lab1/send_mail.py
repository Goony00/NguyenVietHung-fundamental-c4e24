from gmail import GMail, Message
from random import randint

sick_list=["thương hàn", "kiết lị", "bố em mất"]
n=randint(0, len(sick_list)-1)

#1. chọn bệnh
sicks=sick_list[n]

html_template='''
<p>Sếp ơi,</p>
<p>H&ocirc;m qua đi kh&aacute;m b&aacute;c sĩ bảo em bị {{sick}} n&ecirc;n h&ocirc;m nay e xin nghỉ nh&eacute;.</p>
<p>Th&acirc;n.</p>
'''

#2. sick+html_template->html_content
html_content=html_template.replace('{{sick}}',sicks)

gmail=GMail('hung ngt<nguyt226@gmail.com>','7355608.')
msg=Message('Đơn xin nghỉ',to='<c4e.techkidsvn@gmail.com>',html=html_content)
gmail.send(msg)