# unconditional variables passing to a function,
# Args - arguments,passes single variable, Kwargs - Keyward argument, passes key and value

import os
os.getcwd()
def ArgsKwargs(*args,**kwargs):
    print(args,kwargs)

best_students =["Robert","Ferdinant","Vasu","Dancan","Makhabwa"]
grade_scores_details = {"Robert":{"Grade":"A","Scores":"98%"},"Ferdinant":{"Grade":"A-","Scores":"90%"},"Vasu":{"Grade":"A","Scores":"95%"},"Duncan":{"Grade":"B+","Scores":"85"},"Makhabwa":{"Grade":"B+","Scores":"78"}}
# Prints out tuple list
print("\nPrints out tuple list of best students\n")
ArgsKwargs(best_students)

# prints out tuple list in agrs positional only
print("\nPrints out in args position only\n")
ArgsKwargs(best_students,grade_scores_details)

# prints out args in args position, and kwargs in kwargs position
print("\nprints out args in args(list) positions and kwargs(dictionary in kwargs position\n")
ArgsKwargs(*best_students,**grade_scores_details)


