################################################## 
# User_WS_services.py 
# generated by ZSI.generate.wsdl2python
##################################################


from User_WS_services_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
import ZSI

# Locator
class User_WSLocator:
    User_WSPortType_address = "https://dev.bblearn.nau.edu/webapps/ws/services/User.WS"
    def getUser_WSPortTypeAddress(self):
        return User_WSLocator.User_WSPortType_address
    def getUser_WSPortType(self, url=None, **kw):
        if url:
            url = url + "/webapps/ws/services/User.WS"
            return User_WSSOAP11BindingSOAP(url, **kw)
        else:
            return User_WSSOAP11BindingSOAP(User_WSLocator.User_WSPortType_address, **kw)

# Methods
class User_WSSOAP11BindingSOAP:
    def __init__(self, url, endPointReference=None, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        self.endPointReference = endPointReference

    # op: getUser
    def getUser(self, request):
        if isinstance(request, getUserRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getUserRequest"
        self.binding.Send(None, None, request, soapaction="getUser", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getUserResponse"
        response = self.binding.Receive(getUserResponse.typecode, wsaction=wsaction)
        return response

    # op: getSystemRoles
    def getSystemRoles(self, request):
        if isinstance(request, getSystemRolesRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getSystemRolesRequest"
        self.binding.Send(None, None, request, soapaction="getSystemRoles", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getSystemRolesResponse"
        response = self.binding.Receive(getSystemRolesResponse.typecode, wsaction=wsaction)
        return response

    # op: saveUser
    def saveUser(self, request):
        if isinstance(request, saveUserRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveUserRequest"
        self.binding.Send(None, None, request, soapaction="saveUser", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveUserResponse"
        response = self.binding.Receive(saveUserResponse.typecode, wsaction=wsaction)
        return response

    # op: saveObserverAssociation
    def saveObserverAssociation(self, request):
        if isinstance(request, saveObserverAssociationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveObserverAssociationRequest"
        self.binding.Send(None, None, request, soapaction="saveObserverAssociation", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveObserverAssociationResponse"
        response = self.binding.Receive(saveObserverAssociationResponse.typecode, wsaction=wsaction)
        return response

    # op: saveAddressBookEntry
    def saveAddressBookEntry(self, request):
        if isinstance(request, saveAddressBookEntryRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveAddressBookEntryRequest"
        self.binding.Send(None, None, request, soapaction="saveAddressBookEntry", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/saveAddressBookEntryResponse"
        response = self.binding.Receive(saveAddressBookEntryResponse.typecode, wsaction=wsaction)
        return response

    # op: deleteUserByInstitutionRole
    def deleteUserByInstitutionRole(self, request):
        if isinstance(request, deleteUserByInstitutionRoleRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteUserByInstitutionRoleRequest"
        self.binding.Send(None, None, request, soapaction="deleteUserByInstitutionRole", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteUserByInstitutionRoleResponse"
        response = self.binding.Receive(deleteUserByInstitutionRoleResponse.typecode, wsaction=wsaction)
        return response

    # op: initializeUserWS
    def initializeUserWS(self, request):
        if isinstance(request, initializeUserWSRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/initializeUserWSRequest"
        self.binding.Send(None, None, request, soapaction="initializeUserWS", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/initializeUserWSResponse"
        response = self.binding.Receive(initializeUserWSResponse.typecode, wsaction=wsaction)
        return response

    # op: changeUserBatchUid
    def changeUserBatchUid(self, request):
        if isinstance(request, changeUserBatchUidRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/changeUserBatchUidRequest"
        self.binding.Send(None, None, request, soapaction="changeUserBatchUid", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/changeUserBatchUidResponse"
        response = self.binding.Receive(changeUserBatchUidResponse.typecode, wsaction=wsaction)
        return response

    # op: changeUserDataSourceId
    def changeUserDataSourceId(self, request):
        if isinstance(request, changeUserDataSourceIdRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/changeUserDataSourceIdRequest"
        self.binding.Send(None, None, request, soapaction="changeUserDataSourceId", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/changeUserDataSourceIdResponse"
        response = self.binding.Receive(changeUserDataSourceIdResponse.typecode, wsaction=wsaction)
        return response

    # op: deleteObserverAssociation
    def deleteObserverAssociation(self, request):
        if isinstance(request, deleteObserverAssociationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteObserverAssociationRequest"
        self.binding.Send(None, None, request, soapaction="deleteObserverAssociation", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteObserverAssociationResponse"
        response = self.binding.Receive(deleteObserverAssociationResponse.typecode, wsaction=wsaction)
        return response

    # op: getUserInstitutionRoles
    def getUserInstitutionRoles(self, request):
        if isinstance(request, getUserInstitutionRolesRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getUserInstitutionRolesRequest"
        self.binding.Send(None, None, request, soapaction="getUserInstitutionRoles", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getUserInstitutionRolesResponse"
        response = self.binding.Receive(getUserInstitutionRolesResponse.typecode, wsaction=wsaction)
        return response

    # op: getInstitutionRoles
    def getInstitutionRoles(self, request):
        if isinstance(request, getInstitutionRolesRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getInstitutionRolesRequest"
        self.binding.Send(None, None, request, soapaction="getInstitutionRoles", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getInstitutionRolesResponse"
        response = self.binding.Receive(getInstitutionRolesResponse.typecode, wsaction=wsaction)
        return response

    # op: deleteAddressBookEntry
    def deleteAddressBookEntry(self, request):
        if isinstance(request, deleteAddressBookEntryRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteAddressBookEntryRequest"
        self.binding.Send(None, None, request, soapaction="deleteAddressBookEntry", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteAddressBookEntryResponse"
        response = self.binding.Receive(deleteAddressBookEntryResponse.typecode, wsaction=wsaction)
        return response

    # op: getObservee
    def getObservee(self, request):
        if isinstance(request, getObserveeRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getObserveeRequest"
        self.binding.Send(None, None, request, soapaction="getObservee", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getObserveeResponse"
        response = self.binding.Receive(getObserveeResponse.typecode, wsaction=wsaction)
        return response

    # op: deleteUser
    def deleteUser(self, request):
        if isinstance(request, deleteUserRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteUserRequest"
        self.binding.Send(None, None, request, soapaction="deleteUser", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/deleteUserResponse"
        response = self.binding.Receive(deleteUserResponse.typecode, wsaction=wsaction)
        return response

    # op: getServerVersion
    def getServerVersion(self, request):
        if isinstance(request, getServerVersionRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getServerVersionRequest"
        self.binding.Send(None, None, request, soapaction="getServerVersion", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getServerVersionResponse"
        response = self.binding.Receive(getServerVersionResponse.typecode, wsaction=wsaction)
        return response

    # op: getAddressBookEntry
    def getAddressBookEntry(self, request):
        if isinstance(request, getAddressBookEntryRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://user.ws.blackboard/User.WSPortType/getAddressBookEntryRequest"
        self.binding.Send(None, None, request, soapaction="getAddressBookEntry", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://user.ws.blackboard/User.WSPortType/getAddressBookEntryResponse"
        response = self.binding.Receive(getAddressBookEntryResponse.typecode, wsaction=wsaction)
        return response

getUserRequest = user_ns1.getUser_Dec().pyclass

getUserResponse = user_ns1.getUserResponse_Dec().pyclass

getSystemRolesRequest = user_ns1.getSystemRoles_Dec().pyclass

getSystemRolesResponse = user_ns1.getSystemRolesResponse_Dec().pyclass

saveUserRequest = user_ns1.saveUser_Dec().pyclass

saveUserResponse = user_ns1.saveUserResponse_Dec().pyclass

saveObserverAssociationRequest = user_ns1.saveObserverAssociation_Dec().pyclass

saveObserverAssociationResponse = user_ns1.saveObserverAssociationResponse_Dec().pyclass

saveAddressBookEntryRequest = user_ns1.saveAddressBookEntry_Dec().pyclass

saveAddressBookEntryResponse = user_ns1.saveAddressBookEntryResponse_Dec().pyclass

deleteUserByInstitutionRoleRequest = user_ns1.deleteUserByInstitutionRole_Dec().pyclass

deleteUserByInstitutionRoleResponse = user_ns1.deleteUserByInstitutionRoleResponse_Dec().pyclass

initializeUserWSRequest = user_ns1.initializeUserWS_Dec().pyclass

initializeUserWSResponse = user_ns1.initializeUserWSResponse_Dec().pyclass

changeUserBatchUidRequest = user_ns1.changeUserBatchUid_Dec().pyclass

changeUserBatchUidResponse = user_ns1.changeUserBatchUidResponse_Dec().pyclass

changeUserDataSourceIdRequest = user_ns1.changeUserDataSourceId_Dec().pyclass

changeUserDataSourceIdResponse = user_ns1.changeUserDataSourceIdResponse_Dec().pyclass

deleteObserverAssociationRequest = user_ns1.deleteObserverAssociation_Dec().pyclass

deleteObserverAssociationResponse = user_ns1.deleteObserverAssociationResponse_Dec().pyclass

getUserInstitutionRolesRequest = user_ns1.getUserInstitutionRoles_Dec().pyclass

getUserInstitutionRolesResponse = user_ns1.getUserInstitutionRolesResponse_Dec().pyclass

getInstitutionRolesRequest = user_ns1.getInstitutionRoles_Dec().pyclass

getInstitutionRolesResponse = user_ns1.getInstitutionRolesResponse_Dec().pyclass

deleteAddressBookEntryRequest = user_ns1.deleteAddressBookEntry_Dec().pyclass

deleteAddressBookEntryResponse = user_ns1.deleteAddressBookEntryResponse_Dec().pyclass

getObserveeRequest = user_ns1.getObservee_Dec().pyclass

getObserveeResponse = user_ns1.getObserveeResponse_Dec().pyclass

deleteUserRequest = user_ns1.deleteUser_Dec().pyclass

deleteUserResponse = user_ns1.deleteUserResponse_Dec().pyclass

getServerVersionRequest = user_ns1.getServerVersion_Dec().pyclass

getServerVersionResponse = user_ns1.getServerVersionResponse_Dec().pyclass

getAddressBookEntryRequest = user_ns1.getAddressBookEntry_Dec().pyclass

getAddressBookEntryResponse = user_ns1.getAddressBookEntryResponse_Dec().pyclass
