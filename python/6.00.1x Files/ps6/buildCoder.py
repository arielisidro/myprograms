def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    import string
    dict={}
    letters=string.ascii_lowercase[shift:]+string.ascii_lowercase[0:shift]
    n=0
    for l in string.ascii_lowercase:
        dict[l]=letters[n]
        n+=1
    letters=string.ascii_uppercase[shift:]+string.ascii_uppercase[0:shift]
    n=0
    for l in string.ascii_uppercase:
        dict[l]=letters[n]
        n+=1
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO

    newText=''
    for l in text:
        if l in coder:
            newText+=coder[l]
        else:
            newText+=l
                    
    return newText        

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.

    return applyCoder(text,buildCoder(shift))
    
    