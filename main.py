# Write a function to convert numbers to text numerals

NUM_WORD = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'fourty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'}

def text_numeral(num):
    """
    Parameter
    ---------
    num : int
        any integer

    Returns
    -------
    str
        represent num in text form
    """
    if 0<int(num)<100:
        if num not in NUM_WORD.keys():
            num = str(num)
            num1_ = int(num[0]) * 10
            num2_ = int(num[1])
            return    f'{NUM_WORD[num1_]} {NUM_WORD[num2_]}'
        else:
            return f'{NUM_WORD[num]}'

