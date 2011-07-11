import time
import random
import hashlib
import binascii
import logging
'''
Created on Oct 27, 2010

@author: Chris Greenough - Chris.Greenough@nau.edu
'''

class SignatureHandler(object):
    '''
    classdocs
    '''
    OASIS_PREFIX = "http://docs.oasis-open.org/wss/2004/01/oasis-200401"
    SEC_NS = OASIS_PREFIX + "-wss-wssecurity-secext-1.0.xsd"
    UTIL_NS = OASIS_PREFIX + "-wss-wssecurity-utility-1.0.xsd"
    PASSWORD_DIGEST_TYPE = OASIS_PREFIX + "-wss-username-token-profile-1.0#PasswordDigest"
    PASSWORD_PLAIN_TYPE = OASIS_PREFIX + "-wss-username-token-profile-1.0#PasswordText"
    log=logging.getLogger("SignatureHandler")
    def __init__(self,user,password,useDigest=False):
        '''
        Constructor
        '''
        self._user=user
        self._created=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(time.time()))
        self._nonce=hashlib.new("sha",str(random.random())).digest()
        if(useDigest):
            self._passwordType=self.PASSWORD_DIGEST_TYPE
            digest=hashlib.new("sha",self._nonce+self._created+password).digest()
            self._password=binascii.b2a_base64(digest)[:-1]
        else:
            self._passwordType=self.PASSWORD_PLAIN_TYPE
            self._password=password
    
    def sign(self,soapWriter):
        # create element
        securityElem = soapWriter._header.createAppendElement("", "wsse:Security")
        securityElem.node.setAttribute("xmlns:wsse", self.SEC_NS)
        securityElem.node.setAttribute("SOAP-ENV:mustunderstand", "true")
        
        # create element
        timestampElem = securityElem.createAppendElement("", "wsse:Timestamp")
        timestampElem.node.setAttribute("xmlns:wsse", self.UTIL_NS)
        
        # create element
        createdElem = timestampElem.createAppendElement("", "wsse:Created")
        createdElem.node.setAttribute("xmlns:wsse", self.UTIL_NS)
        
        createdElem.createAppendTextNode(self._created)
        
        # create element
        usernameTokenElem = securityElem.createAppendElement("", "wsse:UsernameToken")
        usernameTokenElem.node.setAttribute("xmlns:wsse", self.SEC_NS)
        usernameTokenElem.node.setAttribute("xmlns:wsu", self.UTIL_NS)
        
        # create element
        usernameElem = usernameTokenElem.createAppendElement("", "wsse:Username")
        usernameElem.node.setAttribute("xmlns:wsse", self.SEC_NS)
        
        # create element
        passwordElem = usernameTokenElem.createAppendElement("", "wsse:Password")
        passwordElem.node.setAttribute("xmlns:wsse", self.SEC_NS)
        passwordElem.node.setAttribute("Type", self._passwordType)
        
        # create element
        #nonceElem = usernameTokenElem.createAppendElement("", "wsse:Nonce")
        #nonceElem.node.setAttribute("xmlns:wsse", self.SEC_NS)
        
        
        
        # put values in elements
        usernameElem.createAppendTextNode(self._user)
        passwordElem.createAppendTextNode(self._password)
        # binascii.b2a_base64 adds a newline at the end
        #nonceElem. createAppendTextNode(binascii.b2a_base64(self._nonce)[:-1])
        
        self.log.debug(soapWriter)
        
    def verify(self,soapWriter):
        self
        