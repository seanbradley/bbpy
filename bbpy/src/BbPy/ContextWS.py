'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''
from bbwsdl.Context_WS_services import *
from bbwsdl.Context_WS_services_types import *
from security.SignatureHandler import SignatureHandler
import logging
from UserWS import UserWS
from CourseWS import CourseWS
from CourseMembershipWS import CourseMembershipWS
from NauService import NauService
class ContextWS(object):
    """
    The ContextWS Object is the main entry point for this WebService
    """

    port=None
    """Connection to the WebService"""
    log=logging.getLogger("ContextWS")
    """Logging"""
    sigHandler=None
    """This signature handler does the authentication that Blackboard requires for their web services"""
    baseUrl=None
    """The base of the URL's to Blackboard learn"""
    
    def __init__(self, baseUrl=None):
        """
        Given a URL sets up the connection to the WebService. 
        
        If no baseUrl is given then the URL will be the same as the server that was used to generate bbwsdl.
        """
        self.baseUrl=baseUrl
        locator = Context_WSLocator()
        self.sigHandler = SignatureHandler("session","nosession",False)
        self.port=locator.getContext_WSPortType(baseUrl)
        self.port.binding.sig_handler=self.sigHandler
        
        request = getServerVersionRequest()
        response = self.port.getServerVersion(request)
    
        ret = response._return
        self.log.info("Connecting to ContextWS version: %s" % ret._version)
        
        request = initializeVersion2Request()
        response = self.port.initializeVersion2(request)
        sessionId = response._return
    
        self.sigHandler = SignatureHandler("session",sessionId,False)
        self.port.binding.sig_handler=self.sigHandler
        self.log.info("Received sessionId:%s from initializeVersion2 and set as password" %sessionId)
        self.log.info("Should be all set to use other functions!")
    
    def registerTool(self,vendorId,programId,registrationPassword,description,toolMethods,ticketMethods=[]):
        """
        Register a tool with a Learn instance.
        
        This allows you to register an application with a Bb Learn server. You request tool methods. 
        You then authorize the tool and assign a password in the Blackboard server GUI under Proxy Tools.
        
        @param vendorId: The Vendor ID to register with Learn
        @type vendorId: String
        @param programId: The Vendor ID to register with Learn
        @type programId: String
        @param registrationPassword: The Vendor ID to register with Learn
        @type registrationPassword: String
        @param description: The Vendor ID to register with Learn
        @type description: String
        @param toolMethods: The Vendor ID to register with Learn
        @type toolMethods: [String]
        @param ticketMethods: The Vendor ID to register with Learn
        @type ticketMethods: [String]
        @return: This function returns a tuple of 
            (failureErrors,proxyToolGuid,status)
        
        @note: Example toolMethods C{
        toolMethods = ["User.WS:getServerVersion", 
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
        }
        """
        request = registerToolRequest()
        request._clientVendorId = vendorId
        request._clientProgramId = programId
        request._registrationPassword = registrationPassword
        request._description = description
        request._requiredToolMethods = toolMethods
        request._requiredTicketMethods = ticketMethods
        
        response = self.port.registerTool(request)
        return (response._return._failureErrors,response._return._proxyToolGuid,response._return._status)
    
    def loginTool(self,vendorId,programId,sharedSecret):
        self.log.debug("loginTool")
        request = loginToolRequest()
        request._password = sharedSecret
        request._clientVendorId = vendorId
        request._clientProgramId = programId
        
        response = self.port.loginTool(request)
        return response._return
    
    def getUserWS(self):
        return UserWS(self.sigHandler, self.baseUrl)
    
    def getCourseWS(self):
        return CourseWS(self.sigHandler, self.baseUrl)
    
    def getCourseMembershipWS(self):
        return CourseMembershipWS(self.sigHandler, self.baseUrl)
    
    def getNauService(self):
        return NauService(self.sigHandler, self.baseUrl)
        