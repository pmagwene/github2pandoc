
# Short tests

This is a test of GitHub to Pandoc inline math: \(x^2 + y^2\)

And now a test of displayed math:

\[
x = \frac{x}{\cos y}
\]

The following should work for delimited code:

'''python
greetings = ['Hello', 'Hola', 'Howdy']
worlds = ['world', 'mundo', 'big green planet']
phrases = ['%s, %s' % (i[0],i[1]) for i in zip(greetings,worlds)]
for phrase in phrases:
    print phrase
'''