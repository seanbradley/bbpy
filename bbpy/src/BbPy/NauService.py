'''
Created on Jan 11, 2011

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
from bbwsdl.NauService_services import *
from bbwsdl.NauService_services_types import *
import logging
class NauService(object):
    log=logging.getLogger("NauService")
    port=None
    sigHandler=None
    def __init__(self,sigHandler, baseUrl=None):
        self.sigHandler=sigHandler
        
        locator = NauServiceLocator()
        self.port=locator.getNauServicePortType(baseUrl)
        self.port.binding.sig_handler=self.sigHandler
        
        self.log.info("Connecting to NauService")
    def batchChangeEnrollmentStatus(self,courseBatchUid,peopleBatchUids,disabled=False):
        request = BatchChangeEnrollmentStatusRequest()
        request._courseBatchUid=courseBatchUid
        request._peopleBatchUid=peopleBatchUids
        request._disabled=disabled
        response = self.port.BatchChangeEnrollmentStatus(request)
        return response._return
    
    def getIdsFromBatchUids(self, batchUids):
        request = GetIdsFromBatchUidsRequest()
        request._batchUids=batchUids
        responses = self.port.GetIdsFromBatchUids(request)
        ## Return $ delimited into hash
        ret = dict()
        for response in responses._return:
            parts=response.split("$")
            ret[parts[0]]=parts[1]
        return ret
    
    def changeEnrollmentStatus(self,courseBatchUid,personBatchUid,disabled=False):
        request = ChangeEnrollmentStatusRequest()
        request._courseBatchUid=courseBatchUid
        request._personBatchUid=personBatchUid
        request._disabled=disabled
        response = self.port.ChangeEnrollmentStatus(request)
        return response._return
    
    def rollupCourse(self, parentBatchUid, childBatchUid, enable=True):
        request = RollupCourseRequest()
        request._parentBatchUid=parentBatchUid
        request._childBatchUid=childBatchUid
        request._enable=enable
        response=self.port.RollupCourse(request)
        return response._return
    
    def isRolledup(self, parentBatchUid, childBatchUid):
        request = IsRolledupRequest()
        request._parentBatchUid=parentBatchUid
        request._childBatchUid=childBatchUid
        response=self.port.IsRolledup(request)
        return response._return
    
    def createUpdateUser(self,studentId, firstName, lastName, email, userName, isAvailable=True):
        request = CreateUpdateUserRequest()
        request._studentId=studentId
        request._firstName=firstName
        request._lastName=lastName
        request._email=email
        request._userName=userName
        request._isAvailable=isAvailable
        response=self.port.CreateUpdateUser(request)
        return response._return