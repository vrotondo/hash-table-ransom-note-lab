def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Create hash table to count character frequencies in magazine
    char_count = {}
    
    # Count each character in the magazine
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if ransom note can be constructed
    for char in ransomNote:
        # If character not available or count is 0, return False
        if char not in char_count or char_count[char] == 0:
            return False
        # Use one instance of the character (decrement count)
        char_count[char] -= 1
    
    # All characters in ransom note were successfully matched
    return True