import sys
from streamlit.web import cli as stcli

sys.argv = ['streamlit', 'run', 'retrieve.py']
sys.exit(stcli.main())