import re

with open('face.txt', 'r') as f:
    txt = f.read()
    x = re.findall(r'{{[-\w]+}}', txt)

print("<<<----INSERT INTO SECTION ONE----->>>") 
print("  var timestamp = e.values[0];")  
for i, j in enumerate(x, 1):
    if j == '{{Age}}':
        print(f"  var currentAge = getAge(field_{num});")
    if i != len(x):
        num = str(i).zfill(2)
        print(f"  var field_{num} = e.values[{i}];")
    

print('\n\n')
print("<<<----INSERT INTO SECTION TWO----->>>") 
x.remove('{{Age}}')
print("  body.replaceText('{{Age}}', currentAge);")

for i, j in enumerate(x, 1):
    num = str(i).zfill(2)
    print(f"  body.replaceText('{j}', field_{num});")
