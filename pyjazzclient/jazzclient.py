import requests
import xml.etree.ElementTree as ET

from .testcase import TestCase, TestcaseConstants
from .testscript import TestScript, TestscriptConstants
from .testsuite import TestSuite, TestsuiteConstants
from .exceptions import JazzClientRequestError


class JazzClient():
    RQM_REQUEST_HEADER = {
        "OSLC-Core-Version": "2.0",
        "Accept": "application/xml",
        "Content-Type": "application/rdf+xml"
    }

    WEB_ID_OR_SLUG_REQUIRED = "web_id or slug must be provided"
    TESTCASE_MUST_BE_VALID = "testcase must be a valid TestCase"
    TESTSCRIPT_MUST_BE_VALID = "testscript must be a valid TestScript"
    TESTSUITE_MUST_BE_VALID = "testscript must be a valid TestSuite"

    def __init__(self, server_url: str, username: str, password: str, default_projects: dict = None):
        """Constructor"""
        self.__server_url = server_url
        self.__session = requests.session()
        self.__username = username
        self.__password = password
        self.__default_projects = default_projects or {"qm": "", "rm": ""}

    def __request(self, method: str = "GET", url: str = None, data: str = None,
                  headers: dict = None, auth: tuple = ("", "")) -> requests.Response:
        response = self.__session.request(method=method, url=url, data=data, headers=JazzClient.RQM_REQUEST_HEADER,
                                          allow_redirects=True, auth=auth)
        response.raise_for_status()

        print(response.text)

        return response

    def get_testcase(self, web_id: str = None, slug: str = None, revision: int = None, calm_links: bool = None,
                     oslc_links: bool = None, meta_data: bool = None, abbreviate: bool = None,
                     sort: str = None, fields: str = None, project: dict = None) -> TestCase:
        """
        """
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestcaseConstants.TESTCASE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        response = self.__request(method="GET", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        # convert response payload to xml element
        xml = ET.fromstring(response.text)

        # create a TestCase object containing the results of our request
        testcase = TestCase(xml)

        # return testcase to caller
        return testcase

    def update_testcase(self, testcase: TestCase) -> None:
        if (isinstance(testcase, TestCase) == False):
            raise ValueError(JazzClient.TESTCASE_MUST_BE_VALID)

        _ = self.__session.put(url=testcase.identifier, data=testcase.to_string(),
                               headers=JazzClient.RQM_REQUEST_HEADER, allow_redirects=True,
                               auth=(self.__username, self.__password))

    def create_testcase(self, testcase: TestCase, project: str = None) -> str:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        response = self.__request(method="POST", url=url, data=testcase.to_string(),
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        return response.headers["Content-Location"]

    def delete_testcase(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestcaseConstants.TESTCASE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make DELETE request for testcase
        _ = self.__request(method="DELETE", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def lock_testcase(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestcaseConstants.TESTCASE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        response = self.__request(method="LOCK", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def unlock_testcase(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestcaseConstants.TESTCASE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        _ = self.__request(method="UNLOCK", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def search_testcase(self, fields: str = None, modified_since: str = None, revision: bool = None,
                        calm_links: bool = None, oslc_links: bool = None, meta_data: bool = None,
                        abbreviate: bool = None, sort: bool = None, project: str = None) -> None:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestcaseConstants.TESTCASE_URL.format(project=project)

        # attempt to make GET request for testcase
        _ = self.__request(method="GET", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def get_testscript(self, web_id: str = None, slug: str = None, revision: int = None, calm_links: bool = None,
                       oslc_links: bool = None, meta_data: bool = None, abbreviate: bool = None,
                       sort: str = None, fields: str = None, project: dict = None) -> TestScript:
        """
        """
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestscriptConstants.TESTSCRIPT_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request
        response = self.__request(method="GET", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        # convert response payload to xml element
        xml = ET.fromstring(response.text)

        # create a model object containing the results of our request
        testscript = TestScript(xml)

        # return model to caller
        return testscript

    def update_testscript(self, testscript: TestScript) -> None:
        if (isinstance(testscript, TestScript) == False):
            raise ValueError(JazzClient.TESTSCRIPT_MUST_BE_VALID)

        _ = self.__session.put(url=testscript.identifier, data=testscript.to_string(),
                               headers=JazzClient.RQM_REQUEST_HEADER, allow_redirects=True,
                               auth=(self.__username, self.__password))

    def create_testscript(self, testscript: TestScript, project: str = None) -> str:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        response = self.__request(method="POST", url=url, data=testscript.to_string(),
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        return response.headers.get("Content-Location")

    def delete_testscript(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestscriptConstants.TESTSCRIPT_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to DELETE artifact
        _ = self.__request(method="DELETE", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def lock_testscript(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestscriptConstants.TESTSCRIPT_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        _ = self.__request(method="LOCK", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def unlock_testscript(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestscriptConstants.TESTSCRIPT_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        _ = self.__request(method="UNLOCK", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def search_testscript(self, fields: str = None, modified_since: str = None, revision: bool = None,
                          calm_links: bool = None, oslc_links: bool = None, meta_data: bool = None,
                          abbreviate: bool = None, sort: bool = None, project: str = None) -> None:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestscriptConstants.TESTSCRIPT_URL.format(project=project)

        # attempt to make GET request for testcase
        _ = self.__request(method="GET", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def get_testsuite(self, web_id: str = None, slug: str = None, revision: int = None, calm_links: bool = None,
                      oslc_links: bool = None, meta_data: bool = None, abbreviate: bool = None,
                      sort: str = None, fields: str = None, project: dict = None) -> TestSuite:
        """
        """
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestsuiteConstants.TESTSUITE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request
        response = self.__request(method="GET", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        # convert response payload to xml element
        xml = ET.fromstring(response.text)

        # create a model object containing the results of our request
        testsuite = TestSuite(xml)

        # return model to caller
        return testsuite

    def update_testsuite(self, testsuite: TestSuite) -> None:
        if (isinstance(testsuite, TestSuite) == False):
            raise ValueError(JazzClient.TESTSSUITE_MUST_BE_VALID)

        _ = self.__session.put(url=testsuite.identifier, data=testsuite.to_string(),
                               headers=JazzClient.RQM_REQUEST_HEADER, allow_redirects=True,
                               auth=(self.__username, self.__password))

    def create_testsuite(self, testscript: TestScript, project: str = None) -> str:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        response = self.__request(method="POST", url=url, data=testscript.to_string(),
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

        return response.headers.get("Content-Location")

    def delete_testsuite(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestsuiteConstants.TESTSUITE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to DELETE artifact
        _ = self.__request(method="DELETE", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def lock_testsuite(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestsuiteConstants.TESTSUITE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        _ = self.__request(method="LOCK", url=url,
                                  headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def unlock_testsuite(self, web_id: int = None, slug: str = None, project: str = None) -> None:
        # ensure we have either a web_id or a slug
        if (web_id is None and slug is None):
            raise ValueError(JazzClient.WEB_ID_OR_SLUG_REQUIRED)

        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        # append web_id or slug to url
        if (web_id is not None):
            url += TestsuiteConstants.TESTSUITE_URN.format(web_id=web_id)
        if (slug is not None):
            url += slug

        # attempt to make GET request for testcase
        _ = self.__request(method="UNLOCK", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))

    def search_testsuite(self, fields: str = None, modified_since: str = None, revision: bool = None,
                         calm_links: bool = None, oslc_links: bool = None, meta_data: bool = None,
                         abbreviate: bool = None, sort: bool = None, project: str = None) -> None:
        # use the provided project, if one is not provided use default_projects qm
        project = project or self.__default_projects["qm"]

        # create url string
        url = self.__server_url + \
            TestsuiteConstants.TESTSUITE_URL.format(project=project)

        # attempt to make GET request for testcase
        _ = self.__request(method="GET", url=url,
                           headers=JazzClient.RQM_REQUEST_HEADER, auth=(self.__username, self.__password))
