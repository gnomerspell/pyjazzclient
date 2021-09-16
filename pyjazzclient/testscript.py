
from typing import Text
import xml.etree.ElementTree as ET

from .jazzartifact import JazzArtifact


class TestscriptConstants():
    TESTSCRIPT_URL = ("/service/com.ibm.rqm.integration.service.IIntegrationService/"
                      "resources/{project}/testscript/")

    TESTSCRIPT_URN = "urn:com.ibm.rqm:testscript:{web_id}"

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
    STEPS_PATH = "ns2:steps"
    STEP_PATH = "ns8:step"


class TestScript(JazzArtifact):

    def __init__(self, xml=None):
        super(TestScript, self).__init__(xml)
        # pass
        if (xml is None):
            namespaces = [f'xmlns:{prefix}="{uri}"' for prefix,
                          uri in TestscriptConstants.NAMESPACES.items()]
            empty_testscript_xml = '<?xml version="1.0" encoding="UTF-8"?><ns2:testscript {}></ns2:testscript>'.format(
                " ".join(namespaces))

            self.xml = ET.fromstring(empty_testscript_xml)
            _ = ET.SubElement(
                self.xml, "{http://jazz.net/xmlns/alm/qm/v0.1/}steps")
            self.append_step("", "", "_", "", "")

    @property
    def project_area(self):
        return self.get_attribute_from_element_path(TestscriptConstants.PROJECT_AREA_PATH, "href",
                                                    TestscriptConstants.NAMESPACES)

    @property
    def identifier(self):
        return self.get_text_from_element_path(TestscriptConstants.IDENTIFIER_PATH, TestscriptConstants.NAMESPACES)

    @property
    def stylesheet(self):
        return self.get_attribute_from_element_path(TestscriptConstants.STYLESHEET_PATH, "href",
                                                    TestscriptConstants.NAMESPACES)

    @property
    def web_id(self):
        return self.get_text_from_element_path(TestscriptConstants.WEB_ID_PATH, TestscriptConstants.NAMESPACES)

    @property
    def title(self):
        return self.get_text_from_element_path(TestscriptConstants.TITLE_PATH, TestscriptConstants.NAMESPACES)

    @ title.setter
    def title(self, value):
        element = self.xml.find(
            TestscriptConstants.TITLE_PATH, TestscriptConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestscriptConstants.NAMESPACES["ns4"] + "}title"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def description(self):
        return self.get_text_from_element_path(TestscriptConstants.DESCRIPTION_PATH, TestscriptConstants.NAMESPACES)

    @ description.setter
    def description(self, value):
        element = self.xml.find(
            TestscriptConstants.DESCRIPTION_PATH, TestscriptConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestscriptConstants.NAMESPACES["ns4"] + "}description"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def creation_date(self):
        return self.get_text_from_element_path(TestscriptConstants.CREATION_DATE_PATH, TestscriptConstants.NAMESPACES)

    @property
    def updated(self):
        return self.get_text_from_element_path(TestscriptConstants.UPDATED_PATH, TestscriptConstants.NAMESPACES)

    @property
    def state(self):
        return self.get_attribute_from_element_path(
            TestscriptConstants.STATE_PATH,
            "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", TestscriptConstants.NAMESPACES)

    # TODO - Create setter for state

    @property
    def creator(self):
        return self.get_attributes_from_element_path(
            TestscriptConstants.CREATOR_PATH,
            ["name", "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"], TestscriptConstants.NAMESPACES)

    # TODO: Work
    # @property
    # def owner(self):
    #     pass

    @property
    def locked(self):
        return self.get_text_from_element_path(TestscriptConstants.LOCKED_PATH, TestscriptConstants.NAMESPACES)

    def append_step(self, name: str, title: str, description: str, comment: str, compare: str) -> None:
        steps_element = self.xml.find(
            TestscriptConstants.STEPS_PATH, TestscriptConstants.NAMESPACES)
        step_element = self.create_subelement(steps_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}step",
                                              attrib={"type": "execution"})
        _ = self.create_subelement(
            step_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}name", text=name)
        _ = self.create_subelement(
            step_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}title", text=title)
        _ = self.create_subelement(
            step_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}description", text=description)
        _ = self.create_subelement(
            step_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}comment", text=comment)
        _ = self.create_subelement(
            step_element, "{http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/}compare", text=compare)
