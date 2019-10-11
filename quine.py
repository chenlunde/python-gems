# source:
s = 's = %r\nprint(s%%s)'
print(s%s)


# after change:
# use follow one can make the same 
r = 'r = %r\nprint(r%%r)'
print(r%r)

