'''
Created on Nov 3, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
import unittest
import logging
from BbPy.ContextWS import ContextWS
from BbPy.VO.CourseWS import CategoryMembershipVO, CategoryVO
import string
import random
import datetime
import time
class Test(unittest.TestCase):


    def setUp(self):
        logging.basicConfig()
        log=logging.getLogger()
        log.setLevel(logging.WARN)
        context = ContextWS("https://dev.bblearn.nau.edu")
        success = context.loginTool("NAU", "PythonFeed", "*****")
        if not success:
            log.error("Login was not successful!")
            self.fail("Login was not successful!")

        self.coursews = context.getCourseWS()
        self.random = string.lower(''.join(random.choice(string.letters) for i in xrange(5)))
        
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
        
        ## Create Category to play with
        self.categoryId = self.coursews.createSimpleCourseCategory(
                                                              "category"+self.random, #name
                                                              "catBatch"+self.random, #id
                                                              "Testing category" + self.random + " description", #Description
                                                              True)
        self.assertTrue(self.categoryId)
        
        ## Create Child Category to play with
        categoryVO=CategoryVO()
        categoryVO.available=True
        categoryVO.batchUid="TestChild"+self.random
        categoryVO.description="TestChild"+self.random
        categoryVO.frontPage=False
        categoryVO.title="TestChild"+self.random
        categoryVO.parentId=self.categoryId
        self.childCategoryId = self.coursews.saveCourseCategory(categoryVO)
        
        self.assertTrue(self.childCategoryId)
        
        ## Assign category to course
        self.courseCategoryMembershipId = self.coursews.setCoursesMembership(self.courseid, self.categoryId, True)
        
        self.assertTrue(self.courseCategoryMembershipId)


    def tearDown(self):
        self.assertTrue(self.coursews.deleteCourse(self.courseid))
        self.assertTrue(self.coursews.deleteCourseCategory(self.childCategoryId))
        self.assertTrue(self.coursews.deleteCourseCategory(self.categoryId))
        
        
    def testCourseChild(self):
        categories = self.coursews.getAllCourseCategories()
        found = True
        
        for category in categories:
            if category.id == self.childCategoryId:
                self.assertEqual(category.parentId,self.categoryId,"Category parent id does not match %s != %s"%(category.parentId,self.categoryId))
                    
        self.assertTrue(found,"Could not find category with id = %s"%self.childCategoryId)
                    

    def testGetCourseByBatch(self):
        course = self.coursews.getCourseByBatchId("batch"+self.random)
        self.assertEqual(course.courseId,"course"+self.random)
        self.assertEqual(course.name,"name"+self.random)
        self.assertEqual(course.batchUid,"batch"+self.random)
        self.assertEqual(course.description,"Testing " + self.random + " description")
        self.assertEqual(datetime.date.fromtimestamp(course.startDate),self.begin)
        self.assertEqual(datetime.date.fromtimestamp(course.endDate),self.end)

    def testGetCourseById(self):
        course = self.coursews.getCourseById("course" + self.random)
        self.assertEqual(course.courseId,"course"+self.random)
        self.assertEqual(course.name,"name"+self.random)
        self.assertEqual(course.batchUid,"batch"+self.random)
        self.assertEqual(course.description,"Testing " + self.random + " description")
        self.assertEqual(datetime.date.fromtimestamp(course.startDate),self.begin)
        self.assertEqual(datetime.date.fromtimestamp(course.endDate),self.end)
        
    def testGetAllCourseCategories(self):
        categories = self.coursews.getAllCourseCategories()
        found = False
        for category in categories:
            if category.title == "category"+self.random:
                found=True
        self.assertEqual(found,True)
        
    def testHasCategory(self):
        courseMemberships = self.coursews.getCoursesCategories(self.courseid)
        courseMembership = CategoryMembershipVO()
        found=False
        for courseMembership in courseMemberships:
            if courseMembership.categoryId == self.categoryId:
                found=True
        self.assertEqual(found,True)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()