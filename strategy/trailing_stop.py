def update_stop(entry,current,distance):
    if current>entry:
        return max(entry,current-distance)
    return min(entry,current+distance)
