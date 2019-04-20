intents = {"intro": "hello(query)",
           "programmes":"programme(query)",
           "application":"form(query)",
           "down":"dl(query)",
           "procedure":"proc(query)",
           "host":"hos(query)",
           "fee":"fees(query)",
           "nri":"nri(query)",
           "con":"con(query)",
           "stop": "stop(query)"}
intent_mapper = {
    "hi": "intro",
    "hey": "intro",
    "hello": "intro",
    "howdy": "intro",
    "btech":"programmes",
    "full-time":"programmes",
    "mtech":"programmes",
    "courses":"programmes",
    "apply":"application",
    "forms":"application",
    "download":"down",
    "selection":"procedure",
    "counselling":"procedure",
    "procedure":"procedure",
    "merit":"procedure",
    "hostel":"host",
    "facility":"host",
    "fee":"fee",
    "pay":"fee",
    "nri": "nri",
    "contact":"con",
    "person":"con",
    "quit": "stop",
    "bye": "stop",
    "end": "stop",
    "exit": "stop",
    

}

stopwords = ["a", "and", "the", "this", "list", "get", "display"]
# print(stopwords)
