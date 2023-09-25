'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''


def longestCommonPrefix(self, strs):
    max_lengths = []
    all_instances = []
    element_count= {}
    max_elements = []
    max_count = 1
    if len(strs) == 1:
        return strs[0]
    else:
        for i in strs:
            current_element = ''
            for m in i:
                current_element = current_element + m
                all_instances.append(current_element)

        for instance in all_instances:
            if instance in element_count:
                element_count[instance] += 1
            else:
                element_count[instance] = 1
        
        for element in element_count:
            if element_count[element] > max_count:
                max_count = element_count[element]

        if max_count == 1:
            return ''
        else:
            for element in element_count:
                if element_count[element] == max_count:
                    max_elements.append(element)
            for i in max_elements:
                max_lengths.append(len(i))
            max_length = max(max_lengths)
            for i in max_elements:
                if len(i) == max_length:
                    return i
