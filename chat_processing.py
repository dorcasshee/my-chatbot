from typing import Optional

def validate(question: Optional[str]) -> list[str]:
    errors = []

    if question is None:
        errors.append('Please provide a question.')
        return errors
    
    if not isinstance(question, str): 
        errors.append('Question must be a string.')
        return errors
    
    clean_question = question.strip()
    
    if clean_question == "":
        errors.append('Please enter a message.')
    
    if len(clean_question) > 500:
        errors.append('Your message is too long. Max character count: 500.')

    return errors