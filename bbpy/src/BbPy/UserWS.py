'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
##from bbwsdl.User_WS_services import *
##from bbwsdl.User_WS_services_types import *
from bbwsdl import User_WS_services
import logging
from BbPy.VO.UserWS import *
class UserWS(object):
    log=logging.getLogger("UserWS")
    port=None
    sigHandler=None
    def __init__(self,sigHandler, baseUrl=None):
        self.sigHandler=sigHandler
        
        locator = User_WSLocator()
        self.port=locator.getUser_WSPortType(baseUrl)
        self.port.binding.sig_handler=self.sigHandler
        
        request = User_WS_services.getServerVersionRequest()
        response = self.port.getServerVersion(request)
    
        ret = response._return
        self.log.info("Connecting to UserWS version: %s" % ret._version)
        
    def getUser(self,userFilterVO):
        request = getUserRequest()
        request._filter=userFilterVO.getUserFilter_Def()
        response = self.port.getUser(request)
        return map(UserVO,response._return)
        
    def getUserByBatchId(self,batchId):
        filter = UserFilterVO()
        filter.batchId=(batchId,)
        filter.filterType=UserFilterVO.GET_USER_BY_BATCH_ID_WITH_AVAILABILITY
        filter.available=True
        users = self.getUser(filter)
        if len(users) == 1: return users[0] 
        else: return None
        
    def getUserByUserId(self,userId):
        filter = UserFilterVO()
        filter.name=(userId,)
        filter.filterType=UserFilterVO.GET_USER_BY_NAME_WITH_AVAILABILITY
        filter.available=True
        users = self.getUser(filter)
        if len(users) == 1: return users[0] 
        else: return None
        
    def getUserById(self,id):
        filter = UserFilterVO()
        filter.id=(id,)
        filter.filterType=UserFilterVO.GET_USER_BY_ID_WITH_AVAILABILITY
        filter.available=True
        users = self.getUser(filter)
        if len(users) == 1: return users[0] 
        else: return None
        
    def createSimpleUser(self, isAvailable, userName, studentId, email, firstName, lastName, *insRoles):
        """
        @param isAvailable: boolean - Sets active
        @param userName: string - Sets userID
        @param studentId: string - Sets Student ID and batchUid
        @param email: string - Sets email
        @param firstName: string - Sets First Name
        @param lastName: string - Sets Last Name
        @param *instRoles: all the rest of the params will turn into institutional roles. First one being primary.
        """
        user = UserVO()
        user.userBatchUid=studentId
        user.isAvailable=isAvailable
        user.name=userName
        user.studentId=studentId
        extendedInfo = ExtendedInfoVO()
        extendedInfo.emailAddress = email
        extendedInfo.familyName = firstName
        extendedInfo.givenName = lastName
        user.extendedInfo = extendedInfo
        user.insRoles = insRoles
        return self.saveUser(user)
    
    def updateSimpleUser(self,isAvailable, userName, studentId, email, firstName, lastName, *insRoles):
        """
        @param isAvailable: boolean - Sets active
        @param userName: string - Sets userID
        @param studentId: string - Sets Student ID and batchUid
        @param email: string - Sets email
        @param firstName: string - Sets First Name
        @param lastName: string - Sets Last Name
        @param *instRoles: all the rest of the params will turn into institutional roles. First one being primary.
        """
        user = self.getUserByBatchId(studentId)
        if user is None:
            user = UserVO()
        user.userBatchUid=studentId
        user.isAvailable=isAvailable
        user.name=userName
        user.studentId=studentId
        extendedInfo = ExtendedInfoVO()
        extendedInfo.emailAddress = email
        extendedInfo.familyName = firstName
        extendedInfo.givenName = lastName
        user.extendedInfo = extendedInfo
        user.insRoles = insRoles
        return self.saveUser(user)
        
    def saveUser(self,userVO):
        request = saveUserRequest()
        request._user=[userVO.getUser_Def()]
        response = self.port.saveUser(request)
        return response._return
    
    def saveUsers(self,userVOs):
        request = saveUserRequest()
        ret = []
        for userVo in userVOs:
            ret.append(userVo.getUser_Def())
        request._user=ret
        response = self.port.saveUser(request)
        return response._return
    
    def deleteUser(self,userId):
        request = deleteUserRequest()
        request._userId=[userId]
        response = self.port.deleteUser(request)
        return response._return
    
    def deleteUsers(self,userIds):
        request = deleteUserRequest()
        request._userId=userIds
        response = self.port.deleteUser(request)
        return response._return
    
    def changeUserBatchUid(self,origionalBatchUid,newBatchUid):
        request = changeUserBatchUidRequest()
        request._originalBatchUid=origionalBatchUid
        request._batchUid=newBatchUid
        response = self.port.changeUserBatchUid(request)
        return response._return
        
        
        
    
        
        