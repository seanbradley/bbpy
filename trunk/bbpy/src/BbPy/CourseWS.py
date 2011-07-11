'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
import bbwsdl
from bbwsdl.Course_WS_services_types import *
import logging
from BbPy.VO.CourseWS import *
class CourseWS(object):
    log=logging.getLogger("CourseWS")
    port=None
    sigHandler=None
    def __init__(self,sigHandler, baseUrl=None):
        self.sigHandler=sigHandler
        
        locator = Course_WSLocator()
        self.port=locator.getCourse_WSPortType(baseUrl)
        self.port.binding.sig_handler=self.sigHandler
        
        request = bbwsdl.Course_WS_services.getServerVersionRequest()
        response = self.port.getServerVersion(request)
    
        ret = response._return
        self.log.info("Connecting to CourseWS version: %s" % ret._version)
        
    def createSimpleCourse(self,isAvailable,batchUid,courseId,description,name,startDate=None,endDate=None):
        course = CourseVO()
        course.available=isAvailable
        course.batchUid=batchUid
        course.courseId=courseId
        course.description=description
        course.name=name
        if startDate is None or endDate is None:
            course.courseDuration="Continuous"
        else:
            course.startDate=startDate
            course.endDate=endDate
            course.courseDuration="DateRange"
        return self.saveCourse(course)
    
    def getCourseById(self,courseId):
        courseFilterVO = CourseFilterVO()
        courseFilterVO.courseIds=[courseId]
        courseFilterVO.filterType=CourseFilterVO.LOAD_BY_COURSEIDS
        courses = self.getCourse(courseFilterVO)
        if len(courses) == 1: return courses[0] 
        else: return None
        
    def getCourseByBatchId(self,batchId):
        courseFilterVO = CourseFilterVO()
        courseFilterVO.batchUids=[batchId]
        courseFilterVO.filterType=CourseFilterVO.LOAD_BY_BATCHUIDS
        courses = self.getCourse(courseFilterVO)
        if len(courses) == 1: return courses[0] 
        else: return None
        
    def getCourse(self,courseFilterVO):
        request = getCourseRequest()
        request._filter=courseFilterVO.getCourseFilter_Def()
        response = self.port.getCourse(request)
        return map(CourseVO,response._return)
    
    def saveCourse(self,courseVO):
        request = saveCourseRequest()
        request._c=courseVO.getCourse_Def()
        response = self.port.saveCourse(request)
        return response._return
    
    def updateCourse(self,courseVO):
        request = updateCourseRequest()
        request._c=courseVO.getCourse_Def()
        response = self.port.updateCourse(request)
        return response._return
    
    def deleteCourse(self,courseId):
        request = deleteCourseRequest()
        request._ids=[courseId,]
        response = self.port.deleteCourse(request)
        return response._return
    
    def deleteCourses(self,courseIds):
        request = deleteCourseRequest()
        request._ids=courseIds
        response = self.port.deleteCourse(request)
        return response._return
    
    def getCategories(self, categoryFilterVO):
        request = getCategoriesRequest()
        request._filter=categoryFilterVO.getCategoryFilter_Def()
        response = self.port.getCategories(request)
        return map(CategoryVO,response._return)
    
    def getAllCourseCategories(self):
        filter = CategoryFilterVO()
        filter.filterType = CategoryFilterVO.GET_ALL_COURSE_CATEGORY
        return self.getCategories(filter)
    
    def getAllOrgCategories(self):
        filter = CategoryFilterVO()
        filter.filterType = CategoryFilterVO.GET_ALL_ORG_CATEGORY
        return self.getCategories(filter)
    
    def saveCourseCategory(self, categoryVO):
        request = saveCourseCategoryRequest()
        request._adminCategory = categoryVO.getCategory_Def()
        response = self.port.saveCourseCategory(request)
        return response._return
    
    def createSimpleCourseCategory(self, title, batchUid, description, available):
        category = CategoryVO()
        category.available = available
        category.batchUid = batchUid
        category.description = description
        category.title = title
        return self.saveCourseCategory(category)
    
    def deleteCourseCategory(self,categoryId):
        return self.deleteCourseCategories([categoryId])
    
    def deleteCourseCategories(self, categoryIds):
        request = deleteCourseCategoryRequest()
        request._categoryIds = categoryIds
        response = self.port.deleteCourseCategory(request)
        return response._return
    
    def getCoursesCategories(self, courseId):
        filter = CategoryMembershipFilter()
        filter.filterType=CategoryMembershipFilter.GET_CATEGORY_MEMBERSHIP_BY_COURSE_ID
        categoryMembershipTemplate = CategoryMembershipVO()
        categoryMembershipTemplate.courseId = courseId
        filter.templateCategories = [categoryMembershipTemplate]
        return self.getCourseCategoryMemberships(filter)
    
    def getCourseCategoryMemberships(self, filter):
        request = getCourseCategoryMembershipRequest()
        request._filter = filter.getCategoryFilter_Def()
        response = self.port.getCourseCategoryMembership(request)
        return map(CategoryMembershipVO,response._return)
        
    def saveCourseCategoryMembership(self, courseCategoryMembershipVO):
        request = saveCourseCategoryMembershipRequest()
        request._membership = courseCategoryMembershipVO.getCategoryMembershipVO_Def()
        response = self.port.saveCourseCategoryMembership(request)
        return response._return
    
    def setCoursesMembership(self,courseId,categoryId, available):
        membership = CategoryMembershipVO()
        membership.categoryId=categoryId
        membership.courseId=courseId
        membership.available=available
        return self.saveCourseCategoryMembership(membership)
        