'''
Created on Nov 2, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
import unittest
import logging
import random
import string
from BbPy.ContextWS import ContextWS
from BbPy.VO.UserWS import UserFilterVO
from BbPy.VO.UserWS import UserVO
from BbPy.VO.UserWS import ExtendedInfoVO
from twisted.internet import reactor
from threading import Thread
import time
import math

class TestUser(unittest.TestCase):
    
    def setUp(self):
        logging.basicConfig()
        log=logging.getLogger()
        log.setLevel(logging.WARN)
        context = ContextWS("https://dev.bblearn.nau.edu")
        success = context.loginTool("NAU", "PythonFeed", "********")
        if not success:
            log.error("Login was not successful!")
            self.fail("Login was not successful!")

        self.userws = context.getUserWS()
        self.userName = ''.join(random.choice(string.letters) for i in xrange(5))
        self.userName = string.lower(self.userName)
        
        ## Create user to play with
        user = self.userws.createSimpleUser(True, 
                                               self.userName, 
                                               "7777777" + self.userName, 
                                               "me@stuff.com", 
                                               "familyName" , 
                                               "givenName",
                                               "FORMER_STUDENT","STUDENT")
        self.assertTrue(user)
        self.beforeAsync=-1
        self.afterAsync=-1
        self.callbackTime=-1
        
    def GetUserByBatchIdAsyncCallback(self,response):
        userVos=map(UserVO,response._return)
        self.assertEqual(len(userVos),1)
        self.callbackTime=time.time()

    def testGetUserByBatchIdAsync(self):
        filter = UserFilterVO()
        filter.batchId=("7777777" + self.userName,)
        filter.filterType=UserFilterVO.GET_USER_BY_BATCH_ID_WITH_AVAILABILITY
        filter.available=True
        self.beforeAsync = math.floor(time.time())
        self.userws.getUserAsync(filter,self.GetUserByBatchIdAsyncCallback)
        self.afterAsync = math.floor(time.time())
        self.assertAlmostEqual(self.beforeAsync,self.afterAsync)
        
    def testGetUserByBatchId(self):
        user = self.userws.getUserByBatchId("7777777" + self.userName)
        self.assertEqual(user.name,self.userName)
        ## This is a known bug. No student id's back!
        #self.assertEqual(user.studentId,"7777777")
        self.assertEqual(user.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user.extendedInfo.familyName,"familyName")
        self.assertEqual(user.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testGetUserById(self):
        user = self.userws.getUserByBatchId("7777777" + self.userName)
        user2 = self.userws.getUserById(user.id)
        self.assertEqual(user2.name,self.userName)
        ## This is a known bug. No student id's back!
        #self.assertEqual(user.studentId,"7777777")
        self.assertEqual(user2.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user2.extendedInfo.familyName,"familyName")
        self.assertEqual(user2.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testGetUserByUsername(self):
        user = self.userws.getUserByUserId(self.userName)
        self.assertEqual(user.name,self.userName)
        ## This is a known bug. No student id's back!
        #self.assertEqual(user.studentId,"7777777")
        self.assertEqual(user.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user.extendedInfo.familyName,"familyName")
        self.assertEqual(user.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testUpdateUser(self):
        ## This is a known bug. Cant update users!
        ## This should fail until AS-146406 is fixed
        user = self.userws.getUserByBatchId("7777777" + self.userName)
        user.extendedInfo.emailAddress="you@someone.com"
        user.extendedInfo.familyName="NewFamilyName"
        user.extendedInfo.givenName="NewGivenName"
        
        self.userws.saveUser(user)
        user = self.userws.getUserByBatchId("7777777" + self.userName)
        self.assertEqual(user.name,self.userName)
        ## This is a known bug. No student id's back!
        #self.assertEqual(user.studentId,"77777770")
        self.assertEqual(user.extendedInfo.emailAddress,"you@someone.com")
        self.assertEqual(user.extendedInfo.familyName,"NewFamilyName")
        self.assertEqual(user.extendedInfo.givenName,"NewGivenName")
        
    def tearDown(self):
        # Delete test user
        user = self.userws.getUserByBatchId("7777777" + self.userName)
        self.userws.deleteUser(user.id)
        while self.beforeAsync <> -1 and self.callbackTime==-1:
            if time.time() - self.beforeAsync > 5:
                self.fail("Callback took to long" + str(time.time() - self.beforeAsync)) 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()