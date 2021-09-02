
import xml.etree.ElementTree as ET

from .jazzartifact import JazzArtifact


class TestcaseConstants():
    TESTCASE_URL = ("/service/com.ibm.rqm.integration.service.IIntegrationService/"
                    "resources/{project}/testcase/")

    TESTCASE_URN = "urn:com.ibm.rqm:testcase:{web_id}"

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
    WEIGHT_PATH = "ns2:weight"
    SUSPECT_PATH = "ns2:suspect"
    TESTCASE_EXECUTION_RECORD_COUNT = "ns2:testCaseExecutionRecordCount"
    SCRIPT_STEP_COUNT = "ns2:scriptStepCount"
    TEMPLATE_PATH = "ns2:template"
    COMPONENT_PATH = "ns2:component"
    TESTCASE_DESIGN_PATH = "ns2:com.ibm.rqm.planning.editor.section.testCaseDesign"
    TESTCASE_PRECONDITION_PATH = "ns2:com.ibm.rqm.planning.editor.section.testCasePreCondition"
    TESTCASE_POSTCONDITION_PATH = "ns2:com.ibm.rqm.planning.editor.section.testCasePostCondition"
    TESTSCRIPTS_PATH = "ns2:testscript"
    TESTCASE_EXECUTION_RECORDS_PATH = ""
    VARIABLES_PATH = "ns2:variables/ns2:variable"
    ATTACHMENTS = "ns2:attachment"
    TESTCASE_EXPECTED_RESULTS = "ns2:com.ibm.rqm.planning.editor.section.testCaseExpectedResults"


class TestCase(JazzArtifact):

    def __init__(self, xml=None):
        super(TestCase, self).__init__(xml)
        # pass
        if (xml is None):
            empty_testcase_xml = """<?xml version="1.0" encoding="UTF-8"?>
                                    <ns2:testcase xmlns:ns2="http://jazz.net/xmlns/alm/qm/v0.1/"
                                        xmlns:ns1="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                                        xmlns:ns3="http://schema.ibm.com/vega/2008/"
                                        xmlns:ns4="http://purl.org/dc/elements/1.1/"
                                        xmlns:ns5="http://jazz.net/xmlns/prod/jazz/process/0.6/"
                                        xmlns:ns6="http://jazz.net/xmlns/alm/v0.1/"
                                        xmlns:ns7="http://purl.org/dc/terms/"
                                        xmlns:ns8="http://jazz.net/xmlns/alm/qm/v0.1/testscript/v0.1/"
                                        xmlns:ns9="http://jazz.net/xmlns/alm/qm/v0.1/executionworkitem/v0.1"
                                        xmlns:ns10="http://open-services.net/ns/core#"
                                        xmlns:ns11="http://open-services.net/ns/qm#"
                                        xmlns:ns12="http://jazz.net/xmlns/prod/jazz/rqm/process/1.0/"
                                        xmlns:ns13="http://www.w3.org/2002/07/owl#"
                                        xmlns:ns14="http://jazz.net/xmlns/alm/qm/qmadapter/v0.1"
                                        xmlns:ns15="http://jazz.net/xmlns/alm/qm/qmadapter/task/v0.1"
                                        xmlns:ns16="http://jazz.net/xmlns/alm/qm/v0.1/executionresult/v0.1"
                                        xmlns:ns17="http://jazz.net/xmlns/alm/qm/v0.1/catalog/v0.1"
                                        xmlns:ns18="http://jazz.net/xmlns/alm/qm/v0.1/tsl/v0.1/"
                                        xmlns:ns20="http://jazz.net/xmlns/alm/qm/styleinfo/v0.1/"
                                        xmlns:ns21="http://www.w3.org/1999/XSL/Transform">
                                    </ns2:testcase>"""
            self.xml = ET.fromstring(empty_testcase_xml)

        # for prefix, uri in Constants.NAMESPACES.items():
        #     ET.register_namespace(prefix, uri)

    @property
    def project_area(self):
        return self.get_attribute_from_element_path(TestcaseConstants.PROJECT_AREA_PATH, "href", TestcaseConstants.NAMESPACES)

    @property
    def identifier(self):
        return self.get_text_from_element_path(TestcaseConstants.IDENTIFIER_PATH, TestcaseConstants.NAMESPACES)

    @property
    def stylesheet(self):
        return self.get_attribute_from_element_path(TestcaseConstants.STYLESHEET_PATH, "href", TestcaseConstants.NAMESPACES)

    @property
    def web_id(self):
        return self.get_text_from_element_path(TestcaseConstants.WEB_ID_PATH, TestcaseConstants.NAMESPACES)

    @property
    def title(self):
        return self.get_text_from_element_path(TestcaseConstants.TITLE_PATH, TestcaseConstants.NAMESPACES)

    @ title.setter
    def title(self, value):
        element = self.xml.find(
            TestcaseConstants.TITLE_PATH, TestcaseConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestcaseConstants.NAMESPACES["ns4"] + "}title"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def description(self):
        return self.get_text_from_element_path(TestcaseConstants.DESCRIPTION_PATH, TestcaseConstants.NAMESPACES)

    @ description.setter
    def description(self, value):
        element = self.xml.find(
            TestcaseConstants.DESCRIPTION_PATH, TestcaseConstants.NAMESPACES)
        if (element is None):
            tag = "{" + \
                TestcaseConstants.NAMESPACES["ns4"] + "}description"
            element = ET.SubElement(
                self.xml, tag)
        element.text = str(value)

    @property
    def creation_date(self):
        return self.get_text_from_element_path(TestcaseConstants.CREATION_DATE_PATH, TestcaseConstants.NAMESPACES)

    @property
    def updated(self):
        return self.get_text_from_element_path(TestcaseConstants.UPDATED_PATH, TestcaseConstants.NAMESPACES)

    @property
    def state(self):
        return self.get_attribute_from_element_path(
            TestcaseConstants.STATE_PATH,
            "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", TestcaseConstants.NAMESPACES)

    # TODO - Create setter for state

    @property
    def creator(self):
        return self.get_attributes_from_element_path(
            TestcaseConstants.CREATOR_PATH,
            ["name", "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"], TestcaseConstants.NAMESPACES)

    # TODO: Work
    # @property
    # def owner(self):
    #     pass

    @property
    def locked(self):
        return self.get_text_from_element_path(TestcaseConstants.LOCKED_PATH, TestcaseConstants.NAMESPACES)

    @property
    def weight(self):
        return self.get_text_from_element_path(TestcaseConstants.WEIGHT_PATH, TestcaseConstants.NAMESPACES)

    # TODO - Create setter for weight

    # TODO: Work
    # @property
    # def priority(self):
    #     pass

    @property
    def suspect(self):
        return self.get_text_from_element_path(TestcaseConstants.SUSPECT_PATH, TestcaseConstants.NAMESPACES)

    # TODO - Create setter for suspect

    @property
    def testcase_execution_record_count(self):
        return self.get_text_from_element_path(TestcaseConstants.TESTCASE_EXECUTION_RECORD_COUNT, TestcaseConstants.NAMESPACES)

    # TODO: Work
    # @property
    # def variables(self):
    #     pass

    @property
    def script_step_count(self):
        return self.get_text_from_element_path(TestcaseConstants.SCRIPT_STEP_COUNT, TestcaseConstants.NAMESPACES)

    @property
    def template(self):
        return self.get_attribute_from_element_path(TestcaseConstants.TEMPLATE_PATH, "href", TestcaseConstants.NAMESPACES)

    # TODO - Create setter for template

    @property
    def component(self):
        return self.get_attribute_from_element_path(TestcaseConstants.COMPONENT_PATH, "href", TestcaseConstants.NAMESPACES)

    @property
    def testcase_design(self):
        result = None

        element = self.xml.find(
            TestcaseConstants.TESTCASE_DESIGN_PATH, TestcaseConstants.NAMESPACES)

        if (element is not None):
            children_elements = list(element)
            text = None if len(children_elements) <= 0 else ET.tostring(
                children_elements[0])
            result = {"display_name": element.attrib["extensionDisplayName"],
                      "text": text}

        return result

    # TODO - Create setter for testcase_design

    @property
    def testcase_precondition(self):
        result = None

        element = self.xml.find(
            TestcaseConstants.TESTCASE_PRECONDITION_PATH, TestcaseConstants.NAMESPACES)

        if (element is not None):
            children_elements = list(element)
            text = None if len(children_elements) <= 0 else ET.tostring(
                children_elements[0])
            result = {"display_name": element.attrib["extensionDisplayName"],
                      "text": text}

        return result

    # TODO - Create setter for testcase_precondition

    @property
    def testcase_postcondition(self):
        result = None

        element = self.xml.find(
            TestcaseConstants.TESTCASE_POSTCONDITION_PATH, TestcaseConstants.NAMESPACES)

        if (element is not None):
            children_elements = list(element)
            text = None if len(children_elements) <= 0 else ET.tostring(
                children_elements[0])
            result = {"display_name": element.attrib["extensionDisplayName"],
                      "text": text}

        return result

    # TODO - Create setter for testcase_postcondition

    @property
    def testscripts(self):
        testscripts = []

        testscript_elements = self.xml.findall(
            TestcaseConstants.TESTSCRIPTS_PATH, TestcaseConstants.NAMESPACES)

        for testscript_element in testscript_elements:
            testscripts.append(testscript_element.attrib["href"])

        return testscripts

    # TODO - Create add/remove testscripts method

    # TODO - Determine how to get data
    @property
    def testcase_execution_records(self):
        testcase_execution_records = []

        testcase_execution_records_elements = self.xml.findall(
            TestcaseConstants.TESTCASE_EXECUTION_RECORDS_PATH, TestcaseConstants.NAMESPACES)

        for testscript_element in testscript_elements:
            testscripts.append(testscript_element.attrib["href"])

        return testscripts

    @property
    def variables(self):
        variables = []

        variables_elements = self.xml.findall(
            TestcaseConstants.VARIABLES_PATH, TestcaseConstants.NAMESPACES)

        for variables_element in variables_elements:
            name = variables_element.find(
                "ns2:name", TestcaseConstants.NAMESPACES).text
            value = variables_element.find(
                "ns2:value", TestcaseConstants.NAMESPACES).text
            variables.append({"name": name, "value": value})

        return variables

    # TODO - Create get for architecture element links

    # TODO - Create get for associated electronic signatures

    @property
    def attachments(self):
        attachments = []

        attachment_elements = self.xml.findall(
            TestcaseConstants.ATTACHMENTS, TestcaseConstants.NAMESPACES)

        for attachment_element in attachment_elements:
            attachments.append(attachment_element.attrib["href"])

        return attachments

    # TODO - Create method to add/remove attachments

    @property
    def testcase_expected_results(self):
        result = None

        element = self.xml.find(
            TestcaseConstants.TESTCASE_EXPECTED_RESULTS, TestcaseConstants.NAMESPACES)

        if (element is not None):
            children_elements = list(element)
            text = None if len(children_elements) <= 0 else ET.tostring(
                children_elements[0])
            result = {"display_name": element.attrib["extensionDisplayName"],
                      "text": text}

        return result

    # TODO - Create setter for testcase_expected_results
