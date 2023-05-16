import re

pattern = "was"
text = '''
Enoch Fenwick (May 15, 1780 – November 25, 1827) was an American Catholic priest and Jesuit, 
who ministered throughout Maryland and became the president of Georgetown College in Washington, 
D.C. Born in Maryland, he studied at Georgetown College (pictured). Like his brother, future bishop Benedict Joseph 
Fenwick, he entered the priesthood, studying at St. Mary's Seminary before entering the Society of Jesus, 
which was suppressed at the time. He became the rector of St. Peter's Pro-Cathedral in Baltimore for ten years, 
and was briefly also the vicar general of the Archdiocese of Baltimore. In 1820, Fenwick reluctantly accepted his 
appointment as the president of Georgetown College. While he made some improvements to the curriculum, his presidency 
was considered unsuccessful by contemporaries due to declining enrollment and mounting debt. In August 1825, he 
abandoned the presidency following a disagreement with the provincial superior. Two years later, he died 
at Georgetown College. '''

match = re.search(pattern, text)  # search only first occurrence and give the position
print(match)

pattern = r"[A-Z]yclone"
text = '''
Enoch Fenwick (May 15, 1780 – November 25, 1827) was an American Catholic priest and Jesuit, 
who ministered throughout Maryland and became the president of Georgetown College in Washington, 
D.C. Born in Maryland, he studied at Georgetown College (pictured). Like his brother, future bishop Benedict Joseph 
Fenwick, he Cyclone entered the priesthood, studying Dyclone at St. Mary's Seminary before entering the Society of Jesus, 
which was suppressed at the time. He became the rector of St. Peter's Pro-Cathedral in Baltimore for ten years, 
and was briefly also the vicar general of the Archdiocese of Baltimore. In 1820, Fenwick reluctantly accepted his 
appointment as the president of Georgetown College. While he made some improvements to the curriculum, his presidency 
was considered unsuccessful by contemporaries due to declining enrollment and mounting debt. In August 1825, he 
abandoned the presidency following a disagreement with the provincial superior. Two years later, he died cyclone
at Georgetown College. '''

matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
