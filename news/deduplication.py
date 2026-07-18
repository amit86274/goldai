def remove_duplicates(items):
    seen=set();out=[]
    for a in items:
        k=(a.get('title'),a.get('source'))
        if k not in seen:
            seen.add(k);out.append(a)
    return out
