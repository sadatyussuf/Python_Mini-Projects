def distance(strand_a, strand_b):
    count =0
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands not the same length!")   
    for item_a,item_b in zip(strand_a,strand_b):
        if item_a != item_b:
            count += 1
    return count
        
