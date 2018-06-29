#Thanks to Istvan Albert, Pennsylvania State University, USA, https://www.ialbert.me/ , through BioStars
import itertools, string, sys

# strip newlines from the standard input
stream = itertools.imap(string.strip, sys.stdin)

# this works only if sequences span only one line
for head in stream:

    # advance the stream
    seq  = stream.next()
    tmp  = stream.next()
    qual = stream.next()

    # this is how much to pad
    size = 101 - len(seq)

    # pad each line
    seq  = seq  + "N" * size
    qual = qual + "2" * size

    # print the joined elements
    print "\n".join( (head, seq, tmp, qual) )
