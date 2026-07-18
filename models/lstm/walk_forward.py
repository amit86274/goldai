
def walk_forward_indices(length,train_size,test_size,step):
    start=0
    while start+train_size+test_size<=length:
        yield (slice(start,start+train_size),
               slice(start+train_size,start+train_size+test_size))
        start+=step
