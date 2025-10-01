# Function to join given strings
def combo_string(a, b):

    # your code here
    short=a
    longer=b
    if len(a)<len(b):
        short,longer=a,b
    else:
        short,longer=b,a

    return short + longer + short