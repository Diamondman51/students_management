# import xml.etree.ElementTree as ET
#
# tree = ET.parse('students.xml')
#
# dataset = tree.getroot()
#
# for data in dataset:
#     print(data.tag)
#     for dat in data:
#         pass
#         # print(dat.attrib)
#
class A:
    f = 10



class C(A):
    def __init__(self, cls):
        super().__init__()
        self.cls = cls


class B:
    p = C(A)
    def __str__(self):
        return f'{self.p.f}'


b = B()

print(type(b))