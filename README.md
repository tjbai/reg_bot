

## Prerequisites:
- Knowledge of how to open the terminal and run commands
- Verify that you have `python3` installed by running `python3 --version`
  - See [this link](https://www.python.org/downloads/) for installations
- Verify that you have `git` installed by running `git --version`
  - Most of you are on Mac so `brew install git` should do the trick if it's not already installed

## Instructions
1. Copy the URL to this repository and run `git clone <this link>`
2. Navigate into the repository with `cd regbot`
3. Create a virtual environment with `python3 -m venv venv` and activate it with `source venv/bin/activate`
4. Install all the dependencies with `pip3 install -r requirements.txt`
5. Now you should be able to run the script with `python3 reg.py <list of arguments>`

Once you have this all setup, I'd recommend doing a test run just to verify that everything works correctly. Also,
the first time you use it some extra dependencies might have to be installed at runtime so you'd preferably want to take care
of that before registration.

Note that you can technically run the script and have it idle for an arbitrary amount of time before course registration, but
I'd highly recommend just running the command 5-10 minutes before registration and actively monitoring it. 

## Arguments
You want to supply the relevant time, username, and password as a list of arguments after `python reg.py`
1. The first argument is the time at which you want the bot to attempt registration. Once you activate the script, it will open a browser and wait until that time.
The format for this is <YYYY/MM/DD/HH/MM>. It uses military time, but this shouldn't matter because registration is normally at 7 am.
2. The second argument is your SIS username, which should be your hopkins ID followed by @jh.edu
3. The last argument is the password to your Hopkins email/SIS

## Example
```bash
> python3 reg.py 2023/11/12/07/00 tbai4@jh.edu password123

polling...
fired at 2023-11-12 07:00:00.418107
```
