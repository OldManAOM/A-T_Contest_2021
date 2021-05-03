'''
comment_removal.py
'''
import re
text = 'comment_removal.txt'
def read_text(text):
    '''
    open text file, read and return
    :param text:
    :return: code
    '''
    with open(text, 'r') as file:
        code = ""
        for line in file.readlines():
            code += line
    return code

def pattern_commnent(code):
    '''
    find comment by regex
    :param code:
    :return: noncomment code
    '''
    pattern = re.compile('!![^"]+!!|!-+.+\w+.+')
    noncomment = re.sub(pattern, "", code)
    return noncomment




def main():
    code= read_text(text)
    noncomment_list = pattern_commnent(code)
    print(noncomment_list)

if __name__ == '__main__':
    main()
