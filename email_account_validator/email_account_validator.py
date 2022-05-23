# https://gitea.ksol.io/karolyi/py3-validate-email
from validate_email import validate_email

def start():
    address = input('Enter email: ').strip()
    is_valid = validate_email(
        email_address=address,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        smtp_helo_host=None,
        smtp_from_address=None,
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False)

    print('Valid: ' + str(is_valid))
    print('\n')
    start()

start()
