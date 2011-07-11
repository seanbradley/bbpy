'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
from BbPy.ContextWS import ContextWS
from BbPy.VO.CourseMembershipWS import CourseMembershipVO, CourseMembershipRoleVO
import logging
import sys

if __name__ == '__main__':
    logging.basicConfig()
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    context = ContextWS("https://dev.bblearn.nau.edu")
    if True:
        toolMethods = [
                "User.WS:getServerVersion", 
                "User.WS:initializeUserWS", 
                "User.WS:saveUser", 
                "User.WS:getUser",
                "User.WS:deleteUser", 
                "User.WS:saveObserverAssociation",
                "User.WS:getObservee",
                "User.WS:deleteAddressBookEntry",
                "User.WS:getAddressBookEntry",
                "User.WS:saveAddressBookEntry",
                "User.WS:getSystemRoles",
                "Course.WS:getCourse",
                "Course.WS:saveCourse",
                "Course.WS:deleteCourse",
                "Course.WS:getCategories",
                "Course.WS:getCourseCategoryMembership",
                "Course.WS:saveCourseCategory",
                "Course.WS:saveCourseCategoryMembership",
                "Course.WS:deleteCourseCategory",
                "Course.WS:deleteCourseCategoryMembership",
                "Course.WS:initializeCourseWS",
                "CourseMembership.WS:getCourseMembership",
                "CourseMembership.WS:saveCourseMembership",
                "CourseMembership.WS:initializeCourseMembershipWS",
                "user.authinfo"]
        success = context.registerTool("NAU", 
                                       "PythonFeed", 
                                       "*****", 
                                       "PythonFeed", 
                                       toolMethods, 
                                       None)
    else:
        success = context.loginTool("NAU", "PythonFeed", "lemtein")
        if not success:
            log.error("Login was not successful!")
            sys.exit()
            
        #userws = context.getUserWS()
        courseWs = context.getCourseWS()
        userWs = context.getUserWS()
        courseMembershipWs = context.getCourseMembershipWS()
        
        
        
        course = courseWs.getCourseByBatchId("1107-NAU00-NUR-424-SEC801-11685.NAU-PSSIS")
        memberships = courseMembershipWs.getCourseMembershipsByCourse(course)
        user = userWs.getUserByUserId("cdg2")
        membership = CourseMembershipVO()
        for membership in memberships:
            if membership.userId == user.id:
                membership.available=True
                membership.userId=user.id
                membership.roleId="B"
                
                courseMembershipWs.saveCourseMemberships(course.id, memberships)
        
        
        
    
    
    
    
    