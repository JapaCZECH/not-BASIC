import os
import basic

shell_ver: str = "1.0"
dir: object = os.getcwd()
print(dir)

def restart(runs):
     main()
     for i in range(runs-1):
            raise KeyboardInterrupt

def main():
      global process, restarted, shell_ver, dir
      reputation = 0
      errors = True
      py_errors = False
      fn = f'shell.py'
      os.system('cls')
      print(f'not-BASIC version {shell_ver}\n'
            'Copyright (C) JapaCZECH. All rights reserved.\n'
            '---------------------------------------------')

      try: 
            while True:
                  text = input(f'BSC {dir}>')
                  if text == "--shell-end": break
                  elif text == "--shell-clear": os.system('cls')
                  elif text == "--shell-restart":  process += 1; restart(process)
                  elif text == "--shell-ver": print(f'not-BASIC {shell_ver}')
                  elif text == "--shell-no-errs": errors = False; print("Errors are OFF")
                  elif text == "--shell-errs": errors = True; print("Errors enabled")
                  elif text == "--shell-repo": print(reputation)
                  elif text == "--shell-py-errs": py_errors = True; print("Python syntax errors enabled.")
                  elif text == "--shell-py-no-errs": py_errors = False; print("Python syntax errors disabled.")
                  elif text.startswith("--shell-cd-"):
                        try:
                              if text[11:].strip() == "..":
                                    os.chdir("..")
                                    dir = os.getcwd()
                              else:
                                    os.chdir(text[11:].strip())
                                    dir = os.getcwd()                   
                        except Exception as a:
                              print(a)
                  elif text.startswith("--shell-py-"):
                        if not py_errors:
                              try:
                                    command = text[11:].strip(); exec(f"{command}")
                              except:
                                    print(f"Python command '{command}' not found.")
                        else:
                              try:
                                    command = text[11:].strip(); exec(f"{command}")
                              except Exception as e:
                                    print(e)
                  else:
                    result, error = basic.run(fn, text)
                       
                    if errors:
                        if error:
                              print(error.as_string())
                              if reputation > 0: reputation -= 1
                        elif result: print(result); reputation += 1
                  if not errors:        
                        if result: print(result); reputation +=1
                        elif error:
                              print(error.as_string())
                              if reputation > 0: reputation -= 1

      except KeyboardInterrupt:
            if restarted == 0:
                  print('\n---------------------------------------------')
                  restarted = 1

if __name__ == "__main__":
      restarted = 0
      process = 1
      main()
