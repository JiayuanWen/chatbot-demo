## Chatbot demo
A ChatGPT powered chatbot ripped from an recent project. Posted for showcase to interested party. 

### Required installs: 
* Python 3.11
* git

### Setup
1. Open a terminal or command line, navigate to a desired location with `cd`
1. Clone the repository:
    ```bash
    git clone https://github.com/JiayuanWen/chatbot-demo.git
    ```
1. Used `cd` to get into the cloned repository folder
1. Create a Python virtual environment:
    ```bash
    python3.11 -m venv venv
    ```
1. Activate the virtual environment:
   * Windows CMD
        ```cmd
        venv\Scripts\activate
        ```
   * Windows PowerShell
        ```cmd
        venv\Scripts\Activate.ps1
        ```
   * Linux && MacOS
        ```bash 
        source ./venv/bin/activate
        ```
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
1. Request the `.env` file from me, place the file in the same folder as `main.py`.
### Launch the chatbot

Once finish setup, on a terminal or command line, type:
```bash
python main.py
```
<small>Note: You must have the Python virtual environment activated to run above command, or chatbot will not work properly. Refer to step 5 of setup.</small>
