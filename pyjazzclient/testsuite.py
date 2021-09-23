import xml.etree.ElementTree as ET

from .jazzartifact import JazzArtifact


class TestsuiteConstants():
    TESTSUITE_URL = ("/service/com.ibm.rqm.integration.service.IIntegrationService/"
                     "resources/{project}/testsuite/")

    TESTSUITE_URN = "urn:com.ibm.rqm:testsuite:{web_id}"

    NAMESPACES = {
        "ns1": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "ns2": "http://jazz.net/xmlns/alm/qm/v0.1/",
        "ns3": "http://schema.ibm.com/vega/2008/",
        "ns4": "http://purl.org/dc/elements/1.1/",
        "ns5": "http://jazz.net/xmlns/prod/jazz/process/0.6/",
        "ns6": "http://jazz.net/xmlns/alm/v0.1/",
        "ns7": "http://purl.org/dc/terms/",
        "ns8": "http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/",
        "ns9": "http://jazz.net/xmlns/alm/qm/v0.1/executionworkitem/v0.1",
        "ns10": "http://open-services.net/ns/core#",
        "ns11": "http://open-services.net/ns/qm#",
        "ns12": "http://jazz.net/xmlns/prod/jazz/rqm/process/1.0/",
        "ns13": "http://www.w3.org/2002/07/owl#",
        "ns14": "http://jazz.net/xmlns/alm/qm/qmadapter/v0.1",
        "ns15": "http://jazz.net/xmlns/alm/qm/qmadapter/task/v0.1",
        "ns16": "http://jazz.net/xmlns/alm/qm/v0.1/executionresult/v0.1",
        "ns17": "http://jazz.net/xmlns/alm/qm/v0.1/catalog/v0.1",
        "ns18": "http://jazz.net/xmlns/alm/qm/v0.1/tsl/v0.1/",
        "ns20": "http://jazz.net/xmlns/alm/qm/styleinfo/v0.1/",
        "ns21": "http://www.w3.org/1999/XSL/Transform"
    }

    WEB_ID_PATH = "ns2:webId"
    TITLE_PATH = "ns4:title"
    IDENTIFIER_PATH = "ns4:identifier"
    STYLESHEET_PATH = "ns2:stylesheet"
    PROJECT_AREA_PATH = "ns2:projectArea"
    DESCRIPTION_PATH = "ns4:description"
    CREATION_DATE_PATH = "ns2:creationDate"
    UPDATED_PATH = "ns6:updated"
    STATE_PATH = "ns6:state"
    CREATOR_PATH = "ns4:creator"
    OWNER_PATH = "ns6:owner"
    LOCKED_PATH = "ns2:locked"


class TestSuite(JazzArtifact):

    def __init__(self, xml=None):
        super(TestSuite, self).__init__(xml)
        # pass
        if (xml is None):
            namespaces = [f'xmlns:{prefix}="{uri}"' for prefix,
                          uri in TestsuiteConstants.NAMESPACES.items()]
            empty_testsuite_xml = '<?xml version="1.0" encoding="UTF-8"?><ns2:testsuite {}></ns2:testsuite>'.format(
                " ".join(namespaces))

            self.xml = ET.fromstring(empty_testsuite_xml)

    @property
    def project_area(self):
        return self.get_attribute_from_element_path(TestsuiteConstants.PROJECT_AREA_PATH, "href",
                                                    TestsuiteConstants.NAMESPACES)

    @property
    def identifier(self):
        return self.get_text_from_element_path(TestsuiteConstants.IDENTIFIER_PATH, TestsuiteConstants.NAMESPACES)

    @property
    def stylesheet(self):
        return self.get_attribute_from_element_path(TestsuiteConstants.STYLESHEET_PATH, "href",
                                                    TestsuiteConstants.NAMESPACES)

    @property
    def web_id(self):
        return self.get_text_from_element_path(TestsuiteConstants.WEB_ID_PATH, TestsuiteConstants.NAMESPACES)

    @property
    def title(self):
        return self.get_text_from_element_path(TestsuiteConstants.TITLE_PATH, TestsuiteConstants.NAMESPACES)

    @ title.setter
    def title(self, value):
        element = self.xml.find(
            TestsuiteConstants.TITLE_PATH, TestsuiteConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestsuiteConstants.NAMESPACES["ns4"] + "}title"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def description(self):
        return self.get_text_from_element_path(TestsuiteConstants.DESCRIPTION_PATH, TestsuiteConstants.NAMESPACES)

    @ description.setter
    def description(self, value):
        element = self.xml.find(
            TestsuiteConstants.DESCRIPTION_PATH, TestsuiteConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestsuiteConstants.NAMESPACES["ns4"] + "}description"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def creation_date(self):
        return self.get_text_from_element_path(TestsuiteConstants.CREATION_DATE_PATH, TestsuiteConstants.NAMESPACES)

    @property
    def updated(self):
        return self.get_text_from_element_path(TestsuiteConstants.UPDATED_PATH, TestsuiteConstants.NAMESPACES)

    @property
    def state(self):
        return self.get_attribute_from_element_path(
            TestsuiteConstants.STATE_PATH,
            "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", TestsuiteConstants.NAMESPACES)

    # TODO - Create setter for state

    @property
    def creator(self):
        return self.get_attributes_from_element_path(
            TestsuiteConstants.CREATOR_PATH,
            ["name", "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"], TestsuiteConstants.NAMESPACES)

    @property
    def locked(self):
        return self.get_text_from_element_path(TestsuiteConstants.LOCKED_PATH, TestsuiteConstants.NAMESPACES)
