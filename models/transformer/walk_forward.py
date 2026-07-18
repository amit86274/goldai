
def walk_forward(length,train,test,step):
    i=0
    while i+train+test<=length:
        yield slice(i,i+train),slice(i+train,i+train+test)
        i+=step
