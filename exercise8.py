import sys
info={}
with open("{}".format(sys.argv[1])) as file:
    for i in file:
        name, info[name]=(i.split(":")[0]), ((i.split(":")[1]).split(","))

    for i in sys.argv[2].split(","):
        try:
            u=info[i][0]
            d=info[i][1]
            print(f"Name: "+{i}+"\tUniversity: "+{u}+"\tDepartment: "+{d})
        except KeyError:
            print(f"No record of "+{i}+"was found")

    
