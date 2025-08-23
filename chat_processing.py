def validate(question: str | None) -> list[str]:
    errors = []

    if question is None: # question key does not exist in JSON response
        errors.append('Please provide a question.')
        return errors
    
    if not isinstance(question, str): 
        errors.append('Question must be a string.')
        return errors
    
    clean_question = question.strip()
    
    if clean_question == "": # user sends an empty message
        errors.append('Please enter a message.')
    
    if len(clean_question) > 500: # check character count
        errors.append('Your message is too long. Max character count: 500.')

    return errors