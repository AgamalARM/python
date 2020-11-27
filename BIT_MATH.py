def SET_BIT (VAR,BIT) :
    var = int(VAR)
    bit = int(BIT)
    result = var | (1 << bit)
    return result
    
def CLR_BIT (VAR,BIT) :
    var = int(VAR)
    bit = int(BIT)
    result = var & (~(1 << bit))
    return result
    
def GET_BIT (VAR,BIT) :
    var = int(VAR)
    bit = int(BIT)
    result = (var >> bit) & 1
    return result
    
def TOG_BIT (VAR,BIT) :
    var = int(VAR)
    bit = int(BIT)
    result = var ^ (1 << bit)
    return result