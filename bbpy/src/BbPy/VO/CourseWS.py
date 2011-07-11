'''
Created on Dec 1, 2010

@author: cdg2
'''
from BbPy.bbwsdl.Course_WS_services import *
from BbPy.bbwsdl.Course_WS_services_types import *

class CourseVO(object):
    allowGuests = None
    allowObservers = None
    available = None
    batchUid = None
    buttonStyleBbId = None
    buttonStyleShape = None
    buttonStyleType = None
    cartridgeId = None
    classificationId = None
    courseDuration = None
    courseId = None
    coursePace = None
    courseServiceLevel = None
    dataSourceId = None
    decAbsoluteLimit = None
    description = None
    endDate = None
    enrollmentAccessCode = None
    enrollmentEndDate = None
    enrollmentStartDate = None
    enrollmentType = None
    expansionData = []
    fee = None
    hasDescriptionPage = None
    id = None
    institutionName = None
    locale = None
    localeEnforced = None
    lockedOut = None
    name = None
    navCollapsable = None
    navColorBg = None
    navColorFg = None
    navigationStyle = None
    numberOfDaysOfUse = None
    organization = None
    showInCatalog = None
    softLimit = None
    startDate = None
    uploadLimit = None
    
    
    def getCourse_Def(self):
        ret = course_ns1.CourseVO_Def(None)
        ret._allowGuests=self.allowGuests
        ret._allowObservers=self.allowObservers
        ret._available=self.available
        ret._batchUid=self.batchUid
        ret._buttonStyleBbId=self.buttonStyleBbId
        ret._buttonStyleShape=self.buttonStyleShape
        ret._buttonStyleType=self.buttonStyleType
        ret._cartridgeId=self.cartridgeId
        ret._classificationId=self.classificationId
        ret._courseDuration=self.courseDuration
        ret._courseId=self.courseId
        ret._coursePace=self.coursePace
        ret._courseServiceLevel=self.courseServiceLevel
        ret._dataSourceId=self.dataSourceId
        ret._decAbsoluteLimit=self.decAbsoluteLimit
        ret._description=self.description
        ret._endDate=self.endDate
        ret._enrollmentAccessCode=self.enrollmentAccessCode
        ret._enrollmentEndDate=self.enrollmentEndDate
        ret._enrollmentStartDate=self.enrollmentStartDate
        ret._enrollmentType=self.enrollmentType
        ret._expansionData=self.expansionData
        ret._fee=self.fee
        ret._hasDescriptionPage=self.hasDescriptionPage
        ret._id=self.id
        ret._institutionName=self.institutionName
        ret._locale=self.locale
        ret._localeEnforced=self.localeEnforced
        ret._lockedOut=self.lockedOut
        ret._name=self.name
        ret._navCollapsable=self.navCollapsable
        ret._navColorBg=self.navColorBg
        ret._navColorFg=self.navColorFg
        ret._navigationStyle=self.navigationStyle
        ret._numberOfDaysOfUse=self.numberOfDaysOfUse
        ret._organization=self.organization
        ret._showInCatalog=self.showInCatalog
        ret._softLimit=self.softLimit
        ret._startDate=self.startDate
        ret._uploadLimit=self.uploadLimit
        return ret
        
    def __init__(self,CourseVO_Holder=None):
        if(CourseVO_Holder is not None):
            self.allowGuests = CourseVO_Holder._allowGuests
            self.allowObservers = CourseVO_Holder._allowObservers
            self.available = CourseVO_Holder._available
            self.batchUid = CourseVO_Holder._batchUid
            self.buttonStyleBbId = CourseVO_Holder._buttonStyleBbId
            self.buttonStyleShape = CourseVO_Holder._buttonStyleShape
            self.buttonStyleType = CourseVO_Holder._buttonStyleType
            self.cartridgeId = CourseVO_Holder._cartridgeId
            self.classificationId = CourseVO_Holder._classificationId
            self.courseDuration = CourseVO_Holder._courseDuration
            self.courseId = CourseVO_Holder._courseId
            self.coursePace = CourseVO_Holder._coursePace
            self.courseServiceLevel = CourseVO_Holder._courseServiceLevel
            self.dataSourceId = CourseVO_Holder._dataSourceId
            self.decAbsoluteLimit = CourseVO_Holder._decAbsoluteLimit
            self.description = CourseVO_Holder._description
            self.endDate = CourseVO_Holder._endDate
            self.enrollmentAccessCode = CourseVO_Holder._enrollmentAccessCode
            self.enrollmentEndDate = CourseVO_Holder._enrollmentEndDate
            self.enrollmentStartDate = CourseVO_Holder._enrollmentStartDate
            self.enrollmentType = CourseVO_Holder._enrollmentType
            self.expansionData = CourseVO_Holder._expansionData
            self.fee = CourseVO_Holder._fee
            self.hasDescriptionPage = CourseVO_Holder._hasDescriptionPage
            self.id = CourseVO_Holder._id
            self.institutionName = CourseVO_Holder._institutionName
            self.locale = CourseVO_Holder._locale
            self.localeEnforced = CourseVO_Holder._localeEnforced
            self.lockedOut = CourseVO_Holder._lockedOut
            self.name = CourseVO_Holder._name
            self.navCollapsable = CourseVO_Holder._navCollapsable
            self.navColorBg = CourseVO_Holder._navColorBg
            self.navColorFg = CourseVO_Holder._navColorFg
            self.navigationStyle = CourseVO_Holder._navigationStyle
            self.numberOfDaysOfUse = CourseVO_Holder._numberOfDaysOfUse
            self.organization = CourseVO_Holder._organization
            self.showInCatalog = CourseVO_Holder._showInCatalog
            self.softLimit = CourseVO_Holder._softLimit
            self.startDate = CourseVO_Holder._startDate
            self.uploadLimit = CourseVO_Holder._uploadLimit
            
            
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret

class CourseFilterVO(object):
    LOAD_ALL=0
    LOAD_BY_COURSEIDS=1
    LOAD_BY_BATCHUIDS=2
    LOAD_BY_IDS=3
    LOAD_BY_CATEGORIES=4
    LOAD_BY_SEARCH=5
    
    available = None
    batchUids = []
    categoryIds = []
    courseIds = []
    courseTemplates = []
    dataSourceIds = []
    expansionData = []
    filterType = None
    ids = []
    searchDate = None
    searchDateOperator = None
    searchKey = None
    searchOperator = None
    searchValue = None
    sourceBatchUids = []
    userIds = []
    
    def __init__(self,CourseFilterVO_Holder=None):
        if(CourseFilterVO_Holder is not None):
            self.available = CourseFilterVO_Holder._available
            self.batchUids = CourseFilterVO_Holder._batchUids
            self.categoryIds = CourseFilterVO_Holder._categoryIds
            self.courseIds = CourseFilterVO_Holder._courseIds
            self.courseTemplates = CourseFilterVO_Holder._courseTemplates
            self.dataSourceIds = CourseFilterVO_Holder._dataSourceIds
            self.expansionData = CourseFilterVO_Holder._expansionData
            self.filterType = CourseFilterVO_Holder._filterType
            self.ids = CourseFilterVO_Holder._ids
            self.searchDate = CourseFilterVO_Holder._searchDate
            self.searchDateOperator = CourseFilterVO_Holder._searchDateOperator
            self.searchKey = CourseFilterVO_Holder._searchKey
            self.searchOperator = CourseFilterVO_Holder._searchOperator
            self.searchValue = CourseFilterVO_Holder._searchValue
            self.sourceBatchUids = CourseFilterVO_Holder._sourceBatchUids
            self.userIds = CourseFilterVO_Holder._userIds
            
    def getCourseFilter_Def(self):
        filter = course_ns1.CourseFilter_Def(None)
        filter._available = self.available
        filter._batchUids = self.batchUids
        filter._categoryIds = self.categoryIds
        filter._courseIds = self.courseIds
        filter._courseTemplates = self.courseTemplates
        filter._dataSourceIds = self.dataSourceIds
        filter._expansionData = self.expansionData
        filter._filterType = self.filterType
        filter._ids = self.ids
        filter._searchDate = self.searchDate
        filter._searchDateOperator = self.searchDateOperator
        filter._searchKey = self.searchKey
        filter._searchOperator = self.searchOperator
        filter._searchValue = self.searchValue
        filter._sourceBatchUids = self.sourceBatchUids
        filter._userIds = self.userIds
        return filter  
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class CategoryVO(object):
    available = None
    batchUid = None
    dataSourceId = None
    description = None
    expansionData = []
    frontPage = None
    id = None
    organization = None
    parentId = None
    restricted = None
    title = None
    
    def __init__(self,CategoryVO_Holder=None):
        if(CategoryVO_Holder is not None):
            self.available = CategoryVO_Holder._available
            self.batchUid = CategoryVO_Holder._batchUid
            self.dataSourceId = CategoryVO_Holder._dataSourceId
            self.description = CategoryVO_Holder._description
            self.expansionData = CategoryVO_Holder._expansionData
            self.frontPage = CategoryVO_Holder._frontPage
            self.id = CategoryVO_Holder._id
            self.organization = CategoryVO_Holder._organization
            self.parentId = CategoryVO_Holder._parentId
            self.restricted = CategoryVO_Holder._restricted
            self.title = CategoryVO_Holder._title
            
    def getCategory_Def(self):
        CategoryVO_Holder = course_ns1.CategoryVO_Def(None)
        CategoryVO_Holder._available = self.available 
        CategoryVO_Holder._batchUid = self.batchUid
        CategoryVO_Holder._dataSourceId = self.dataSourceId
        CategoryVO_Holder._description = self.description
        CategoryVO_Holder._expansionData = self.expansionData
        CategoryVO_Holder._frontPage = self.frontPage
        CategoryVO_Holder._id = self.id 
        CategoryVO_Holder._organization = self.organization
        CategoryVO_Holder._parentId = self.parentId
        CategoryVO_Holder._restricted = self.restricted
        CategoryVO_Holder._title = self.title
        return CategoryVO_Holder
    
    def __str__(self):
        ret=""
        for x in dir(self):
            if "_" not in x :ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class CategoryFilterVO(object):
    GET_ALL_COURSE_CATEGORY=0
    GET_ALL_ORG_CATEGORY=1
    GET_CATEGORY_BY_ID=2
    GET_CATEGORY_BY_PARENT_ID=3
    
    expansionData = []
    filterType = None
    templateCategories = []
    
    def __init__(self,CategoryFilterVO_Holder=None):
        if(CategoryFilterVO_Holder is not None):
            self.expansionData = CategoryFilterVO_Holder._expansionData
            self.filterType = CategoryFilterVO_Holder._filterType
            self.templateCategories = CategoryFilterVO_Holder._templateCategories
            
    def getCategoryFilter_Def(self):
        filter = course_ns1.CategoryFilter_Def(None)
        filter._expansionData = self.expansionData
        filter._filterType = self.filterType
        filter._templateCategories = self.templateCategories
        return filter 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class CategoryMembershipVO(object):
    available = None
    categoryId = None
    courseId = None
    dataSourceId = None
    expansionData = []
    id = None
    organization = None
    
    def __init__(self,CategoryMembershipVO_Holder=None):
        if(CategoryMembershipVO_Holder is not None):
            self.available = CategoryMembershipVO_Holder._available
            self.categoryId = CategoryMembershipVO_Holder._categoryId
            self.courseId = CategoryMembershipVO_Holder._courseId
            self.dataSourceId = CategoryMembershipVO_Holder._dataSourceId
            self.expansionData = CategoryMembershipVO_Holder._expansionData
            self.id = CategoryMembershipVO_Holder._id
            self.organization = CategoryMembershipVO_Holder._organization
            
            
    def getCategoryMembershipVO_Def(self):
        categoryMembership = course_ns1.CategoryMembershipVO_Def(None)
        categoryMembership._available = self.available
        categoryMembership._categoryId = self.categoryId
        categoryMembership._courseId = self.courseId
        categoryMembership._dataSourceId = self.dataSourceId
        categoryMembership._expansionData = self.expansionData
        categoryMembership._id = self.id
        categoryMembership._organization = self.organization
        return categoryMembership 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret
    
class CategoryMembershipFilter(object):
    GET_CATEGORY_MEMBERSHIP_BY_ID=1
    GET_CATEGORY_MEMBERSHIP_BY_COURSE_ID=2
    
    expansionData = []
    filterType = None
    templateCategories = []
    
    def __init__(self,CategoryFilterVO_Holder=None):
        if(CategoryFilterVO_Holder is not None):
            self.expansionData = CategoryFilterVO_Holder._expansionData
            self.filterType = CategoryFilterVO_Holder._filterType
            self.templateCategories = CategoryFilterVO_Holder._templateCategories
            
    def getCategoryFilter_Def(self):
        filter = course_ns1.CategoryMembershipFilter_Def(None)
        filter._expansionData = self.expansionData
        filter._filterType = self.filterType
        ret = []
        for template in self.templateCategories:
            ret.append(template.getCategoryMembershipVO_Def())
        filter._templateCategoryMembership = ret
        return filter 
    
    def __str__(self):
        ret=""
        for x in dir(self):
            ret = ret + ":" +  x + ":" + str(getattr(self,x))
        return ret