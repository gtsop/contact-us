
def are_messages_equal(arrayA, arrayB):

    if len(arrayA) != len(arrayB):
        return False
    
    return all([a.is_equal(b) for a, b in zip(arrayA, arrayB)])