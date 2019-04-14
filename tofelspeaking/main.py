# -*- coding: utf-8 -*-
# @Author: orres
# @Email:  jasonjin22@gmail.com
# @Date:   2019-03-21 10:30:28
# @Last Modified by:   orres
# @Last Modified time: 2019-03-31 17:15:43

import record
import topic
import _thread
import time

date = str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) )
input_filename = "record_" + date + ".wav"
input_filepath = "../records/"
in_path = input_filepath + input_filename

if __name__ == '__main__':
    topic.assignTopic()
try:
    _thread.start_new_thread(record.get_audio, (in_path, ))
    _thread.start_new_thread(topic.timeCount, (45, ) )
except:
    print ("Error: Fail to start the thread")

while 1:
    pass