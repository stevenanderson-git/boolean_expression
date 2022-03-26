# Steven Anderson
def string_to_CNF(instring):
    '''
    Given a string with capital letters as variables, replaces the character flags with the unicode symbol for boolean logic.
    o: \u2228 : OR
    n: \u00AC : NOT
    a: \u2227 : AND
    '''
    replacewith = {'o': ' \u2228 ', 'n': ' \u00AC', 'a': ' \u2227 '}
    for k, v in replacewith.items():
        instring = instring.replace(k, v)
    return instring
