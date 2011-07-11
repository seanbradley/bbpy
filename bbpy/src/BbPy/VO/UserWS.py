'''
Created on Dec 1, 2010

@author: cdg2
'''
from BbPy.bbwsdl.User_WS_services import *
from BbPy.bbwsdl.User_WS_services_types import *

class ExtendedInfoVO(object):
    businessFax = None
    businessPhone1 = None
    businessPhone2 = None
    city = None
    company = None
    country = None
    department = None
    emailAddress = None
    expansionData = []
    familyName = None
    givenName = None
    homeFax = None
    homePhone1 = None
    homePhone2 = None
    jobTitle = None
    middleName = None
    mobilePhone = None
    state = None
    street1 = None
    street2 = None
    webPage = None
    zipCode = None
    
    def getUserExtendedInfoVO_Def(self):
        ret = user_ns2.UserExtendedInfoVO_Def(None)
        ret._businessFax = self.businessFax
        ret._businessPhone1 = self.businessPhone1
        ret._businessPhone2 = self.businessPhone2
        ret._city = self.city
        ret._company = self.company
        ret._country = self.country
        ret._department = self.department
        ret._emailAddress = self.emailAddress
        ret._expansionData = self.expansionData
        ret._familyName = self.familyName
        ret._givenName = self.givenName
        ret._homeFax = self.homeFax
        ret._homePhone1 = self.homePhone1
        ret._homePhone2 = self.homePhone2
        ret._jobTitle = self.jobTitle
        ret._middleName = self.middleName
        ret._mobilePhone = self.mobilePhone
        ret._state = self.state
        ret._street1 = self.street1
        ret._street2 = self.street2
        ret._webPage = self.webPage
        ret._zipCode = self.zipCode
        return ret
        

    def __init__(self,ExtendedInfoVO_Holder=None):
        if(ExtendedInfoVO_Holder is not None):
            self.businessFax = ExtendedInfoVO_Holder._businessFax
            self.businessPhone1 = ExtendedInfoVO_Holder._businessPhone1
            self.businessPhone2 = ExtendedInfoVO_Holder._businessPhone2
            self.city = ExtendedInfoVO_Holder._city
            self.company = ExtendedInfoVO_Holder._company
            self.country = ExtendedInfoVO_Holder._country
            self.department = ExtendedInfoVO_Holder._department
            self.emailAddress = ExtendedInfoVO_Holder._emailAddress
            self.expansionData = ExtendedInfoVO_Holder._expansionData
            self.familyName = ExtendedInfoVO_Holder._familyName
            self.givenName = ExtendedInfoVO_Holder._givenName
            self.homeFax = ExtendedInfoVO_Holder._homeFax
            self.homePhone1 = ExtendedInfoVO_Holder._homePhone1
            self.homePhone2 = ExtendedInfoVO_Holder._homePhone2
            self.jobTitle = ExtendedInfoVO_Holder._jobTitle
            self.middleName = ExtendedInfoVO_Holder._middleName
            self.mobilePhone = ExtendedInfoVO_Holder._mobilePhone
            self.state = ExtendedInfoVO_Holder._state
            self.street1 = ExtendedInfoVO_Holder._street1
            self.street2 = ExtendedInfoVO_Holder._street2
            self.webPage = ExtendedInfoVO_Holder._webPage
            self.zipCode = ExtendedInfoVO_Holder._zipCode
            
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class UserVO(object):
    birthDate = None
    dataSourceId = None
    educationLevel = None
    expansionData = []
    extendedInfo = None
    genderType = None
    id = None
    insRoles = []
    isAvailable = None
    name = None
    password = None
    studentId = None
    systemRoles = []
    title = None
    userBatchUid = None
    
    def getUser_Def(self):
        ret = user_ns2.UserVO_Def(None)
        ret._birthDate=self.birthDate
        ret._dataSourceId=self.dataSourceId
        ret._educationLevel=self.educationLevel
        ret._expansionData=self.expansionData
        if self.extendedInfo:
            ret._extendedInfo=self.extendedInfo.getUserExtendedInfoVO_Def()
        ret._genderType=self.genderType
        ret._id=self.id
        ret._insRoles=self.insRoles
        ret._isAvailable=self.isAvailable
        ret._name=self.name
        ret._password=self.password
        ret._studentId=self.studentId
        ret._systemRoles=self.systemRoles
        ret._title=self.title
        ret._userBatchUid=self.userBatchUid
        return ret
        
        
        

    def __init__(self,UserVO_Holder=None):
        if(UserVO_Holder is not None):
            self.birthDate = UserVO_Holder._birthDate
            self.dataSourceId = UserVO_Holder._dataSourceId
            self.educationLevel = UserVO_Holder._educationLevel
            self.expansionData = UserVO_Holder._expansionData
            self.extendedInfo = ExtendedInfoVO(UserVO_Holder._extendedInfo)
            self.genderType = UserVO_Holder._genderType
            self.id = UserVO_Holder._id
            self.insRoles = UserVO_Holder._insRoles
            self.isAvailable = UserVO_Holder._isAvailable
            self.name = UserVO_Holder._name
            self.password = UserVO_Holder._password
            self.studentId = UserVO_Holder._studentId
            self.systemRoles = UserVO_Holder._systemRoles
            self.title = UserVO_Holder._title
            self.userBatchUid = UserVO_Holder._userBatchUid
            
            
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class UserFilterVO(object):
    available = None
    batchId = []
    courseId = []
    expansionData = []
    filterType = None
    groupId = []
    id = []
    name = []
    systemRoles = []
    #GET_ALL_USERS_WITH_AVAILABILITY=1
    GET_USER_BY_ID_WITH_AVAILABILITY=2
    GET_USER_BY_BATCH_ID_WITH_AVAILABILITY=3
    #GET_USER_BY_COURSE_ID_WITH_AVAILABILITY=4
    #GET_USER_BY_GROUP_ID_WITH_AVAILABILITY=5
    GET_USER_BY_NAME_WITH_AVAILABILITY=6
    #GET_USER_BY_SYSTEM_ROLE=7
    
    def __init__(self,UserFilterVO_Holder=None):
        if(UserFilterVO_Holder is not None):
            self.available = UserFilterVO_Holder._available
            self.batchId = UserFilterVO_Holder._batchId
            self.courseId = UserFilterVO_Holder._courseId
            self.expansionData = UserFilterVO_Holder._expansionData
            self.filterType = UserFilterVO_Holder._filterType
            self.groupId = UserFilterVO_Holder._groupId
            self.id = UserFilterVO_Holder._id
            self.name = UserFilterVO_Holder._name
            self.systemRoles = UserFilterVO_Holder._systemRoles
            
    def getUserFilter_Def(self):
        filter = user_ns2.UserFilter_Def(None)
        filter._available = self.available
        filter._batchId = self.batchId
        filter._courseId = self.courseId
        filter._expansionData = self.expansionData
        filter._filterType = self.filterType
        filter._groupId = self.groupId
        filter._id = self.id
        filter._name = self.name
        filter._systemRoles = self.systemRoles
        return filter  
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret