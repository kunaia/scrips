from subprocess import Popen

err = open('error.txt', 'w+')
p = Popen(['javac', 'Main.java'], stderr=err)
p.wait()
err.close()

if p.returncode != 0:
    with open('error.txt', "r") as f:
        t = f.readline()
        s = "should be declared in a file named"
        pos = t.find(s)
        if pos == -1:
            print("Compilation Error")  # this happens if we did not found message "should be
                                        # declared in a file named" in first line of error message
        else:
            new_name = t[pos + len(s) + 1:].strip()
            print("File should be named:", new_name)
