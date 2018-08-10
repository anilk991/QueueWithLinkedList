# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:52:03 2018

@author: Anil Kumar Koundal

Implementaion of Queue with Linked List
Originally written by Narasimha Karumanchi
Modified the code @ https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter05queues/QueuesWithLinkedLists.py
on Aug 10, 2018.

"""

class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.last=None
        self.next=next
        
    def setData(self,data):
        self.data=data
    
    def getData(self):
        return self.data
    
    def setNext(self,next):
        self.next=next
        
    def getNext(self):
        return self.next
    
    def setLast(self,last):
        self.last=last
        
    def getLast(self):
        return self.last
    
    def hasNext(self):
        return self.next != None
    
class Queue(object):
    def __init__(self,data=None):
        self.front=None
        self.rear=None
        self.size=0
        
    def enQueue(self,data):
        self.lastNode=self.rear
        self.rear=Node(data,self.rear)
        if self.lastNode:
            self.lastNode.setLast(self.rear)
        if self.front is None:
            self.front = self.rear
        self.size += 1
        
    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.front.getData()
    
    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.rear.getData()
    
    def deQueue(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        result=self.front.getData()
        self.front=self.front.last
        self.size -= 1
        return result
    
    def getSize(self):
        return self.size
    
que=Queue()
que.enQueue("First")
print("Front: ",que.queueFront())
print("Last: ",que.queueRear())
print("Size: ",que.getSize())
que.enQueue("Second")
print("Front: ",que.queueFront())
print("Last: ",que.queueRear())
print("Size: ",que.getSize())
que.enQueue("Third")
print("Front: ",que.queueFront())
print("Last: ",que.queueRear())
print("Size: ",que.getSize())
que.enQueue("Fourth")
print("Front: ",que.queueFront())
print("Last: ",que.queueRear())
print("Size: ",que.getSize())
que.deQueue()
print("Front: ",que.queueFront())
print("Last: ",que.queueRear())
print("Size: ",que.getSize())