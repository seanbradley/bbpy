'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
#from bbwsdl.CourseMembership_WS_services import *
#from bbwsdl.CourseMembership_WS_services_types import *
from bbwsdl import CourseMembership_WS_services
import logging
from BbPy.VO.CourseMembershipWS import *
class CourseMembershipWS(object):
    log=logging.getLogger("CourseMembershipWS")
    port=None
    sigHandler=None
    def __init__(self,sigHandler,baseUrl=None):
        self.sigHandler=sigHandler
        
        locator = CourseMembership_WS_services.CourseMembership_WSLocator()
        self.port=locator.getCourseMembership_WSPortType(baseUrl)
        self.port.binding.sig_handler=self.sigHandler
        
        request = CourseMembership_WS_services.getServerVersionRequest()
        response = self.port.getServerVersion(request)
    
        ret = response._return
        self.log.info("Connecting to CourseMembershipWS version: %s" % ret._version)

    def getCourseMembershipsByCourse(self, courseVO):
        filter = MembershipFilter()
        filter.courseIds.append(courseVO.id)
        filter.filterType=MembershipFilter.GET_COURSE_MEMBERSHIP_BY_COURSE_ID
        return self.getCourseMemberships(courseVO.id, filter)

    def getCourseMemberships(self, courseId, membershipFilter):
        request = CourseMembership_WS_services.getCourseMembershipRequest()
        request._courseId = courseId
        request._f=membershipFilter.getMembershipFilter_Def()
        response = self.port.getCourseMembership(request)
        return map(CourseMembershipVO,response._return)
    
    def saveCourseMemberships(self, courseId, courseMembershipVOs):
        request = CourseMembership_WS_services.saveCourseMembershipRequest()
        request._courseId = courseId
        ret = []
        for cm in courseMembershipVOs:
            ret.append(cm.getCourseMembershipVO_Def())
        request._cmArray = ret
        response = self.port.saveCourseMembership(request)
        return response._return
    
    def getCourseRoles(self):
        request = CourseMembership_WS_services.getCourseRolesRequest()
        request._f=None
        response = self.port.getCourseRoles(request)
        return map(CourseMembershipRoleVO,response._return)
        
        
        