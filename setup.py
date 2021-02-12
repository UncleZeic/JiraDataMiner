from credential import Credential


def get_credentials():
    credential = Credential("<jira_url>", "usr", "<pwd>")
    credential = Credential("https://jira.telenav.com:8443/", "marian.zeic@telenav.com", "w3e2;'w3e2")
    return credential
