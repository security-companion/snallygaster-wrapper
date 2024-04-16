import subprocess
import os
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT

if __name__ == '__main__':

    filename = "input.txt"

    with open(filename) as input_f:
        domains = input_f.readlines()

    for domain in domains:
        domain = domain.rstrip()
        print("scanning domain " + domain)
        # "-t", "backup_archive",
        testrun = subprocess.run(["python", "../snallygaster/snallygaster", domain ,
                                  "--nowww", "--nohttp"],
                                 stdout=subprocess.PIPE, check=True)
        output = testrun.stdout.decode("utf-8").rstrip()

        print(output)
        filename = domain + ".txt"

        result_file = open("./results/" + filename, 'a')
        result_file.write(str(datetime.now()))
        result_file.write("\r\n")
        result_file.write(str(output))
        result_file.close()

