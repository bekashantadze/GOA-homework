# 6) მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
score=int(input("შეიყვანე გამოცდის ქულა:"))
if score >70:
    print("passed:")
else:
    print("failed:")
if score >80:
    grade="A"
elif score >60:
    grade="B"
elif score>40:
    grade="C"
elif score >20:
    grade="D"
else:
    grade="F"
print("შეფასება:" ,grade)
