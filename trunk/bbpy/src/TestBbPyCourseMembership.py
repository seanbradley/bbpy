'''
Created on Nov 2, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
import unittest
import logging
import random
import string
import datetime
import time
from BbPy.ContextWS import ContextWS
from BbPy.VO.UserWS import UserFilterVO
from BbPy.VO.UserWS import UserVO
from BbPy.VO.UserWS import ExtendedInfoVO
from BbPy.VO.CourseMembershipWS import CourseMembershipVO

class TestUser(unittest.TestCase):
    
    def setUp(self):
        logging.basicConfig()
        log=logging.getLogger()
        log.setLevel(logging.WARN)
        context = ContextWS("https://dev.bblearn.nau.edu")
        success = context.loginTool("NAU", "PythonFeed", "*****")
        if not success:
            log.error("Login was not successful!")
            self.fail("Login was not successful!")

        self.userws = context.getUserWS()
        self.coursews = context.getCourseWS()
        self.courseMembershipWs = context.getCourseMembershipWS()
        
        self.random = string.lower(''.join(random.choice(string.letters) for i in xrange(5)))
        
        ## Create user to play with
        self.userId = self.userws.createSimpleUser(True, 
                                               self.random, 
                                               "7777777" + self.random, 
                                               "me@stuff.com", 
                                               "familyName" , 
                                               "givenName")
        self.assertTrue(self.userId)
        
        ## Create course to play with
        self.begin = datetime.date.today()
        self.end = datetime.date.today()+datetime.timedelta(days=1)
        self.courseid = self.coursews.createSimpleCourse(True,
                                         "batch"+self.random, # course batch id
                                         "course"+self.random, # course id
                                         "Testing " + self.random + " description", # description
                                         "name"+self.random, # course name
                                         time.mktime(self.begin.timetuple()),
                                         time.mktime(self.end.timetuple()))
        self.assertTrue(self.courseid)
        
        ## Enroll user in class
        membership = CourseMembershipVO()
        membership.available=True
        membership.courseId=self.courseid
        membership.roleId="S"
        membership.userId=self.userId
        
        self.memberships = self.courseMembershipWs.saveCourseMemberships(self.courseid, [membership])
        self.assertTrue(self.memberships)
               
    def tearDown(self):
        pass
        #self.assertTrue(self.coursews.deleteCourse(self.courseid))
        # Delete test user
        #user = self.userws.getUserByBatchId("7777777" + self.random)
        #self.userws.deleteUser(user.id)
        
    def testChangeEnrollment(self):
        course = self.coursews.getCourseById("course"+self.random)
        self.assertTrue(course)
        
        courseMemberships = self.courseMembershipWs.getCourseMembershipsByCourse(course)
        mem = CourseMembershipVO()
        
        for mem in courseMemberships:
            if mem.userId == self.userId[0]:
                self.assertTrue(mem.available)
                self.assertEquals(mem.courseId,self.courseid)
                self.assertEquals(mem.roleId,"S")
                mem.roleId="B"
                
                self.memberships = self.courseMembershipWs.saveCourseMemberships(self.courseid, [mem])
                self.assertTrue(self.memberships)
                
        found = False
        courseMemberships = self.courseMembershipWs.getCourseMembershipsByCourse(course)
        mem = CourseMembershipVO()
        
        for mem in courseMemberships:
            if mem.userId == self.userId[0]:
                found = True
                self.assertTrue(mem.available)
                self.assertEquals(mem.courseId,self.courseid)
                self.assertEquals(mem.roleId,"B")
                mem.roleId="Secondary-Instructor"
                self.memberships = self.courseMembershipWs.saveCourseMemberships(self.courseid, [mem])
                self.assertTrue(self.memberships)
                
        self.assertTrue(found)
        
        found = False
        courseMemberships = self.courseMembershipWs.getCourseMembershipsByCourse(course)
        for mem in courseMemberships:
            if mem.userId == self.userId[0]:
                self.assertTrue(mem.available)
                self.assertEquals(mem.courseId,self.courseid)
                self.assertEquals(mem.roleId,"Secondary-Instructor")
        
        
    
    def testUserEnrolled(self):

        course = self.coursews.getCourseById("course"+self.random)
        self.assertTrue(course)
        
        courseMemberships = self.courseMembershipWs.getCourseMembershipsByCourse(course)
        found = False
        mem = CourseMembershipVO()
        
        for mem in courseMemberships:
            if mem.userId == self.userId[0]:
                found = True
                self.assertTrue(mem.available)
                self.assertEquals(mem.courseId,self.courseid)
                self.assertEquals(mem.roleId,"S")
                
        self.assertTrue(found)
                

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()