'''
Created on Dec 1, 2010

@author: cdg2
'''
from BbPy.bbwsdl.CourseMembership_WS_services import *
from BbPy.bbwsdl.CourseMembership_WS_services_types import *
class CourseMembershipVO(object):
    available = None
    courseId = None
    dataSourceId = None
    enrollmentDate = None
    expansionData = []
    hasCartridgeAccess = None
    id = None
    imageFile = None
    roleId = None
    userId = None
    
    def __init__(self,CourseMembershipVO_Holder=None):
        if(CourseMembershipVO_Holder is not None):
            self.available = CourseMembershipVO_Holder._available
            self.courseId = CourseMembershipVO_Holder._courseId
            self.dataSourceId = CourseMembershipVO_Holder._dataSourceId
            self.expansionData = CourseMembershipVO_Holder._expansionData
            self.hasCartridgeAccess = CourseMembershipVO_Holder._hasCartridgeAccess
            self.id = CourseMembershipVO_Holder._id
            self.imageFile = CourseMembershipVO_Holder._imageFile
            self.roleId = CourseMembershipVO_Holder._roleId
            self.userId = CourseMembershipVO_Holder._userId
            
            
    def getCourseMembershipVO_Def(self):
        courseMembership = course_membership_ns2.CourseMembershipVO_Def(None)
        courseMembership._available = self.available
        courseMembership._courseId = self.courseId
        courseMembership._dataSourceId = self.dataSourceId
        courseMembership._expansionData = self.expansionData
        courseMembership._hasCartridgeAccess = self.hasCartridgeAccess
        courseMembership._id = self.id
        courseMembership._imageFile = self.imageFile
        courseMembership._roleId = self.roleId
        courseMembership._userId = self.userId
        return courseMembership 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret

class MembershipFilter(object):
    GET_COURSE_MEMBERSHIP_BY_ID=1
    GET_COURSE_MEMBERSHIP_BY_COURSE_ID=2
    GET_COURSE_MEMBERSHIP_BY_USER_ID=5
    GET_COURSE_MEMBERSHIP_BY_COURSE_AND_USER_ID=6
    GET_COURSE_MEMBERSHIP_BY_COURSE_ID_AND_ROLE_ID=7
    
    courseIds = []
    courseMembershipIds = []
    expansionData = []
    filterType = None
    groupIds = []
    groupMembershipIds = []
    roleIds = []
    userIds = []
    
    def __init__(self,MembershipFilter_Holder=None):
        if(MembershipFilter_Holder is not None):
            self.courseIds = MembershipFilter_Holder._courseIds
            self.courseMembershipIds = MembershipFilter_Holder._courseMembershipIds
            self.expansionData = MembershipFilter_Holder._expansionData
            self.filterType = MembershipFilter_Holder._filterType
            self.groupIds = MembershipFilter_Holder._groupIds
            self.groupMembershipIds = MembershipFilter_Holder._groupMembershipIds
            self.roleIds = MembershipFilter_Holder._roleIds
            self.userIds = MembershipFilter_Holder._userIds
            
    def getMembershipFilter_Def(self):
        filter = course_membership_ns2.MembershipFilter_Def(None)
        filter._courseIds = self.courseIds
        filter._courseMembershipIds = self.courseMembershipIds
        filter._expansionData = self.expansionData
        filter._filterType = self.filterType
        filter._groupIds = self.groupIds
        filter._groupMembershipIds = self.groupMembershipIds
        filter._roleIds = self.roleIds
        filter._userIds = self.userIds
        
        return filter 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class CourseMembershipRoleVO(object):
    courseRoleDescription = None
    defaultRole = None
    expansionData = []
    orgRoleDescription = None
    roleIdentifier = None
    
    def __init__(self,CourseMembershipRoleVO_Holder=None):
        if(CourseMembershipRoleVO_Holder is not None):
            self.courseRoleDescription = CourseMembershipRoleVO_Holder._courseRoleDescription
            self.defaultRole = CourseMembershipRoleVO_Holder._defaultRole
            self.expansionData = CourseMembershipRoleVO_Holder._expansionData
            self.orgRoleDescription = CourseMembershipRoleVO_Holder._orgRoleDescription
            self.roleIdentifier = CourseMembershipRoleVO_Holder._roleIdentifier
            
            
    def getCourseMembershipRoleVO_Def(self):
        courseMembershipRole = course_membership_ns2.CourseMembershipRoleVO_Def(None)
        courseMembershipRole._courseRoleDescription = self.courseRoleDescription
        courseMembershipRole._defaultRole = self.defaultRole
        courseMembershipRole._expansionData = self.expansionData
        courseMembershipRole._orgRoleDescription = self.orgRoleDescription
        courseMembershipRole._roleIdentifier = self.roleIdentifier
        return courseMembershipRole 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret