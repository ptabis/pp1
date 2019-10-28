import re

txt = 'To be, or not to be, that is the question'
samo = re.findall('[eyuioa]', txt)
print("Liczba samogłosek: {}".format(len(samo)))