def make_out_word(out, word):
    z = len(out)/2
    return "%s%s%s" %(out[z:], word, out[:z])


print make_out_word('xxcaazz', 'xxbaaz')