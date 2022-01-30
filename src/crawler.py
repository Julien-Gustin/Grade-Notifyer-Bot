import requests
from bs4 import BeautifulSoup

def get_submit_web_page(credentials: dict) -> str:
    """Get the submition platform web page in raw associated to a student

    Args:
        credentials (dict): Dictionnary that contains 2 fields
            - 'username': 
            - 'password':
    """
    session = requests.Session() # create a session that handles cookies by default

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko)     Chrome"} 

    # Get a cookie and an authstate associated to the session
    # And ask to redirect to submit.montefiore once finished
    access_to_submit_not_log = session.get(url='https://www.intranet.ulg.ac.be/login?&request_uri2=https%3A%2F%2Fwww.intranet.ulg.ac.be%2Fjwt%2Flogin%3Fservice%3Dhttps%3A%2F%2Fsubmit.montefiore.ulg.ac.be%2Flogin', headers=headers)
    soup = BeautifulSoup(access_to_submit_not_log.text, 'html.parser')

    # Go to the identification web page given the authstate and some metadata (still on the same session)
    identification_web_page = "https://idp.uliege.be" + soup.findAll("a")[1]["href"]
    identification_web_page_text = session.get(url=identification_web_page).text
    soup = BeautifulSoup(identification_web_page_text, 'html.parser')

    # Get authState value
    auth_state = soup.find("form").find('input', {'name': 'AuthState'}).get('value')

    # Create a Post request with credentials and auth_state
    url = 'https://idp.uliege.be/simplesaml/module.php/core/loginuserpass.php?'
    myobj = {'username': credentials['username'],
            'password': credentials['password'],
            'AuthState': auth_state
            }
    post_response = session.post(url, data = myobj, headers=headers)
    soup = BeautifulSoup(post_response.text, 'html.parser')

    # Get the redirect link 
    redirect_link = soup.findAll('input')[2].get('value')
    get_response = session.get(redirect_link, headers=headers)
    soup = BeautifulSoup(get_response.text, 'html.parser')

    # Extract needed parameters to simulate the button press
    SAMLResponse = soup.find('form').find('input', {'name': 'SAMLResponse'}).get('value')
    RelayState = soup.find('form').find('input', {'name': 'RelayState'}).get('value')

    # Final POST request to access to the submit of montefiore 
    myobj = {'SAMLResponse': SAMLResponse,
            'RelayState': RelayState,
            }
    submit_webpage = session.post("https://www.intranet.ulg.ac.be/login/mellon/postResponse", data = myobj, headers=headers)
    return submit_webpage.text


def extract_project_fields(raw_web_page: str) -> dict:
    """Extract the filed relative to project

    Args:
        raw_web_page (str): raw web page of Submit of montefiore

    Returns:
        dict: A dictionnary that given a key `data-projectid` has
            - `course_id`  ~  example: INFO0970 
            - `project_name`  ~  example: Blockchain project
            - `state_info`  ~  SUBMITTED/NOT SUBMITTED/NOT VALID
            - `grade` ~ N/A or grade
    """
    projects_dict = {}

    soup_web_page = BeautifulSoup(raw_web_page, 'html.parser')
    projects = soup_web_page.findAll("tr", {"class":"beautifultd project"})
    for project in projects:
        _, state_info, grade = project.findAll("span") # [0]: date, [1]: (NOT) SUBMITTED, [2]: grade
        tmp = {}
        tmp["course_id"] = project["data-courseid"]
        tmp["project_name"] = project["data-project-name"]
        tmp["state_info"] = state_info.text      # submitted / not submitted
        tmp["grade"] = grade.text

        projects_dict[project["data-projectid"]] = tmp

    return projects_dict