from SMS import SMS
from email import EMail

sms = SMS('66666', '77777')
sms.set_message('no elo')
sms.send()
mail = EMail('aa@aa.aa', 'bb@bb.bb', 'elo')
mail.set_message('no siema')
mail.send()