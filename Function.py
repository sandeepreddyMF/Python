def list_benefits():
    return ["More organized code","More readable code","Easier code reuse", "Allow programmers to share and connect code together"]
benefits=list_benefits()


def sum(a,b):
    return a+b


def build_sentance(info):
    infox=info+' is a benefit of functions!'
    return infox



def name_benefits():
    list_of_benefits=list_benefits()
    for benefits in list_of_benefits:
        print(build_sentance(benefits))


