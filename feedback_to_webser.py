#! /usr/bin/python3

import os
import requests
import sys

# Function to get the file content and store it in local variable
def get_file_list():

    '''Change the directory to where feedback is located'''
    os.chdir(os.path.dirname(sys.argv[0]))
    os.chdir("feedback")

    '''Get file name list in the directory'''
    file_list = os.listdir()

    return tuple(file_list)

# Function to obtain the feedback information
def get_file_data():
    file_lists = get_file_list()

    raw_feedback = []
    feedback_list = []
    key = ('title','name','date','feedback')

    '''Open the file content and store it in list'''
    for feedback in file_lists:
        with open(feedback,'r') as feed:
            tmp = []
            for line in feed:
                tmp.append(line.strip())
            raw_feedback.append(tmp)
            feed.close()
    
    '''Process the file with its corresponding key in dictionary'''
    for feedback in raw_feedback:
        tmp_dict = {}
        tmp_dict[key[0]], tmp_dict[key[1]], tmp_dict[key[2]], tmp_dict[key[3]] = feedback[0], feedback[1], feedback[2], '\n'.join(feedback[3:])
        feedback_list.append(tmp_dict)

    return tuple(feedback_list)

# Function to post the feedback into web server
def post_to_webserver(url,items):
    
    '''Post the request into web server'''
    response = requests.post(url,data=items)
    return response.status_code

def main():
    feedbacks = get_file_data()
    url = 'https://ipaddress/feedback'
    for feedback in feedbacks:
        print(post_to_webserver(url,feedback))

if __name__ == '__main__':
    main()