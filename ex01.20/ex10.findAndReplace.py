def findAndReplace(original, old_text, new_text):
    replacingText = original
    length_old_text = len(old_text)
    start_idx = 0
    while start_idx + length_old_text <= len(original) :
        if original[start_idx:start_idx + length_old_text] == old_text:
            replacingText = replacingText[:start_idx] + new_text + replacingText[start_idx + length_old_text:]
            start_idx += len(old_text)
        else:
            start_idx += 1
    return replacingText
    
# Book solution
# Move one character of text into replaceText one by one.
# def findAndReplace(text, oldText, newText):
#     replacedText = ''
#     i = 0
#     while i < len(text):
#         # If index i in text is the start of the oldText pattern, add
#         # the replacement text:
#         if text[i:i + len(oldText)] == oldText:
#             # Add the replacement text:
#             replacedText += newText
#             # Increment i by the length of oldText:
#             i += len(oldText)
#         # Otherwise, add the characters at text[i] and increment i by 1:
#         else:
#             replacedText += text[i]
#             i += 1
#     return replacedText


if __name__ == "__main__":
    print("== Start replacing text ==")
    assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
    assert findAndReplace('fox', 'fox', 'dog') == 'dog'
    assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
    assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
    assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
    print("== Finish replacing text ==")