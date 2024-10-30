"""Utilizes the features of dictionaries to create new functions"""
__author__ = "730768561"

def invert(dictionary : dict[str, str]) -> dict[str, str]:
    new_dict : dict[str, str] = {}
    count : int = 0

    for i in dictionary: 
        for j in dictionary: 
            if dictionary[i] == dictionary[j]: # Realized I had to create a counter and if that counter is greater than 1 then it will raise an error
                count += 1 
        if count > 1: 
            raise KeyError("Multiple same keys found")
        else:
            count = 0
        
    for key in dictionary: 
        new_dict[dictionary[key]] = key
    
    return new_dict

def favorite_color(colors : dict[str, str]) -> str:
    max_count : int = 0
    color : str = ""

    for i in colors: 
        count : int = 0
        for j in colors: 
            if colors[i] == colors[j]: 
                count += 1
        if max_count < count: # I also realized I needed to store the color value into a string so that I can return it later.
            max_count = count 
            color = colors[i]

    return color 

def count(values : list[str]) -> dict[str, int]:
    counts : dict[str, int] = {} 

    for value in values: 
        if value in counts: 
            counts[value] += 1
        else:
            counts[value] = 1

    return counts

def alphabetizer(words : list[str]) -> dict[str, list[str]]: 
    new_words : list[str] = [] 

    for item in words: 
        new_words.append(item.lower()) # Needed to create a new list of lowercased words so that the program works optimally

    dictionary : dict[str, list[str]] = {} 

    for i in new_words: 
        first : str = i[0] 
        word_list : list[str] = [] 

        for j in new_words: 
            if first == j[0]: 
                word_list.append(j) # Rather than appending j, I intially appending i which led to many bugs. 

        
        dictionary[first] = word_list # At first, I tried to use the in keyword for this program, but it was just overcomplicating the whole thing and not covering for edge cases.
    
    return dictionary 

def update_attendance(attendance_log : dict[str, list[str]], day : str, student : str) -> None: 
    # Edge Cases need to be covered 

    if day in attendance_log: 
        if student not in attendance_log[day]: 
            attendance_log[day].append(student) 
    else: 
        attendance_log[day] = [student]