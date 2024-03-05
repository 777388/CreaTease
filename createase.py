

### CREATES (crea-tease) ###
try:
    class creator:
        def __init__(self):
            regards = {Fundamentals: ["society", "independence", "intuition", "correspondance", "decadence", "physics"], 
                       Insight: ["manipulation", "altruism", "revolution", "domestication"], 
                       Tensions: ["Equality", "remainders", "loose ends", "bad calls"],
                       Inspirations: ["Martyrdom", "Naturalism", "Fault", "Entropy", "Chaos"]}
            return regards
        def __init_subclass__(self):
            intellect = {Workplace: ["Design", "Schooling", "Interoperability Triggers", "Mechanisms", "Reputation", "Possibilities", "Opportunities"],
                        In: ["Interruptions", "Intelligence", "Insight", "Inspirations"],
                        Out: ["Outsiders", "outlines", "callout"]}
            (lambda: intellect.append(__name__.__add__))()
    class found(creator):
        def __init__(self):
            super(found, self).__init__()
except:
    print("You could be creating right now")
