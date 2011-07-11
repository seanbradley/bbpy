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
from BbPy.VO.CourseMembershipWS import CourseMembershipRoleVO
import cx_Oracle

class TestUser(unittest.TestCase):
    
    def getParent(self, childBatchUid):
        sql = """
        select * from bblearn.course_main
        where 
          pk1 in (
            select crsmain_pk1 from bblearn.course_course 
              where crsmain_parent_pk1=(
                select pk1 from bblearn.course_main 
                  where batch_uid='%s'
                )
              )
        """%childBatchUid
        ezConStr = cx_Oracle.makedsn("devlmshost1.ucc.nau.edu",1521,"learn")
        connection = cx_Oracle.Connection(
                                          dsn=ezConStr,
                                          user="bblearn",
                                          password="*****")
        cursor=cx_Oracle.Cursor(connection);
        cursor.execute(sql)
        i=0
        for row in cursor.fetchall():
            i=i+1
        cursor.close()
        connection.close()
        return i
    
    def getRowStatus(self, courseBatchUid, userBatchUid):
        sql = """
        select row_status from course_users where 
          crsmain_pk1=(select pk1 from course_main where batch_uid='%s')
          and users_pk1=(select pk1 from users where batch_uid='%s')
        """%(courseBatchUid,userBatchUid)
        ezConStr = cx_Oracle.makedsn("devlmshost1.ucc.nau.edu",1521,"learn")
        connection = cx_Oracle.Connection(
                                          dsn=ezConStr,
                                          user="bblearn",
                                          password="*****")
        cursor=cx_Oracle.Cursor(connection);
        cursor.execute(sql)
        ret=-1
        for row in cursor.fetchall():
            ret=row[0]
        cursor.close()
        connection.close()
        return ret
        
      
    def setUp(self):
        logging.basicConfig()
        log=logging.getLogger()
        log.setLevel(logging.WARN)
        context = ContextWS("https://devlmshost2.ucc.nau.edu")
        success = context.loginTool("NAU", "PythonFeed", "*****")
        if not success:
            log.error("Login was not successful!")
            self.fail("Login was not successful!")
        
        self.nauService = context.getNauService()
        self.userService = context.getUserWS()
        self.courseService = context.getCourseWS()
        self.courseMembership = context.getCourseMembershipWS()
        
        self.random = string.lower(''.join(random.choice(string.letters) for i in xrange(5)))
        self.random2 = string.lower(''.join(random.choice(string.letters) for i in xrange(5)))
        
        ## Create user to play with
        self.userid = self.userService.createSimpleUser(True, 
                                               self.random, 
                                               "7777777" + self.random, 
                                               "me@stuff.com", 
                                               "familyName" , 
                                               "givenName",
                                               "FORMER_STUDENT","STUDENT")
        self.assertTrue(self.userid)
        
        ## Create another user to play with
        self.userid2 = self.userService.createSimpleUser(True, 
                                               self.random2, 
                                               "88888888" + self.random2, 
                                               "me@stuff.com", 
                                               "familyName" , 
                                               "givenName",
                                               "FORMER_STUDENT","STUDENT")
        self.assertTrue(self.userid2)
        
        ## Create course to play with
        self.begin = datetime.date.today()
        self.end = datetime.date.today()+datetime.timedelta(days=1)
        self.courseid = self.courseService.createSimpleCourse(True,
                                         "batch"+self.random, # course batch id
                                         "course"+self.random, # course id
                                         "Testing " + self.random + " description", # description
                                         "name"+self.random, # course name
                                         time.mktime(self.begin.timetuple()),
                                         time.mktime(self.end.timetuple()))
        self.assertTrue(self.courseid)
        
        self.parentCourseid = self.courseService.createSimpleCourse(True,
                                         "PARENTbatch"+self.random, # course batch id
                                         "PARENTcourse"+self.random, # course id
                                         "PARENT Testing " + self.random + " description", # description
                                         "PARENTname"+self.random, # course name
                                         time.mktime(self.begin.timetuple()),
                                         time.mktime(self.end.timetuple()))
        self.assertTrue(self.parentCourseid)
        
        ## Enroll user in class
        membership = CourseMembershipVO()
        membership.available=True
        membership.courseId=self.courseid
        membership.roleId="S"
        membership.userId=self.userid
        
        self.memberships = self.courseMembership.saveCourseMemberships(self.courseid, [membership])
        self.assertTrue(self.memberships)
        
        ## Enroll user in class
        membership = CourseMembershipVO()
        membership.available=True
        membership.courseId=self.courseid
        membership.roleId="S"
        membership.userId=self.userid2
        
        self.memberships = self.courseMembership.saveCourseMemberships(self.courseid, [membership])
        self.assertTrue(self.memberships)
        
    def testGetUserByBatchId(self):
        user = self.userService.getUserByBatchId("7777777" + self.random)
        self.assertEqual(user.name,self.random)
        self.assertEqual(user.studentId,"7777777" + self.random)
        self.assertEqual(user.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user.extendedInfo.familyName,"familyName")
        self.assertEqual(user.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testGetUserById(self):
        user = self.userService.getUserByBatchId("7777777" + self.random)
        user2 = self.userService.getUserById(user.id)
        self.assertEqual(user2.name,self.random)
        self.assertEqual(user.studentId,"7777777" + self.random)
        self.assertEqual(user2.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user2.extendedInfo.familyName,"familyName")
        self.assertEqual(user2.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testGetUserByUsername(self):
        user = self.userService.getUserByUserId(self.random)
        self.assertEqual(user.name,self.random)
        self.assertEqual(user.studentId,"7777777" + self.random)
        self.assertEqual(user.extendedInfo.emailAddress,"me@stuff.com")
        self.assertEqual(user.extendedInfo.familyName,"familyName")
        self.assertEqual(user.extendedInfo.givenName,"givenName")
        self.assertEqual(len(user.insRoles),2)
        
    def testUpdateUser(self):
        ## This is a known bug. Can't update users!
        ## This should fail until AS-146406 is fixed
        ## This is implementing our own nau service to work around this bug
        ## createUpdateUser is our own implementation of this function
        
        self.nauService.createUpdateUser("7777777" + self.random, "NewGivenName", "NewFamilyName", "you@someone.com", self.random)
        
        user = self.userService.getUserByBatchId("7777777" + self.random)
        self.assertEqual(user.name,self.random)
        ## This is a known bug. No student id's back!
        self.assertEqual(user.studentId,"7777777" + self.random)
        self.assertEqual(user.extendedInfo.emailAddress,"you@someone.com")
        self.assertEqual(user.extendedInfo.familyName,"NewFamilyName")
        self.assertEqual(user.extendedInfo.givenName,"NewGivenName")
        
    def testChangeEnrollmentStatus(self):
        ret = self.nauService.changeEnrollmentStatus("batch"+self.random, "7777777" + self.random, True)
        self.assertNotEqual(ret,None)
        self.assertEqual(self.getRowStatus("batch"+self.random, "7777777" + self.random),2)
        ret = self.nauService.changeEnrollmentStatus("batch"+self.random, "7777777" + self.random, False)
        self.assertNotEqual(ret,None)
        self.assertEqual(self.getRowStatus("batch"+self.random, "7777777" + self.random),0)
    
    def testBatchChangeEnrollmentStatus(self):
        ret = self.nauService.batchChangeEnrollmentStatus("batch"+self.random, ["7777777" + self.random,"88888888" + self.random2], True)
        self.assertNotEqual(ret,None)
        self.assertEqual(self.getRowStatus("batch"+self.random, "7777777" + self.random),2)
        self.assertEqual(self.getRowStatus("batch"+self.random, "88888888" + self.random2),2)
        ret = self.nauService.batchChangeEnrollmentStatus("batch"+self.random, ["7777777" + self.random,"88888888" + self.random2], False)
        self.assertNotEqual(ret,None)
        self.assertEqual(self.getRowStatus("batch"+self.random, "7777777" + self.random),0)
        self.assertEqual(self.getRowStatus("batch"+self.random, "88888888" + self.random2),0)
        
    def testRollupCourse(self):
        ret = self.nauService.rollupCourse("PARENTbatch"+self.random, "batch"+self.random, True)
        self.assertNotEqual(ret,None)
        self.assertTrue(self.nauService.isRolledup("PARENTbatch"+self.random, "batch"+self.random))
        self.assertEqual(self.getParent("PARENTbatch"+self.random),1)
        ret = self.nauService.rollupCourse("PARENTbatch"+self.random, "batch"+self.random, False)
        self.assertNotEqual(ret,None)
        self.assertEqual(self.getParent("PARENTbatch"+self.random),0)
        self.assertFalse(self.nauService.isRolledup("PARENTbatch"+self.random, "batch"+self.random))
        
    def testGetIdsFromBatchUids(self):
        ret = self.nauService.getIdsFromBatchUids(["7777777" + self.random,])
        self.assertEqual(ret["7777777" + self.random],self.userid[0])
        
    def tearDown(self):
        # Delete test user
        user = self.userService.getUserByBatchId("7777777" + self.random)
        self.userService.deleteUser(user.id)
        # Delete test user
        user = self.userService.getUserByBatchId("88888888" + self.random2)
        self.userService.deleteUser(user.id)
        # Delete course
        self.courseService.deleteCourse(self.courseid)
        self.courseService.deleteCourse(self.parentCourseid)

if __name__ == "__main__":
    unittest.main()
    
    
    