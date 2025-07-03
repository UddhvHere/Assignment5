try:
    dict={'Alice':'85','Robin':'90','Harry':'67','Henry':'98'}
    name=input("Enter the student's name:")
    str="{}".format(name)
    print(str,"'s marks:" ,dict[name].format(name))
except:
    print("Student Not Found")
